# -*- coding: utf-8 -*-
{
    'name' : 'Blood-donor & group Management',
    'version' : '1',
    'summary': 'Manage blood donor & blood group related information',
    'description': """
This is description for blood donor & group management system.
    """,
    'depends':['sale_management'],
    'data': [
        'views/admin.xml',
        'views/camp_registration.xml',
        'views/donor_details_view.xml',
        'views/make_a_query.xml',
        'views/search_donor.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}
