# -*- encoding: utf-8 -*-
#
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2014 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#
#    Coded by: Luis Torres (luis_t@vauxoo.com)
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    "name": "HR payslip paid",
    "version": "1.0",
    "author": "Vauxoo",
    "category": "Localization/Mexico",
    "description": """
    This module add the state paid in hr payroll

    Note:
    If you have registers of payslip before to this module, you can run the
    next Web Service:
    github.com/vauxoo-dev/gist-vauxoo/blob/master/update_state_paid_payslip.py
    to change to paid the payslips that have your payment.
    """,
    "website": "http://www.vauxoo.com/",
    "license": "AGPL-3",
    "depends": [
        "hr_payroll_account",
        "hr_payroll_cancel"
    ],
    "demo": [],
    "data": [
        "view/hr_payslip_workflow.xml",
        "view/hr_payslip_view.xml"
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
    "active": False
}
