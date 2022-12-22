# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_collection_price = fields.Boolean(
        string='Precio acopio-gerencia ',
        default=False
    )
    collection_price_ids = fields.One2many(
        'collection.price',
        'product_category_id',
        string='Líneas de precio gerencia',
        copy=False
    )
