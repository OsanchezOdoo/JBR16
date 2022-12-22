# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta, date

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    lot_id = fields.Many2one(
        string="Lote de producto aguacate",
        related="move_raw_ids.move_line_ids.lot_id"
    )
    lot_name = fields.Char(
        string="Lote",
        related="lot_id.name",
        store=True
    )
    collec_price = fields.Float(
        string="Acopio",
        compute="_get_acopio_price",
        store=True
    )
    manage_price = fields.Float(
        string="Gerencia",
        compute="_get_acopio_price",
        store=True
    )
    qty_line = fields.Float(
        string="Por consumir",
        related="move_raw_ids.product_uom_qty"
    )
    # related_collection_ids = fields.One2many(
    #     related="product_id.categ_id.collection_price_ids",
    #     store=True
    # )

    @api.depends(
        "product_id.categ_id.collection_price_ids", 
        "product_id.categ_id.collection_price_ids.name",
        "product_id.categ_id.collection_price_ids.collection_price",
        "product_id.categ_id.collection_price_ids.management_price")
    def _get_acopio_price(self):
        for rec in self:
            if rec.product_id:
                if rec.product_id.categ_id.collection_price_ids:
                    today = fields.Date.today()
                    for r in rec.product_id.categ_id.collection_price_ids:
                        if today == r.name:
                            rec.collec_price = r.collection_price
                            rec.manage_price = r.management_price
                        else:
                            rec.collec_price = None
                            rec.manage_price = None
                else:
                    rec.collec_price = None
                    rec.manage_price = None
            else:
                rec.collec_price = None
                rec.manage_price = None


    
    # lot_id = fields.Many2one(
    #     "hr.employee",
    #     string="Lote de producto aguacate",
    #     compute="_search_lot"
    # )

    # lot_rel_id = fields.Many2one(
    #     string="Lote de producto aguacate relación",
    #     related="lot_id",
    #     store=True
    # )
    
    # def _search_lot(self):
    #     if self.product_id.tracking == "lot":
    #         if self.move_raw_ids:
    #             for raw in self.move_raw_ids:
    #                 if raw.move_line_ids:
    #                     for line in raw.move_line_ids:
    #                         self.lot_id = line.lot_id
    #                         return
    #                 else:
    #                     return
    #         else:
    #             return
    #     else:
    #         return

    
    # def get_categ_acopio(self):
    #     mrp = self.env["mrp.production"].search([("lot_producing_id","=", self.lot_producing_id.id)])
    #     datas = []
    #     for rec in mrp:
    #         data = {"name_categ": rec.product_id.categ_id.name}
    #         datas.append(data)
    #     return datas