# -*- coding: utf-8 -*-

# Created on 2019-01-04
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo12在线用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/12.0/en/index.html

# Odoo12在线开发者手册（长期更新）
# http://www.sunpop.cn/documentation/12.0/index.html

# Odoo10在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/

# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale Order Line Sequence",
    "summary": "Propagates SO line sequence to invoices and stock picking.",
    "version": "12.0.1.0.0",
    "author": "Sunpop.cn",
    "category": "Sales",
    "website": "https://www.sunpop.cn",
    "license": "AGPL-3",
    'data': [
        'views/sale_view.xml',
        'views/report_saleorder.xml',
        'data/ir_default_data.xml',
    ],
    "depends": [
        "sale",
    ],
    'post_init_hook': 'post_init_hook',
    "installable": True,
}