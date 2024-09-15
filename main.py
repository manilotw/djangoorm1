import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit
from django.utils.timezone import localtime
from datetime import timedelta



if __name__ == '__main__':
#     # Программируем здесь
#     # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
#     date=localtime()
#     print('Время сейчас: ',date)
#     enters = (Visit.objects.all()[0])
#     print(enters.entered_at)
    

#     print('Время нахождения: ',date-enters.entered_at)

    # visit_time=Visit.objects.filter(leaved_at__isnull=True)

    # for human in visit_time:
    #     enter_time = localtime(human.entered_at)
    #     now_time = localtime()
    #     spend_time = now_time - enter_time
    #     seconds = spend_time.total_seconds()
    #     hour = seconds // 3600
    #     remaind = seconds % 3600
    #     minute = remaind // 60
    #     seconds = remaind % 60

    # print('Вошел по МСК: ', enter_time)
    # # print ('Время проведенное в хранилище:', int(hour),':',int(minute),":",int(seconds))
    # # print('Время проведенное в хранилище:',spend_time)
    # print('Время проведенное в хранилище: ', f"{int(hour):02}:{int(minute):02}:{int(seconds):02}")

# active_visits = Visit.objects.filter(leaved_at__isnull=True)

# for visit in active_visits:
    
#     entered_at_local = localtime(visit.entered_at)
#     current_time = localtime()
#     time_spent = current_time - entered_at_local
#     total_seconds = int(time_spent.total_seconds())
#     hours, remainder = divmod(total_seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     # Выводим информацию
#     print("Зашёл в хранилище, время по Москве: ",entered_at_local)
#     print(f"Находится в хранилище: {hours:02}:{minutes:02}:{seconds:02}")






    
    # # all_inf=(Passcard.objects.all())
    # # print(all_inf[0])
    # active_passcard=[]

    # for active in Passcard.objects.filter(is_active=True):
        
    #     active_passcard.append(active)
    
    # print('Активных пропусков:', len(active_passcard))
    # print(Visit.objects.filter(leaved_at__isnull = True))
    # for name in Visit.objects.filter(leaved_at__isnull=True):

    #     print(name.passcard)
            
    # card= Passcard.objects.all()
    
    # humans = Visit.objects.filter(passcard=card[1])
    # print(humans)
    # print(card[1])


    
    def is_visit_long(visit,minutes):
    
    

        listspion = []

         


        for human in visit:
            if human.leaved_at:
                enter_time = localtime(human.entered_at)
                exit_time = localtime(human.leaved_at)
                spend_time = exit_time - enter_time
                seconds = spend_time.total_seconds()
                minute = seconds / 60
            
                if minutes < minute :
                    listspion.append(human)
        return listspion

