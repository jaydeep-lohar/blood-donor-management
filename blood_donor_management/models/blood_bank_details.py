from odoo import api, fields, models
from datetime import datetime 

class Blood_bank_detais(models.Model):
	_name = "blood.bank.details"
	_description = "Blood bank details"


	type1=fields.Selection([('independent','Independent'),('government','Government'),('hospital','Hospital')])
	name=fields.Char(string='Name ')
	contact_person=fields.Char(string='Contact person ')
	contact_no=fields.Char(string='Contact No  ')
	email_id=fields.Char(string='Email-Id ')
	address=fields.Char(string='Address')
	state=fields.Char(string='State')
	city=fields.Char(string='City')