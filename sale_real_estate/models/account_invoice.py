# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models

class AcountInvoice(models.Model):
    _inherit  = "account.invoice"  
     
    @api.multi
    def set_payment_schedule(self):
        for inv in self:
            order=self.env['sale.order'].search([('name','=',inv.origin)])
            payments_date=self.env['account.move.line'].search([('ref','=',inv.origin),('credit','=',0.0)])
            timetable = []
            timetable.append((order.date_confirm,order.reservation,'F'))
            for item in payments_date:
                x=(item.date_maturity,item.debit,'I')
                timetable.append(x)
            timetable.sort()
            second_payment= (timetable[1][0],timetable[1][1]-order.reservation,'I')
            timetable[1]=second_payment
            i=len(timetable)-1
            last_payment=(timetable[i][0],timetable[i][1],'L')
            timetable[i]=last_payment
            i=1
            for payment in timetable:
                schedule ={}
                schedule['order_id']=order.id
                schedule['payment_date']=payment[0]
                schedule['quantity']=payment[1]
                schedule['type']=payment[2]
                schedule['order']=i
                due_date = self.env['sale.order.payment_schedule'].create(schedule)
                i+=1
        return True       