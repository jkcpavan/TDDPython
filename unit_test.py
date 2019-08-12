import unittest

from qrcodepkg.qrcode import qrcode

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

if __name__=="__main__":
	unittest.main()