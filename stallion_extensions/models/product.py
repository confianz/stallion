# -*- coding: utf-8 -*-

from odoo import _, api, fields, models




class ProductProduct(models.Model):
    _inherit = 'product.product'

    condition = fields.Selection([('new', 'New'), ('refurb', 'Refurbished')], string='Condition')
    group = fields.Selection([('hdd', 'HDD'), ('ssd', 'SSD')], string='Group')
    brand_id = fields.Many2one('product.brand', string='Brand')
    subgroup_id = fields.Many2one('product.subgroup', string='Subgroup')
    manufacturer_id = fields.Many2one('product.mfg', string='MFG')


ProductProduct()



class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string='Name')

ProductBrand()



class ProductSubgroup(models.Model):
    _name = 'product.subgroup'

    name = fields.Char(string='Name')

ProductSubgroup()


class ProductMfg(models.Model):
    _name = 'product.mfg'

    name = fields.Char(string='Name')

ProductMfg()


