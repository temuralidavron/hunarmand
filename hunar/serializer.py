from rest_framework import serializers
from .models import Anketa, User, MarkAnketa


class AnketaSerializer(serializers.ModelSerializer):
    anketa = serializers.SerializerMethodField()

    def get_anketa(self, obj):
        anketa = MarkAnketa.objects.filter(anketa=obj)
        return MarkAnketaSerializer(anketa, many=True).data

    class Meta:
        model = Anketa
        fields = (
            'id',
            'photo',
            'name',
            'fname',
            'lname',
            'koyadress',
            'state',
            'password',
            'passwordpnfl',
            'malumot',
            'adress',
            'workadress',
            'number',
            'email',
            'web_chart',
            'studentcount',
            'job',
            'grift',
            'memberyear',
            'award',
            'festival',
            'nationalfest',
            'owngalery',
            'teacherabout',
            'orginalwork',
            'modepraduct',
            'addinform',
            'photos',
            'anketa')









class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class MarkAnketaSerializer(serializers.ModelSerializer):
    class Meta:
        model =MarkAnketa
        fields = '__all__'



