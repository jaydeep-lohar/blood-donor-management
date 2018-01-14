# -*- coding: utf-8 -*-
{
	'name': 'Blood-donor & blood-bank management',
	'version': '1',
	'summary': 'Manage blood donor & blood bank related information',
	'description': """This is description for blood donor & blood bank management system""",
	# 'depends': ['base'],
	'data': [
	'views/home_registration.xml',
	'views/admin_view.xml',
	'wizard/update_donor_status.xml',
	'wizard/update_query_status.xml'
	],
	'demo': [ ],
	'qweb': [ ],
	'installable': True,
	'auto_install': False,

}