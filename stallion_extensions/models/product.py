# -*- coding: utf-8 -*-

from odoo import api, fields, models, _




class ProductTemplate(models.Model):
    _inherit = 'product.template'

    condition = fields.Selection([('new', 'New'), ('refurb', 'Refurbished')], string='Condition')
    group = fields.Selection([('hdd', 'HDD'), ('ssd', 'SSD')], string='Group')
    brand_id = fields.Many2one('product.brand', string='Brand')
    subgroup_id = fields.Many2one('product.subgroup', string= 'Subgroup')
    manufacturer_id = fields.Many2one('product.mfg', string='MFG')
    qty_product = fields.Integer(string="Quantity", compute='_compute_qty_product')
    is_manufactured = fields.Boolean(string= 'Is Manufactured', compute='_compute_is_manufactured', default=False)


    @api.depends('is_manufactured','bom_ids')
    def _compute_qty_product(self):
        if self.is_manufactured and self.bom_ids:
            bom = self.bom_ids and self.bom_ids[0]
            self.qty_product = min([i.product_id.qty_available for i in bom.bom_line_ids])


    @api.depends('route_ids')
    def _compute_is_manufactured(self):
        mrp_routes = self.route_ids.filtered(lambda s:s.name=='Manufacture')
        if len(mrp_routes):
            self.is_manufactured = True
        else:
            self.is_manufactured = False



ProductTemplate()



class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string= 'Name', required=True)
    description = fields.Char(string="Description")
    product_ids = fields.One2many('product.product', 'brand_id', string='Products')


ProductBrand()



class ProductSubgroup(models.Model):
    _name = 'product.subgroup'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string="Description")
    product_ids = fields.One2many('product.product', 'subgroup_id', string='Products')


ProductSubgroup()



class ProductMfg(models.Model):
    _name = 'product.mfg'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string="Description")
    product_ids = fields.One2many('product.product', 'manufacturer_id', string='Products')


ProductMfg()


