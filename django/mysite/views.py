from django.http import HttpResponse
import datetime

def echo(request):
    now = datetime.datetime.now()
    html = "<html><body>The time is now %s.</body></html>" % now
    return HttpResponse(html)