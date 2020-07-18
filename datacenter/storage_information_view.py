from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

import datetime


def storage_information_view(request):
    active_visites = Visit.objects.filter(leaved_at=None).select_related('passcard')

    non_closed_visits = [{
            "who_entered": visit.passcard.owner_name,
            "entered_at": localtime(visit.entered_at),
            "duration": visit.format_duration(),
            "is_strange": visit.is_visit_long()
        } for visit in active_visites]

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

