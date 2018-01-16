
from odoo import models, api, fields

class Update_donor_status(models.TransientModel):
    _name = 'update.donor.status'
    _description = 'Update donor status if 1 then eligible to donate blood & 0 then not eligible'
    # course_id = fields.Many2one('course.details',string='Course')
    # student_id=fields.Many2many('res.partner',string='Student',domain="[('course_id','=',course_id)]")
    donor_status=fields.Boolean(string='Donor status',default=False)

    @api.multi
    def update_donor_status(self):
        active_ids = self.env.context['active_ids']
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:
            line.write({'donor_status':True})


    @api.model
    def create(self,vals):
        obj = super(Update_donor_status,self).create(vals)
        template = self.env.ref('blood_donor_management.on_update_status',raise_if_not_found=False) #note here registration is template id of registration_template.xml
        template.send_mail(obj.id)
        return obj