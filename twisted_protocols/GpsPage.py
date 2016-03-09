from json import dumps

from twisted.web.resource import Resource
from twisted.web.server import Site,NOT_DONE_YET
from twisted.python import log, failure
from twsited.internet import defer,reactor

class GpsPage(Resource):
	isLeaf = True

	
