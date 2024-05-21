from collections import defaultdict
from django.db.models.functions import TruncMonth
from apps.home.models import Alert
from django.db.models import Count



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
    return list(alerts_by_month)


def get_alerts_count_per_month():
    # Query alerts, annotate each with the month, and count them
    alerts = Alert.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id_a')).order_by(
        'month')

    # Create a list of counts per month
    counts_per_month = [alert['count'] for alert in alerts]
    print(counts_per_month)
    return counts_per_month


# Usage example
counts_per_month = get_alerts_count_per_month()



