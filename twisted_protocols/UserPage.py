from json import dumps,loads
from smtplib
from email.mime.text import MIMEText

from twisted.python import log
from twisted.internet import reactor,defer
from twisted.web.resource import Resource
from twisted.web.server import Site,NOT_DOWN_YET


class UserPage(Resource):
	isLeaf = True
	def render_POST(self,request):


userPage = UserPage()
