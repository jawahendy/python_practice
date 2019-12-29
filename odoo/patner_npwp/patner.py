from odoo import api, fields, models

class patner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    npwp = fields.Char(string="NPWP", size=20, required=False)
    so_ids2 = fields.One2many(string="Sale Orders", comodel_name="sale.order", inverse_name="partner_id")

    # # @api.multi
    # @api.depends('account.invoice')
    # def create_invoice(self):
    #     obj_inv = self.env['account.invoice']
    #     obj_acc = self.env['account.account']

    #     account = obj_acc.search([(
    #         'name','=','Product Sales'
    #     )])

    #     data = {
    #         'partner_id': self.id,
    #         'invoice_line_ids': [
    #             (0,0,{
    #                 'name' : 'subscription',
    #                 'quatity' : 1.0,
    #                 'price_unit' : 40,
    #                 'account_id' :  account[0].id
    #             })
    #         ]
    #     }
    #     obj_inv.create(data)
    


    
