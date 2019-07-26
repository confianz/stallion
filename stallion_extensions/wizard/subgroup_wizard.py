# -*- encoding: utf-8 -*-

from odoo import api, fields, models
import itertools

class SubgroupWizard(models.TransientModel):
    _name = 'subgroup.wizard'

    name = fields.Char(string='Name')
    line_ids = fields.One2many('subgroup.wizard.line', 'parent_id', string="Subgroup")





    @api.multi
    def action_create_product(self):
        active_model = self._context.get('active_model', False)
        active_id = self._context.get('active_id', False)

        route_id = self.env['stock.location.route'].search([('name', '=', 'Manufacture')], limit=1)

        for rec in self:

            new_product = self.env['product.product'].create({
                                                                'name': rec.name,
                                                                'route_ids': [(6, 0, route_id.ids)],
                                                             })
            if new_product:
                bom = self.env['mrp.bom'].create({
                                                    'product_tmpl_id': new_product.product_tmpl_id.id,
                                                    'product_id': new_product.id,
                                                    'product_qty': 1,
                                                    'type': 'phantom',
                                                    'bom_line_ids': [(0, 0, {'product_id': rec_line.product_id.id, 'product_qty': rec_line.quantity}) for rec_line in rec.line_ids],
                                                 })

                if active_model == 'sale.order' and active_id and bom:
                    self.env[active_model].browse(active_id).write({'order_line': [(0, 0, {'product_id': new_product.id, 'name': new_product.name})]})



SubgroupWizard()



class SubgroupWizardLine(models.TransientModel):
    _name = 'subgroup.wizard.line'

    parent_subgroup_id = fields.Many2one('product.subgroup', string='Parent Subgroup')
    subgroup_id = fields.Many2one('product.subgroup', string='Subgroup')
    product_id = fields.Many2one('product.product', string='Products')
    parent_id = fields.Many2one('subgroup.wizard', string="Parent")
    quantity = fields.Float(string='Qty Req', default=1.0)
    qty_oh = fields.Float(string='Qty Available', related='product_id.virtual_available')


    @api.onchange('parent_subgroup_id')
    def _onchange_parent_subgroup_id(self):
        child_subgroup_ids = self.parent_subgroup_id and self.parent_subgroup_id.child_subgroup_ids and self.parent_subgroup_id.child_subgroup_ids.ids or []
        res = {}
        res['domain'] = {'subgroup_id':[('id', 'in', child_subgroup_ids)]}
        self.subgroup_id = False
        self.product_id = False
        return res


    @api.onchange('subgroup_id')
    def _onchange_subgroup_id(self):
        product_ids = self.subgroup_id and self.subgroup_id.product_ids and self.subgroup_id.product_ids.ids or []
        res = {}
        res['domain'] = {'product_id':[('id', 'in', product_ids)]}
        self.product_id = False
        return res



SubgroupWizardLine()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
