# -*- coding: utf-8 -*-
{
    "name": "Estate",
    "summary": "Test module",
    "description": "Real estate module",
    "author": "Olga",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["crm"],
    # always loaded
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
