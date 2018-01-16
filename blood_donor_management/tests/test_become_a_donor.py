from .common import Common

class Test_become_a_donor(Common):

	def test_01(self):
		print("Hello............................")
		self.assertIsNotNone(self.become_a_donor.role,'Role cannot be null')
		# self.assertIsNotNone(self.assignment_1.subject_id,'assignment have no subject')
		# self.assertIsNotNone(self.assignment_1.faculty_id,'No one have assign assignment')
		print("Hello")