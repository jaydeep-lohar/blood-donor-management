# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
from datetime import datetime,date


class Donor_details(models.Model):
	_name="donor.details"
	_description="Donor Details"

	full_name=fields.Char(string='Name: ')
	blood_group=fields.Selection([
		('O+','O+'),
		('A+','A+'),
		('B+','B+'),
		('AB+','AB+'),
		('O-','O-'),
		('A-','A-'),
		('B-','B-'),
		('AB-','AB-')])
	previous_donation_date=fields.Date(string='Previous donation date')
	hemoglobin=fields.Char(string='Hemoglobin')
	pulse_rate=fields.Char(string='Pulse rate')
	blood_pressure=fields.Integer(string='Blood pressure')
	temperature=fields.Char(string='Temperature')
	mobile=fields.Char(string='Contact No:-')
	address=fields.Text()
	gender=fields.Selection([('1','Male'),('2','Female')])
	weight=fields.Char(string="Weight")
	diastolic=fields.Char(string='Blood Pressure(diastolic)')
	systolic=fields.Char(string='Blood Pressure(systolic)')
	status=fields.Boolean(string='Status',default=False)
	image = fields.Binary(string="Receipt from doctor with all above details to be verified at admin end")
	
	@api.onchange('hemoglobin')
	def check_hemoglobin(self):
		try:
			j=float(self.hemoglobin)
			if (self.hemoglobin and (j <= 12.5)):
				raise UserError("Error: The quantity of hemoglobin should be > 12.5")
		except ValueError:
			raise UserError("Error: Input a float Value")


	@api.onchange('weight')
	def check_weight(self):
		try:
			j=float(self.weight)
			if j and self.gender=='1' and j < 45:
				raise UserError("Error: The weight for male should be >= 45kg ")
			elif j and self.gender=='2' and j < 50:
				raise UserError("Error: The weight for female should be >= 50kg ")
		except ValueError:
			raise UserError("Error: Input a float Value")


	
	def date_calc(self,strt):
		l=strt.split("-")
		return date(int(l[0]),int(l[1]),int(l[2]))

	@api.onchange('previous_donation_date')
	def check_previous_donation_date(self):
		if self.previous_donation_date :
			n=date.today()
			cur=self.date_calc(str(n))
			pre=self.date_calc(str(self.previous_donation_date))
			diff=cur-pre
			if self.previous_donation_date and diff.days <= 54 :
				raise UserError("Error: There should be a gap of 54 days between your previous donation\n Sorry ur not eligible to donate blood")

	@api.onchange('pulse_rate')
	def check_pulse_rate(self):
		try:
			j=int(self.pulse_rate)
			if j and j <=60 or j >=100:
				raise UserError("Error: The quantity of blood pressure should be 60 < x < 100")
		except ValueError:
			raise UserError("Error: Input a integer Value")


	@api.onchange('temperature')
	def check_temperature(self):
		try:
			j=float(self.temperature)
			if ( j and j <= 37.5):
				raise UserError("Error: The body temperature should be <= 37.5 Celsius")
		except ValueError:
			raise UserError("Error: Input a float Value")

	@api.onchange('systolic')
	def check_systolic(self):
		try:
			j=int(self.systolic)
			if ( j and j <= 180):
				raise UserError("Error: The blood_group(systolic) should be <= 180 ")
		except ValueError:
			raise UserError("Error: Input a int  Value")


	@api.onchange('diastolic')
	def check_diastolic(self):
		try:
			j=int(self.diastolic)
			if ( j and j <= 100):
				raise UserError("Error: The blood_group(diastolic) should be <= 100")
		except ValueError:
			raise UserError("Error: Input a int Value")



