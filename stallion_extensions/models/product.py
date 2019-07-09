# -*- coding: utf-8 -*-

from odoo import api, fields, models, _




class ProductTemplate(models.Model):
    _inherit = 'product.template'

    condition = fields.Selection([('new', 'New'), ('refurb', 'Refurbished')], string='Condition')
    group = fields.Selection([('hdd', 'HDD'), ('ssd', 'SSD')], string='Group')
    brand_id = fields.Many2one('product.brand', string='Brand')
    subgroup_id = fields.Many2one('product.subgroup', string='Subgroup')
    manufacturer_id = fields.Many2one('product.mfg', string='MFG')


ProductTemplate()



class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string = "Description")
    product_ids = fields.One2many('product.template', 'brand_id', string='Products')

ProductBrand()



class ProductSubgroup(models.Model):
    _name = 'product.subgroup'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string = "Description")
    product_ids = fields.One2many('product.template', 'subgroup_id', string='Products')

ProductSubgroup()


class ProductMfg(models.Model):
    _name = 'product.mfg'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string = "Description")
    product_ids = fields.One2many('product.template', 'manufacturer_id', string='Products')

ProductMfg()


