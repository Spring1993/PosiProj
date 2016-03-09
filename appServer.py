from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site,NOT_DONE_YET
import time

class BusyPage(Resource):
	isLeaf = True 

	def render_POST(self,request):
		req = eval(request.content.read())
		print req
		return NOT_DONE_YET

root = BusyPage()
factory = Site(root) 
reactor.listenTCP(8000,factory)
reactor.run()
