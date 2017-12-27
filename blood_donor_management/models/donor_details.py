# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Donor_details(models.Model):
	_name = "donor.details"
	_description = "Donor Details"
	_inherit="res.partner"

	usertype=fields.Selection([('admin','admin'),('client','client')],required=True)
	name = fields.Char(string='Name: ',required=True)
	date_of_birth = fields.Date(string='Date of birth: ',required=True)

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
		],required=True)
	address = fields.Char(string='Address: ', required=True)
	contact_no = fields.Text(string='Contact No: ',required=True)
	email_id= fields.Char(string='Email-Id: ')
	gender=fields.Selection(
		[('1','Male'),('0','Female')],required=True)
	# category = fields.Selection(
	# 	[
	# 		('novel','Novel'),
	# 		('comic','Comic'),
	# 		('drama','Drama'),
	# 		('ebook','E-Book'),
	# 		('magzin','Magzin'),
	# 		('technical','Technical'),
	# 		('management','Management'),
	# 		('social','Social'),
	# 		('other','Other')

	# 	])
	# author = fields.Selection(
	# 	[
	# 		('author1','Author1'),
	# 		('author2','Author2'),
	# 		('author3','Author3'),
	# 		('author4','Author4'),
	# 		('author5','Author4'),
	# 		('author6','Author6'),
	# 		('other','Other')

	# 	])
	# publisher = fields.Selection(
	# 	[
	# 		('publisher1','Publisher1'),
	# 		('publisher2','Publisher2'),
	# 		('publisher3','Publisher3'),
	# 		('publisher4','Publisher4'),
	# 		('publisher5','Publisher5'),
	# 		('publisher6','Publisher6'),
	# 		('publisher7','Publisher7'),
	# 		('other','Other')
	# 	])
	# price = fields.Float(string="Price: ")
	# copies = fields.Integer(string="Copies: ")
	# # cover_image = fields.
	# date = fields.Date(string="Date")













	# ./odoo-bin -d asd --db-filter=asd --addons-path=addons,../library-management -u library_management
