from odoo import api, fields, models
# from datetime import datetime 

class Camp_registration_details(models.Model):
	_name = "camp.registration.details"
	_description = "Camp Registraion Details"


	district_id=fields.Many2one('district',string="District ",required=True)
	blood_bank_id=fields.Many2one('blood_bank',string="Blood bank  ",required=True)
	organization_id=fields.Many2one('organization',string="Organization  ",required=True)
	camp_name=fields.Char(string='Camp name ',required=True)
	camp_venue=fields.Char(string='Venue ',required=True)
	camp_date=fields.Date(string='Date  ',required=True)
	time=fields.Char(string='Time ',required=True)
	person_name=fields.Char(string='Person Name  ',required=True)
	contact_no=fields.Char(string='Contact No  ',required=True)
	email_Id=fields.Char(string='Email-Id ',required=True)
	message=fields.Char(string='Message  ',required=True)

	# blood_group = fields.Selection(
	# 	[
	# 		('O+', 'O+'), 
	# 		('A+', 'A+'), 
	# 		('B+', 'B+'),
	# 		('AB+', 'AB+'),
	# 		('O-', 'O-'),
	# 		('A-', 'A-'),
	# 		('B-', 'B-'),
	# 		('AB-', 'AB-'),
	# 	])
	# address = fields.Char(string='Address: ', required=True)
	# contact_no = fields.Text(string='Contact No: ')
	# email_id= fields.Char(string='Email-Id: ')
	# gender=fields.Char(string='Gender: ')
	# # category = fields.Selection(