# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Orchard(models.Model):
    _name = 'orchard'
    _description = 'orchard'

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner id',
        required=True,
        index=True,
        ondelete='cascade')
    name = fields.Char(
        string='Huerta',
        required=True)
    sader = fields.Char(
        string='Sader')
    state_id = fields.Many2one(
        'res.country.state',
        string='Estado',
        domain="[('country_id.code', '=', 'MX')]")
    municipality_id = fields.Many2one(
        'l10n_mx_edi.res.locality',
        string='Municipio',
        domain="[('state_id', '=', state_id)]")
    locality = fields.Char(
        string='Localidad')
    is_china = fields.Boolean(
        string='China',
        default=False)
    is_ngg = fields.Boolean(
        string='GGN',
        default=False)
