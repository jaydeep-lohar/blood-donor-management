# import re
from odoo import api, fields, models,_
# from odoo.exceptions import UserError,ValidationError

class User_query(models.Model):
	_name = "user.query"
	_description = "Make a Query to the admin"

	
	name = fields.Char(string=' Name: ')
	contact_no = fields.Char(string='Contact No: ')
	email_id = fields.Char(string='Email-Id: ')
	message = fields.Text(string='Message: ')
	status=fields.Boolean(string='Status')



	# @api.constrains('contact_no')
	# def check_phone_no(self):
	# 	if not re.match("[0-9]{7,10}",self.contact_no):
	# 		raise ValidationError(_('Mobile number must be 10 digits!!!'))
