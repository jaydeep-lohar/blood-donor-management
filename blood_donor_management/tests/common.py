from odoo.tests.common import TransactionCase

class Common(TransactionCase):
    def setUp(self):
        super(Common,self).setUp() 

         # for become a donor
        self.become_a_donor = self.env['res.partner'].create({

            'role': "1",
            'name': 'Dhwani Mehta',
            'blood_group': 'O+',
            'previous_donation_date': '2017-9-28',
            'hemoglobin': '17',
            'pulse_rate': '90',
            'temperature': '30',
            'gender': '2',
            'weight': '65',
            'diastolic': '85',
            'systolic': '170',
            'donor_status': 'True',
            'street': 'Home no:-206',
            'street2': 'New C.G Road',
            'city': 'Ahmedabad'
            })


        # for add blood bank
        self.add_blood_bank = self.env['res.partner'].create({

            'role': '2',
            'type1': 'independent',
            'name': 'Sai Seva',
            'contact_person': 'Prashant Yadav',
            'phone': ' 123456789',
            'mobile': '90',
            'email': 'Sai_Seva@gmail.com',
            'street': 'Opp Sports Complex',
            'street2': 'new C.G. Road',
            'website': 'www.Sai-Seva.com',
            'city': 'Ahmedabad'
            })

        # for camp registration
        self.camp_registration = self.env['res.partner'].create({


            'role': '3',
            'name': 'Om mandal seva',
            'blood_bank_ref':self.add_blood_bank,
            'camp_date': '2018-02-10',
            'camp_time': '11.50',
            'person_name': 'Vidit Singh',
            'mobile': '9054495887',
            'email': 'om_mandal_seva@gmail.com',
            'street': 'Opp Nike Showroom',
            'street2': 'Government streets',
            'city': 'Gandhinagar',
            'message': 'Hello'
            })  


        # for user query
        self.user_query = self.env['res.partner'].create({

            'role': '4',
            'query_status': 'True',
            'name': 'Nikhil',
            'message': 'Hello',
            'mobile': '9054495887',
            'email': 'nikhil@gmail.com'
            })

    