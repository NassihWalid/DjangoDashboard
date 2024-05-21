from collections import defaultdict
from django.db.models.functions import TruncMonth
from apps.home.models import Alert


def get_alerts_grouped_by_month():
    # Query alerts and annotate each with the month
    alerts = Alert.objects.annotate(month=TruncMonth('date')).order_by('month')

    # Group alerts by month
    alerts_by_month = defaultdict(list)
    for alert in alerts:
        month = alert.date.strftime('%Y-%m')  # Format: YYYY-MM
        alerts_by_month[month].append({
            'id': alert.id_a,
            'voyage_id': alert.voyage.id_vo,
            'date': alert.date,
            'driver': alert.voyage.driver.name,
            'vehicle': alert.voyage.vehicle.model,
            'road': alert.voyage.road.name
        })

    # Convert defaultdict to a regular dict before returning
    return dict(alerts_by_month)



