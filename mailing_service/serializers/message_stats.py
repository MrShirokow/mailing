from collections import defaultdict
from django.db.models import QuerySet


def get_stats_dict(queryset: QuerySet) -> defaultdict:
    message_stats_by_notification = defaultdict(lambda: defaultdict(int))
    for notification_id, is_sending, count, text in queryset:
        message_stats_by_notification[notification_id][is_sending] += count
        message_stats_by_notification[notification_id]['text'] = text

    return message_stats_by_notification


def serialize_stats(stats_dict: defaultdict) -> list:
    return [
        {
            'notification': notification_id,
            'text': message_state['text'],
            'messages': [
                {'is_sending': state,
                 'count': message_state[state]} for state in (True, False)
            ]
        }
        for notification_id, message_state in stats_dict.items()
    ]
