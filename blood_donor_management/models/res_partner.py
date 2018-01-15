# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
from odoo.addons.base.res import res_partner
from datetime import datetime,date


class ResPartner(models.Model):
	_inherit = 'res.partner'
	_description="Home_Registration"

	role=fields.Selection([('1','Become a donor'),('2','Add blood bank'),('3','Camp Registration'),('4','Donor Query')],default='1')

	############-----------------------------------------------Donor-details & validation
	############full_name=name // field_name in res.partner
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
	############taken integer amount of hemoglobin as char because while taking int the default values where replacing the place holder.....Same in all below fields 
	pulse_rate=fields.Char(string='Pulse rate')
	temperature=fields.Char(string='Temperature')
	############mobile=fields.Char(string='Contact No:-')
	############address=fields.Text()
	gender=fields.Selection([('Male','Male'),('Female','Female')])
	weight=fields.Char(string="Weight")
	diastolic=fields.Char(string='Blood Pressure(diastolic)')
	systolic=fields.Char(string='Blood Pressure(systolic)')
	donor_status=fields.Boolean(string='Donor status',default=False)
	#profile_pic=fields.Binary(string='Profile Image:-')
	image = fields.Binary(string="Receipt from doctor with all above details to be verified at admin end")

	#############Onchange Validation
	@api.onchange('hemoglobin')
	def check_hemoglobin(self):
		try:
			j=float(self.hemoglobin)
			if (self.hemoglobin and (j < 12.5)):
				raise UserError("Error: The quantity of hemoglobin should be >= 12.5")
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
			if j and j < 60 or j > 100:
				raise UserError("Error: The quantity of blood pressure should be 60 <= x <= 100")
		except ValueError:
			raise UserError("Error: Input a integer Value")


	@api.onchange('temperature')
	def check_temperature(self):
		try:
			j=float(self.temperature)
			if ( j and j > 37.5):
				raise UserError("Error: The body temperature should be <= 37.5 Celsius")
		except ValueError:
			raise UserError("Error: Input a float Value")

	@api.onchange('systolic')
	def check_systolic(self):
		try:
			j=int(self.systolic)
			if ( j and j > 180):
				raise UserError("Error: The blood_group(systolic) should be <= 180 ")
		except ValueError:
			raise UserError("Error: Input a int  Value")


	@api.onchange('diastolic')
	def check_diastolic(self):
		try:
			j=int(self.diastolic)
			if ( j and j > 100):
				raise UserError("Error: The blood_group(diastolic) should be <= 100")
		except ValueError:
			raise UserError("Error: Input a int Value")

	
	############-----------------------------------Blood-bank registration & validation
	type1=fields.Selection([('independent','Independent'),('government','Government'),('hospital','Hospital')])
	############name
	contact_person=fields.Char(string='Contact person ')
	############contact_no = phone //name of field in res.partner
	############mobile
	############email
	############state_id
	############city


	############--------------------------------------Camp-registration details & validation

	blood_bank_ref=fields.Many2one('res.partner',string='Blood bank reference',domain=[('role','=','2')])
	###########camp_name=name
	############ camp_venue=Address_label
	camp_date=fields.Date(string='Date  ')
	camp_time=fields.Float(string='Time (e.g; 10:00)')
	person_name=fields.Char(string='Person Name  ')
	############mobile
	############email
	message=fields.Char(string='Message  ')


	############----------------------------------------------Donor-query & validation
	############ name
	############ contact_no = mobile//res.partner field
	############ email_id = email // res.partner field
	message = fields.Text(string='Message: ')
	query_status=fields.Boolean(string='User Query status',default=False)



	



