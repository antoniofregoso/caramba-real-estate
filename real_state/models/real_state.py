


from odoo import api, fields, models

class RealStateDevelopment(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'real_state.development'
    _description = 'Real State Development'
    _order = 'license_plate asc, acquisition_date asc'
    
    name = fields.Char('Name', required=True, translate=True)
    active = fields.Boolean(default=True)
    website_published = fields.Boolean(tracking=True)
    color = fields.Integer('Kanban Color Index')
    sequence = fields.Integer('Sequence')
    state = fields.Selection([
        ('draft', 'Draft'),('testing', 'Testing'),
        ('onsale', 'On Sale'), ('sold', 'Sold'), ('cancel', 'Cancelled')],
        string='Status', default='draft', required=True, copy=False, track_visibility='onchange', group_expand='_expand_states')
    ref = fields.Char(string='Internal Reference')
    type = fields.Selection([('online', 'Online'),('offline', 'Offline')], string='Type', required=True, default='online')
