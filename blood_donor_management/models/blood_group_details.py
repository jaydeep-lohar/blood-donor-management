from odoo import api, fields, models

class Blood_group_details(models.Model):
	_name = "blood.group.details"
	_description = "Blood Group Details"

	name = fields.Selection(
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
