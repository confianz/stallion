# -*- encoding: utf-8 -*-

from odoo import api, fields, models


class SubgroupWizard(models.TransientModel):
    _name = 'subgroup.wizard'

    name = fields.Char(string='Name')
    line_ids = fields.One2many('subgroup.product', 'parent_id', string="Subgroup")



SubgroupWizard()



class SubgroupProduct(models.TransientModel):
    _name = 'subgroup.product'

    name = fields.Many2one('product.subgroup', string='Subgroup', required=True)
    product_ids = fields.One2many('product.product', 'subgroup_id', string='Products')
    parent_id = fields.Many2one('subgroup.wizard', string="Subgroup")


    @api.onchange('name')
    def _onchange_name(self):
        product_ids = self.name.product_ids.ids
        res = {}
        res['domain'] = {'product_ids':[('id', 'in', product_ids)]}
        return res



SubgroupProduct()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
