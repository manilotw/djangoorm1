from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404  
from django.utils.timezone import localtime


def get_duration(enter_time,
                 now_time):
        spend_time = now_time - enter_time
        return spend_time

  

def format_duration(spend_time):
        seconds = spend_time.total_seconds
        hour = seconds // 3600
        remaind = seconds % 3600
        minute = remaind // 60
        seconds = remaind % 60

        return f"{int(hour):02}:{int(minute):02}:{int(seconds):02}"
    

def is_visit_long(visit, minutes=60):
    enter_time = localtime(visit.entered_at)
    exit_time = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    spend_time = exit_time - enter_time
    seconds = spend_time.total_seconds()
    minutes_spent = seconds / 60
    return minutes_spent > minutes


