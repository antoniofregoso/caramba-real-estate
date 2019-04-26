# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit  = "res.company"
    
    deed = fields.Many2one('Public Deed')
    deed_date = fields.Date('Date Deed')
    notary_public = fields.Many2one('res.partner', 'Deed Notary Public')
    deed_folio = fields.Char('Mercantile Folio')
    deed_folio_date = fields.Date('Date Folio')
    deed_country_id = fields.Many2one('res.country', 'Deed Country', ondelete='restrict')
    deed_state_id = fields.Many2one("res.country.state", 'Deed State', ondelete='restrict')
    deed_city = fields.Char('Deed City')
    legal_representative1 = fields.Many2one('res.partner', 'Legal Rep. 1')
    legal_representative2 = fields.Many2one('res.partner', 'Legal Rep. 2')
    legal_representative3 = fields.Many2one('res.partner', 'Legal Rep. 3')
    lr_deed = fields.Char('Public Deed')
    lr_deed_date = fields.Date('Date Deed')
    lr_notary_public = fields.Many2one('res.partner', 'Deed Notary Public')
    lr_deed_folio = fields.Char('Mercantile Folio')
    lr_deed_folio_date = fields.Date('Date Folio')
    lr_deed_country_id = fields.Many2one('res.country', 'Deed Country', ondelete='restrict')
    lr_deed_state_id = fields.Many2one("res.country.state", 'Deed State', ondelete='restrict')
    lr_deed_city = fields.Char('Deed City')
    contractual_penalty = fields.Float('Contractual Penalty %',help='Interest Rate Penalty for breach of contract applied to the total price agreed in the contract')
    days_money_back1 = fields.Integer('Days to Money Back', help='If company breaches the contract')
    penality_money_back1 = fields.Float('Interest Rate %', help='Daily interest rate to be applied if the company does not return the money  in the stipulated time when company breaches the contract')
    days_money_back2 = fields.Integer('Days to Money Back', help='If client breaches the contract')
    penality_money_back2 = fields.Float('Interest Rate %', help='Daily interest rate to be applied if the company does not return the money  in the stipulated time when client breaches the contract')
    contract_verification = fields.Many2one('res.partner', 'Verified By',help='Authority verifies the contract')
    contract_verification_ref = fields.Char('Verified Ref')
    contract_verification_date = fields.Date('Verification Date')
    
    
    