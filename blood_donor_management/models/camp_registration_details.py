from odoo import api, fields, models
from datetime import datetime 

class Camp_registration_details(models.Model):
	_name = "camp.registration.details"
	_description = "Camp Registraion Details"


	blood_bank_id=fields.Many2one('blood_bank',string="Blood bank  ")
	camp_name=fields.Char(string='Camp name ')
	camp_venue=fields.Char(string='Venue ')
	camp_date=fields.Date(string='Date  ')
	time=fields.Char(string='Time ')
	person_name=fields.Char(string='Person Name  ')
	contact_no=fields.Char(string='Contact No  ')
	email_Id=fields.Char(string='Email-Id ')
	message=fields.Char(string='Message  ')