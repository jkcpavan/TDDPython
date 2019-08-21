import unittest

from qrcodepkg.qrcode import qrcode

class qrintegrationtest(unittest.TestCase):
	def setUp(self):
		self.tmp=qrcode()
	def test_info_qrcode(self):
		self.assertEqual(self.tmp.info(),"Swagger")
        
if __name__=="__main__":
	unittest.main()