# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    orchard_id = fields.Many2one(
        'orchard',
        string='Huerta',
        copy=False,
        domain="[('partner_id', '=', partner_id)]")
    sader = fields.Char(related="orchard_id.sader")
    state_id = fields.Many2one(related="orchard_id.state_id")
    municipality_id = fields.Many2one(related="orchard_id.municipality_id")
    locality = fields.Char(related="orchard_id.locality")
    is_china = fields.Boolean(related="orchard_id.is_china")
    is_ngg = fields.Boolean(related="orchard_id.is_ngg")
    price_type = fields.Selection([
        ('pactado', 'Pactado'),
        ('banda', 'A la banda')],
        string='Tipo de precio'
    )
    collector_id = fields.Many2one(
        'res.partner',
        string='Acopiador')
    cut_type = fields.Char(string='Tipo de corte')
    cutting_company = fields.Char(string='Empresa de corte')
    damage_type = fields.Char(string='Tipo de daño')
    truck = fields.Char(string='Camión')
