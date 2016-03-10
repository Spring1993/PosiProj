from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site,NOT_DONE_YET

'''
class Page(Resource):
	isLeaf = True 

	def render_POST(self,request):
		req = eval(request.content.read())
		print req
		return NOT_DONE_YET
'''
from twisted_protocols.GpsPage import gpsPage
from twisted_protocols.UserPage
mainPage = Reource()
apiPage = Resource()
mainPage.putChild('api',apiPage)
apiPage.putChild('gps',gpsPage)
apiPage.putChild('user',userPage)
factory = Site(mainPage) 
reactor.listenTCP(8000,factory)
reactor.run()
