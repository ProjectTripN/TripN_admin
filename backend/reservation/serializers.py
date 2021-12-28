from rest_framework import serializers
from .models import Reservation as reservation


class ReservationSerializer(serializers.Serializer):
    reg_date = serializers.DateField()
    people = serializers.IntegerField()
    day = serializers.IntegerField()
    plane_unit = serializers.IntegerField()
    plane_price = serializers.IntegerField()
    acc_unit = serializers.IntegerField()
    acc_price = serializers.IntegerField()
    act_unit = serializers.IntegerField()
    price = serializers.IntegerField()
    tax = serializers.IntegerField()
    subtotal = serializers.IntegerField()
    fees = serializers.IntegerField()
    total_price = serializers.IntegerField()
    jeju_schedule = serializers.IntegerField()
    user = serializers.IntegerField()

    class Meta:
        model = reservation
        fileds = '__all__'

    def create(self, valideted_data):
        return reservation.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        reservation.objects.filter(pk=instance.username).update(**valideted_data)
