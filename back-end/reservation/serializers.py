from rest_framework import serializers
from jeju_schedule.models import JejuSchedule
from .models import Reservation as reservation


class ReservationSerializer(serializers.Serializer):
    reg_date = serializers.DateField()
    price = serializers.IntegerField()
    tax = serializers.IntegerField()
    subtotal = serializers.IntegerField()
    fees = serializers.IntegerField()
    total_price = serializers.IntegerField()
    jeju_schedule = serializers.IntegerField()

    class Meta:
        model = reservation
        fileds = '__all__'

    def create(self, valideted_data):
        return reservation.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        reservation.objects.filter(pk=instance.username).update(**valideted_data)
