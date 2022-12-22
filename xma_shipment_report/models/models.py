# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class xma_shipment_report(models.Model):
#     _name = 'xma_shipment_report.xma_shipment_report'
#     _description = 'xma_shipment_report.xma_shipment_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
