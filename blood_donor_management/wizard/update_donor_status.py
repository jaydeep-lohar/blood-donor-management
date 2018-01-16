
from odoo import models, api, fields

class Update_donor_status(models.TransientModel):
    _name = 'update.donor.status'
    _description = 'Update donor status if 1 then eligible to donate blood & 0 then not eligible'

    donor_status=fields.Boolean(string='Donor status')

    @api.multi
    def update_donor_status(self):
        active_ids = self.env.context['active_ids']
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:            
            if line.donor_status==False:
                line.write({'donor_status':True})
            elif line.donor_status==True:
                line.write({'donor_status':False})
            else:
                pass



    # @api.model
    # def create(self,vals):
    #     obj = super(Update_donor_status,self).create(vals)
    #     template = self.env.ref('blood_donor_management.update_donor_status_true',raise_if_not_found=False)
    #     template.send_mail(obj.id)
    #     print("------------------------------------------------------------------")
    #     return obj


    @api.model
    def create(self,vals):
        obj = super(Update_donor_status,self).create(vals)
        active_ids = self.env.context['active_ids']
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:
            if line.donor_status==True:
                template = self.env.ref('blood_donor_management.on_update_status_false',raise_if_not_found=False)
                template.send_mail(obj.id)
            elif line.donor_status==False:
                template = self.env.ref('blood_donor_management.on_update_status_true',raise_if_not_found=False)
                template.send_mail(obj.id)
        return obj