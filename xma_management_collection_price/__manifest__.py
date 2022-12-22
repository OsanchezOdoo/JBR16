# -*- coding: utf-8 -*-
{
    'name': "Reporte Lista de precios de acopio y Gerencia",
    'summary': """Reporte Lista de precios de acopio y Gerencia""",
    'description': """Reporte Lista de precios de acopio y Gerencia""",
    'author': "Xmarts",
    'contributors': "javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'product',
        'mrp',
        #'xma_orchard_catalog',
    ],
    'data': [
        'security/ir.model.access.csv',
        #'wizard/wizard_report_lot_view.xml',
        'views/inherit_product_category_views.xml',
        'views/inherit_mrp_production_tree_view.xml',
        'report/collection_price.xml',
        #'report/wizard_collection_price.xml',
    ],
    'license': 'LGPL-3',
}
