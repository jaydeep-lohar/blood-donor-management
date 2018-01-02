from odoo import api, fields, models

class District(models.Model):
	_name = "district"
	_description = "District Details"
	
	name = fields.Char(string='District Name: ')





class Blood_Bank(models.Model):
	_name = "blood_bank"
	_description = "Blood Bank Details"
	
	name = fields.Char(string='Blood Bank Name: ')
	district_id = fields.Many2one('district',string='District Name ' )




class Organization(models.Model):
	_name = "organization"
	_description = "Organization Details"

	
	name = fields.Char(string='Organization Name: ')
	district_id = fields.Many2one('district',string='District Name ' )