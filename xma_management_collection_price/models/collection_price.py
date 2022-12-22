# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CollectionPrice(models.Model):
    _name = 'collection.price'
    _description = 'collection.price'
    _order = "name desc"

    product_category_id = fields.Many2one(
        'product.category',
        string='product category',
        required=True,
        index=True,
        ondelete='cascade'
    )
    name = fields.Date(
        string='Fecha', 
        required=True,
        index=True,
        default=fields.Date.context_today
    )
    collection_price = fields.Float('Precio acopio')
    management_price = fields.Float('Precio gerencia')
