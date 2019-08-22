import unittest
from unittest.mock import patch, Mock

from qrcodepkg.qrcode import qrcode
from qrrelation.relation import relation

class qrtest(unittest.TestCase):
	def setUp(self):
		self.tmp=qrcode()
	def test_info_qrcode(self):
		self.assertEqual(self.tmp.info(),"Swagger")
	def test_create_qrcode_isnotnone(self):
		self.assertIn(b'PNG', self.tmp.createQR("test"))
	def test_create_qrcode_isnone(self):
		with self.assertRaises(TypeError):
			self.tmp.createQR()
	def test_create_qrcode_scale(self):
		self.assertIn(b'PNG', self.tmp.createQR("test",6))
	def test_create_qrcode_scale_high(self):
		self.assertIn(b'PNG', self.tmp.createQR("test",100))
	def test_create_qrcode_special_char(self):
		self.assertIn(b'PNG', self.tmp.createQR("*/?%$#@",6))
	def test_create_qrcode_null_str(self):
		self.assertIn(b'PNG', self.tmp.createQR(''))
	def test_create_qrcode_empty_Str(self):
		self.assertIn(b'PNG', self.tmp.createQR(' '))
	def test_create_qrcode_empty_special_char(self):
		self.assertIn(b'PNG', self.tmp.createQR(' _*&^%$$#@!~ '))

class qrrelationtest(unittest.TestCase):
	@patch('qrrelation.relation.relation.relationdf',return_value='5678')
	def setUp(self,relationdf_mock):
		self.tmp=relation()
		#relationdf_mock.return_value='5678'
	@patch('qrrelation.relation.relation.relationdf',return_value='5678')
	def test_getrelation(self,relationdf_mock):
		self.assertIsNotNone(self.tmp.getRelation("tmp"))
	@patch('qrrelation.relation.relation.relationdf',return_value='5678')
	def test_getRelation_data(self,relationdf_mock):
		self.assertEqual("5678",self.tmp.getRelation("Sample"))
	def test_getRelation_df(self):
		self.assertEqual("1234",self.tmp.relationdf("Sample"))

if __name__=="__main__":
	unittest.main()