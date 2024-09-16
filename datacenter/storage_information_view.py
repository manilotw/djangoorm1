from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.time_functions import format_duration, get_duration





def storage_information_view(request):
    

    visit_names = []
    in_storage = Visit.objects.filter(leaved_at__isnull=True)

    for visit in in_storage:
            
        in_storage_info ={ 
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': get_duration(visit.entered_at),}

        visit_names.append(in_storage_info)


  
    context = {
        'non_closed_visits': visit_names,  
    }
    return render(request, 'storage_information.html', context)
