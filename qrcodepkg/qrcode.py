import pyqrcode
import base64
class qrcode(object):
    def info(self):
        return "Swagger"
    def createQR(self,msg,scale=6):
            url= pyqrcode.create(msg)
            return base64.b64decode(url.png_as_base64_str(scale))