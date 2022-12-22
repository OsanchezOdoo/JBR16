# -*- coding: utf-8 -*-
{
    'name': "Reporte de Información de Embarques",
    'summary': """Reporte de Información de Embarques""",
    'description': """Reporte de Información de Embarques""",
    'author': "Xmarts",
    'contributors': "javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Inventory/Inventory',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'report/shipping_manifest.xml',
        'report/fda.xml',
    ],
    'license': 'LGPL-3',
}
