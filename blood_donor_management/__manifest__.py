# -*- coding: utf-8 -*-
{
	'name': 'Blood-donor & blood-bank management',
	'version': '1',
	'summary': 'Manage blood donor & blood bank related information',
	'description': """This is description for blood donor & blood bank management system""",
	'depends': ['base','mail'],
	'data': [
	'security/access_security.xml',
	'views/home_registration.xml',
	'views/admin_view.xml',
	'views/welcome_template.xml',
	'wizard/update_donor_status.xml',
	'wizard/update_query_status.xml',
	# 'wizard/report_camp_detail.xml',
	'report/report_menu.xml',
	'report/report_donor_detail.xml',
	# 'report/wizard_report_camp_detail.xml'
	'security/ir.model.access.csv'
	],
	'demo': [
	'demo/demo_become_a_donor.xml',
	'demo/demo_add_blood_bank.xml',
	'demo/demo_camp_registration.xml',
	'demo/demo_user_query.xml'
	 ],
	'qweb': [ ],
	'installable': True,
	'auto_install': False,

}