# -*- encoding: utf-8 -*-

from odoo import api, fields, models
import itertools

class SubgroupWizard(models.TransientModel):
    _name = 'subgroup.wizard'

    name = fields.Char(string='Name')
    line_ids = fields.One2many('subgroup.wizard.line', 'parent_id', string="Subgroup")





    @api.multi
    def action_create_product(self):
        route_id = self.env['stock.location.route'].search([('name', '=', 'Manufacture')], limit = 1)

        for rec in self:
            line_products = []
            all_products_combinations = []
            for line in rec.line_ids:
                line_products.append(line.product_ids.ids)


            all_products_combinations = list(itertools.product(*line_products))

        if route_id:
            index = 1
            for product_combination in all_products_combinations:
                new_product = self.env['product.product'].create({
                                                                    'name':'New Product %s' %(index),
                                                                    'route_ids': [(6, 0, route_id.ids)],
                                                                 })
                index += 1
                bom = self.env['mrp.bom'].create({
                                                    'product_tmpl_id': new_product.product_tmpl_id.id,
                                                    'product_id': new_product.id,
                                                    'product_qty': 1,
                                                    'type': 'phantom',
                                                    'bom_line_ids': [(0, 0, {'product_id': pid, 'product_qty': 1}) for pid in product_combination],
                                                 })







SubgroupWizard()



class SubgroupWizardLine(models.TransientModel):
    _name = 'subgroup.wizard.line'

    parent_subgroup_id = fields.Many2one('product.subgroup', string='Parent Subgroup')
    subgroup_id = fields.Many2one('product.subgroup', string='Subgroup')
    product_ids = fields.Many2many('product.product', string='Products')
    parent_id = fields.Many2one('subgroup.wizard', string="Parent")


    @api.onchange('parent_subgroup_id')
    def _onchange_parent_subgroup_id(self):
        child_subgroup_ids = self.parent_subgroup_id and self.parent_subgroup_id.child_subgroup_ids and self.parent_subgroup_id.child_subgroup_ids.ids or []
        res = {}
        res['domain'] = {'subgroup_id':[('id', 'in', child_subgroup_ids)]}
        self.subgroup_id = False
        self.product_ids = False
        return res


    @api.onchange('subgroup_id')
    def _onchange_subgroup_id(self):
        product_ids = self.subgroup_id and self.subgroup_id.product_ids and self.subgroup_id.product_ids.ids or []
        res = {}
        res['domain'] = {'product_ids':[('id', 'in', product_ids)]}
        self.product_ids = False
        return res



SubgroupWizardLine()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
