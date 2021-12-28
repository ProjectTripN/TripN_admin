import datetime
import pandas as pd
from django.db.models import Count, Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from reservation.models import Reservation
from reservation.models_process import Processing
from reservation.serializers import ReservationSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def preprocess(request):
    Processing().pre_process()
    return Response({'preprocess': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request, pk):
    Processing().process(pk)
    return JsonResponse({'process': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_data(request):
    Processing().insert_data()
    return Response({'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def profit_month(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    plane_sum = Reservation.objects.filter(date__year=2021, date__month=12).aggregate(Sum('plane_pr'))
    acc_sum = Reservation.objects.filter(date__year=2021, date__month=12).aggregate(Sum('acc_pr'))
    act_sum = Reservation.objects.filter(date__year=2021, date__month=12).aggregate(Sum('act_pr'))
    sum_data = pd.DataFrame(plane_sum, acc_sum, act_sum)
    return JsonResponse(data=sum_data, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def count_res(request):
    count_data = Processing().count()
    # print(count_data)
    # df_c = pd.DataFrame(count_data, columns=['a', 'b'])
    # df_b = df_c.T
    # df_a = df_b.values.tolist()
    # df_r = df_a[0]
    # df_r.reverse()
    # df_rr = df_a[1]
    # df_rr.reverse()
    # df = [df_r, df_rr]
    # print(df)
    return JsonResponse(data=count_data, safe=False)
