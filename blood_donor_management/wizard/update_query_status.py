
from odoo import models, api, fields

class Update_query_status(models.TransientModel):
    _name = 'update.query.status'
    _description = 'Update the status of query i.e; whether admin has read it or not'
    # course_id = fields.Many2one('course.details',string='Course')
    # student_id=fields.Many2many('res.partner',string='Student',domain="[('course_id','=',course_id)]")
    query_status=fields.Boolean(string='User Query status')

    @api.multi
    def update_query_status(self):
        active_ids = self.env.context['active_ids']
        lines = self.env['res.partner'].search([('id', 'in', active_ids)])
        for line in lines:            
            if line.query_status==False:
                line.write({'query_status':True})
            elif line.query_status==True:
                line.write({'query_status':False})
            else:
                pass