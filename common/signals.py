import django.dispatch


order_cleared = django.dispatch.Signal()

consultation_start = django.dispatch.Signal()
consultation_end = django.dispatch.Signal()