# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritProductTemplate(models.Model):
    _inherit = "product.template"

    item_code = fields.Char(string="Item Code")
    description = fields.Char(string="Description")
    cost_trans = fields.Float(string="Cost+Trans")
    weight = fields.Integer(string="Weight")
    uom_2 = fields.Integer(string="UOM2")
    uom = fields.Integer(string="$/UOM2")
    dim_1 = fields.Char(string="Dim1")
    dim_2 = fields.Char(string="Dim2")
    thickness = fields.Float(string="Thickness")
    density = fields.Float(string="Density")
    pool_cost = fields.Integer(string="Pool Cost")
    type = fields.Selection([
        # ('receive', 'Receivable'),
        # ('pay', 'Payable'),
    ], string='Type')
    hs_code = fields.Integer(string="HS Code")
    finish = fields.Integer(string="Finish")

    @api.onchange('standard_price' , 'cost_trans')
    def calculate_cost_trans(self):
        self.cost_trans = self.standard_price + ((self.standard_price/100)*8)






