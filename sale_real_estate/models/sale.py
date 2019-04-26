# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import api, fields, models, exceptions
import time

class SaleOrderPaymentSchedule(models.Model):
    _name  = "sale.order.payment_schedule" 
    _description ="payment schedule" 
    
    order_id = fields.many2one('sale.order', 'Order Reference', ondelete='cascade')
    payment_date = fields.datetime('Reservation')
    quantity = fields.float('Reservation')
    type = fields.char('Type', size=1)
    order = fields.integer('Order')
    
    
class SaleOrderLine(models.Model):
    _inherit  = "sale.order.line" 
    
    
    UNIDADES = (
        '',
        'UN ',
        'DOS ',
        'TRES ',
        'CUATRO ',
        'CINCO ',
        'SEIS ',
        'SIETE ',
        'OCHO ',
        'NUEVE ',
        'DIEZ ',
        'ONCE ',
        'DOCE ',
        'TRECE ',
        'CATORCE ',
        'QUINCE ',
        'DIECISEIS ',
        'DIECISIETE ',
        'DIECIOCHO ',
        'DIECINUEVE ',
        'VEINTE '
            )
    
    DECENAS = (
        'VENTI',
        'TREINTA ',
        'CUARENTA ',
        'CINCUENTA ',
        'SESENTA ',
        'SETENTA ',
        'OCHENTA ',
        'NOVENTA ',
        'CIEN '
        )
    
    CENTENAS = (
        'CIENTO ',
        'DOSCIENTOS ',
        'TRESCIENTOS ',
        'CUATROCIENTOS ',
        'QUINIENTOS ',
        'SEISCIENTOS ',
        'SETECIENTOS ',
        'OCHOCIENTOS ',
        'NOVECIENTOS '
        )
    
    UNITS = (
        ('',''),
        ('MIL ','MIL '),
        ('MILLON ','MILLONES '),
        ('MIL MILLONES ','MIL MILLONES '),
        ('BILLON ','BILLONES '),
        ('MIL BILLONES ','MIL BILLONES '),
        ('TRILLON ','TRILLONES '),
        ('MIL TRILLONES','MIL TRILLONES'),
        ('CUATRILLON','CUATRILLONES'),
        ('MIL CUATRILLONES','MIL CUATRILLONES'),
        ('QUINTILLON','QUINTILLONES'),
        ('MIL QUINTILLONES','MIL QUINTILLONES'),
        ('SEXTILLON','SEXTILLONES'),
        ('MIL SEXTILLONES','MIL SEXTILLONES'),
        ('SEPTILLON','SEPTILLONES'),
        ('MIL SEPTILLONES','MIL SEPTILLONES'),
        ('OCTILLON','OCTILLONES'),
        ('MIL OCTILLONES','MIL OCTILLONES'),
        ('NONILLON','NONILLONES'),
        ('MIL NONILLONES','MIL NONILLONES'),
        ('DECILLON','DECILLONES'),
        ('MIL DECILLONES','MIL DECILLONES'),
        ('UNDECILLON','UNDECILLONES'),
        ('MIL UNDECILLONES','MIL UNDECILLONES'),
        ('DUODECILLON','DUODECILLONES'),
        ('MIL DUODECILLONES','MIL DUODECILLONES'),
        )
    
        
    def _convert_group(self, n):
        """Turn each group of numbers into letters"""
        output = ''   
    
        if(n == '100'):
            output = "CIEN "
        elif(n[0] != '0'):
            output = self.CENTENAS[int(n[0]) - 1]
    
        k = int(n[1:])
        if(k <= 20):
            output += self.UNIDADES[k]
        else:   
            if((k > 30) & (n[2] != '0')):
                output += '%sY %s' % (self.DECENAS[int(n[1]) - 2], self.UNIDADES[int(n[2])])
            else:
                output += '%s%s' % (self.DECENAS[int(n[1]) - 2], self.UNIDADES[int(n[2])])
        return output

    
    def _hundreds_word(self, number):       
        converted = ''
        if not (0 < number < 1000):
            return 'No es posible convertir el numero a letras'
    
        number_str = str(number).zfill(9)  
        cientos = number_str[6:]   
        if(cientos):
            if(cientos == '001'):
                converted += 'UN '
            elif(int(cientos) > 0):
                converted += '%s ' % self._convert_group(cientos)
    
    
        return converted.title().strip() 
    
    def _to_word(self, quantity):
        i = int(quantity)
        j= round(abs(quantity) - abs(int(quantity)),2)
        f = str(j).split('.')[1]
        human_readable = []
        num_units = format(i,',').split(',')
        #print num_units
        for i,n in enumerate(num_units): 
            if int(n) != 0:
                words = self._hundreds_word(int(n))          
                units = self.UNITS[len(num_units)-i-1][0 if int(n) == 1 else 1] 
                human_readable.append([words,units])      
    
        #filtrar MIL MILLONES - MILLONES -> MIL - MILLONES
        for i,item in enumerate(human_readable):
            try:
                if human_readable[i][1].find(human_readable[i+1][1]):
                    human_readable[i][1] = human_readable[i][1].replace(human_readable[i+1][1],'')
            except IndexError:
                pass
        human_readable = [item for sublist in human_readable for item in sublist]
        human_readable_str =  ' '.join(human_readable).replace('  ',' ').lower().strip() + ' pesos ' + str(f).zfill(2) + '/100 M.N.'
        #human_readable.append(moneda)
        return human_readable_str
    
    def _get_values(self, cr,uid, ids, field_value, arg, context):
        order_line=self.pool.get('sale.order.line').browse(cr, uid,ids, context=context )
        order =  self.pool.get('sale.order').browse(cr, uid,[order_line.order_id.id], context=context )
        payments_ids = self.pool.get('account.payment.term.line').search(cr, uid, [('payment_id','in',[order.payment_term.id])], context=context )
        payments = self.pool.get('account.payment.term.line').browse(cr, uid, payments_ids, context=context )
        res = {}
        for sale in order_line:
            if field_value=='downpayment':                
                amount=0
                for payment in payments:
                    if payment.value == 'procent':
                        amount+= sale.price_subtotal*payment.value_amount
                    elif payment.value =='fixed':
                        amount+= payment.value_amount
                    else:                    
                        amount+= 0
            elif field_value=='mortgage':
                dp=0
                for payment in payments:
                    if payment.value == 'procent':
                        dp+= sale.price_subtotal*payment.value_amount
                    elif payment.value =='fixed':
                        dp+= payment.value_amount
                amount = sale.price_subtotal-dp
            elif field_value=='signing':  
                amount=0
                try:
                    first=sorted(payments, key=lambda objeto: objeto.days, reverse=False)[0]
                except Exception:
                    raise osv.except_osv(_('Error!'), _("You must select a Payment Term"))
                if first.value == 'procent':
                    amount= sale.price_subtotal*first.value_amount-order.reservation
                elif first.value =='fixed':  
                    amount= first.value_amount-order.reservation
                elif first.value=='balance':
                    amount= sale.price_subtotal-order.reservation
                else:
                    amount=0
            elif field_value=='monthly':
                size = len(payments)
                i = size-2
                amount=i
            else:
                amount=0
                first=sorted(payments, key=lambda objeto: objeto.days, reverse=False)[0]
                if first.value!='balance':
                    try:
                        second=sorted(payments, key=lambda objeto: objeto.days, reverse=False)[1]
                    except Exception:
                        res['warning'] = {
                            'title': _('Error!'),
                            'message': _('You must select a Payment Term.')
            }
                    if second.value == 'procent':
                            amount= sale.price_subtotal*second.value_amount
                    elif second.value =='fixed':
                        amount= second.value_amount
                    else:
                        amount=0
                else:
                    amount=0
        res[order_line.id]= amount
        return res
    
    def to_word(self, quantity,money=True):   
        i = int(quantity)
        j= round(abs(quantity) - abs(int(quantity)),2)
        f = str(j).split('.')[1]
        human_readable = []
        num_units = format(i,',').split(',')
        #print num_units
        for i,n in enumerate(num_units): 
            if int(n) != 0:
                words = self._hundreds_word(int(n))          
                units = self.UNITS[len(num_units)-i-1][0 if int(n) == 1 else 1] 
                human_readable.append([words,units])      
    
        #filtrar MIL MILLONES - MILLONES -> MIL - MILLONES
        for i,item in enumerate(human_readable):
            try:
                if human_readable[i][1].find(human_readable[i+1][1]):
                    human_readable[i][1] = human_readable[i][1].replace(human_readable[i+1][1],'')
            except IndexError:
                pass
        human_readable = [item for sublist in human_readable for item in sublist]
        integer_part = ' '.join(human_readable).replace('  ',' ').lower().strip()
        if money:        
            human_readable_str = integer_part  + ' pesos ' + str(f).zfill(2) + '/100 M.N.'
            return human_readable_str
        else:
            return integer_part
        #human_readable.append(moneda)
        
class SaleOrder(models.Model):    
    __inherit = "sale.order"
    
    contract_singing_date= fields.Date('Contract Signing Date')
    
    
    