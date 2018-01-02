# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Donor_details(models.Model):
	_name = "donor.details"
	_description = "Donor Details"
	

	#usertype=fields.Selection([('admin','admin'),('client','client')],required=True)
	full_name = fields.Char(string='Name: ',required=True)
	date_of_birth = fields.Date(string='Date of birth: ',required=True)

	blood_group_id = fields.Many2one('blood.group.details',string="Blood Group")
	address = fields.Char(string='Address: ', required=True)
	city=fields.Char(string='City:')
	mobile = fields.Text(string='Contact No: ',required=True)
	email_id= fields.Char(string='Email-Id: ')
	gender=fields.Selection([('1','Male'),('0','Female')])
	date_of_birth=fields.Date(string='Date of birth: ')
	message=fields.Char(string='Message  ',required=True)
	