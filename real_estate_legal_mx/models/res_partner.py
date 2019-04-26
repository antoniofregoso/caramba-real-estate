# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

from odoo import api, fields, models, tools

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    nationality = fields.Char('Nationality', size=64)
    identification_type = fields.Char('Identification Type', size=64)
    identification_no = fields.Char('Identification Number', size=64)    
    birthdate = fields.Date('Birthdate')
    age = fields.Integer('Age')