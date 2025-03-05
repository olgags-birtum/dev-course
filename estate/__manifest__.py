# -*- coding: utf-8 -*-
{
    "name": "Estate",
    "summary": "Test module",
    "description": "Real estate module",
    "author": "Olga",
    "website": "estate04marzo.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["crm"],
    # always loaded
    "data": [
        "security/res_group.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
