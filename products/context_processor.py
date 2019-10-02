from .models import Alerts


def alert_count(request):
   return { 'total_alerts' : Alerts.objects.all().count() }