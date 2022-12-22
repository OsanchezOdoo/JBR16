from odoo import api, fields, models

class WizardReportLot(models.TransientModel):
    _name = "wizard.report.lot"
    _description = "Wizard para la generación de reportes por lotes"

    stock_lot_id = fields.Many2one(
        "stock.production.lot",
        string="Número de serie o Lote",
        required=True
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto"
    )
    mrp_ids = fields.Many2many(
        "mrp.production",
        string="Ordenes de producción"
    )
    
    def pdf_report_lot(self):
        categories = [m.product_id.categ_id.name for m in self.mrp_ids]
        datas = {
            "categories_record": categories,
        }
        return self.env.ref("xma_management_collection_price.collection_price_report_action_wizard").report_action(self, data=datas)