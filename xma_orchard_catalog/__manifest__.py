# -*- coding: utf-8 -*-
{
    'name': "Catálogo de huertas",
    'summary': """Crear campos en el catálogo de proveedores que se hereden en la compra""",
    'description': """Crear campos en el catálogo de proveedores que se hereden en la compra""",
    'author': "Xmarts",
    'contributors': "javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Inventory/Purchase',
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'contacts',
        'purchase',
        'l10n_mx_edi',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_res_partner_views.xml',
        'views/inherit_purchase_order_views.xml',
    ],
    'license': 'LGPL-3',
}
