from odoo import models, fields, api, _


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    freight = fields.Integer('Freight')
    duty = fields.Integer('Duty')
    doc_charges = fields.Integer('Doc. Charges')
    vat = fields.Integer('VAT')

    tab_payment = fields.Char('Payment')
    tab_delivery = fields.Char('Delivery')
    tab_incoterms = fields.Char('Incoterms')
    tab_standards = fields.Char('Standards')
    tab_others = fields.Char('Others')

    @api.depends('order_line.price_total', 'freight', 'duty', 'doc_charges', 'vat')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax + order.freight + order.duty + order.doc_charges
            })
