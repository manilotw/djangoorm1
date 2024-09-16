from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404  
from django.utils.timezone import localtime
from datacenter.storage_information_view import get_duration
from datacenter.time_functions import format_duration, is_visit_long




def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)  
    
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit.entered_at, visit.leaved_at)
        info = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit),
        }
        this_passcard_visits.append(info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }

    return render(request, 'passcard_info.html', context)
