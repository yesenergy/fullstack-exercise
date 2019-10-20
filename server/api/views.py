from django.http import HttpResponse
from django.http import JsonResponse

from collections import namedtuple
from django.db import connection
import pandas as pd
import json

def summary(request):
	result = fetchSummary()
	df = pd.DataFrame(result)
	grouped  = df.groupby(['tradetype', 'peaktype', 'auctiontype', 'hedgetype'])
	grouped = grouped.sum()
	return JsonResponse(json.loads(grouped.to_json(orient="table"))["data"], safe=False)

def fetchSummary():
	with connection.cursor() as cursor:
		cursor.execute("select tradetype, peaktype, auctiontype, hedgetype, profit from trans, price_nodes as source\
		where source.nodetype = 'HUB'\
		and trans.sourceid = source.nodeid ")
		result = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
		return result

def fetchTransactions():
	"""
	Fetch the FTR transactions from the database.  Executes the SQL and then unpacks it into a Dict
	"""
	with connection.cursor() as cursor:
		cursor.execute("select iso, participants.ftrparticipant, participantshortname, tradetype,\
		peaktype, auctiontype, hedgetype,  sourceid, sinkid, counterflow, contractsize, \
		cost, revenue, profit, hours, hrs_in_period,\
		sink.nodename as sinkname, source.nodename as sourcename\
		from trans, price_nodes as source, price_nodes as sink, participants\
		where trans.ftrparticipant = participants.ftrparticipant \
		and trans.sinkid = sink.nodeid \
		and source.nodetype = 'HUB'")
		result = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
		return result

def transactions(request):
	"""
	This is the /api/transactions endpoint, it calls the DB fetch
	and returns a JsonResponse with the results
	"""
	result = fetchTransactions()
	return JsonResponse(result, safe=False)
