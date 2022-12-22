# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    orchard_line_ids = fields.One2many(
        'orchard',
        'partner_id',
        string='líneas de huerta',
        copy=False)
