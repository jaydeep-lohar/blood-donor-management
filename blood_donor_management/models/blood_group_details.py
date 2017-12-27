from odoo import api, fields, models

class blood_group_details(models.Model):
	_name = "blood.group.details"
	_description = "Blood Group Details"

	name = fields.Char(string='Name: ')
	date_of_birth = fields.Integer(string='Date of birth: ')

	blood_group = fields.Selection(
		[
			('O+', 'O+'), 
			('A+', 'A+'), 
			('B+', 'B+'),
			('AB+', 'AB+'),
			('O-', 'O-'),
			('A-', 'A-'),
			('B-', 'B-'),
			('AB-', 'AB-'),
		])
	address = fields.Char(string='Address: ', required=True)
	contact_no = fields.Text(string='Contact No: ')
	email_id= fields.Char(string='Email-Id: ')
	gender=fields.Char(string='Gender: ')
	# category = fields.Selection(