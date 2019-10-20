from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json

def fetchTransactions():
	"""
	Fetch the FTR transactions from the database.  Executes the SQL and then unpacks it into a Dict
	"""
	with connection.cursor() as cursor:
		cursor.execute("select iso, participants.ftrparticipant, participantshortname, tradetype,\
		peaktype, auctiontype, hedgetype,  sourceid, sinkid, counterflow, contractsize, \
		cost, revenue, profit, hours, hrs_in_period \
		from trans \
		inner join participants on trans.ftrparticipant = participants.ftrparticipant")
		result = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor.fetchall()]
		return result

def transactions(request):
	"""
	This is the /api/transactions endpoint, it calls the DB fetch
	and returns a JsonResponse with the results
	"""
	result = fetchTransactions()
	return JsonResponse(result, safe=False)
