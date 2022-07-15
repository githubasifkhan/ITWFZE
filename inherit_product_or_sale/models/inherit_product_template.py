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

    service_tracking = fields.Selection([
        ('no', 'Don\'t create task'),
        ('task_global_project', 'Create a task in an existing project'),
        ('task_in_project', 'Create a task in sales order\'s project'),
        ('project_only', 'Create a new project but no task')],
        string="Service Tracking", default="no",
        help="On Sales order confirmation, this product can generate a project and/or task. \
            From those, you can track the service you are selling.\n \
            'In sale order\'s project': Will use the sale order\'s configured project if defined or fallback to \
            creating a new project based on the selected template.")
    project_id = fields.Many2one(
        'project.project', 'Project', company_dependent=True,
        domain="[('company_id', '=', current_company_id)]",
        help='Select a billable project on which tasks can be created. This setting must be set for each company.')
    project_template_id = fields.Many2one(
        'project.project', 'Project Template', company_dependent=True, copy=True,
        domain="[('company_id', '=', current_company_id)]",
        help='Select a billable project to be the skeleton of the new created project when selling the current product. Its stages and tasks will be duplicated.')

    @api.onchange('standard_price' , 'cost_trans')
    def calculate_cost_trans(self):
        self.cost_trans = self.standard_price + .08






