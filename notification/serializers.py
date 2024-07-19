# serializers.py

from rest_framework import serializers
from .models import Notification, DataSystem


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


        def validate_uuid(self, value):
            """
            Revisa que el uuid de la clase DataSystem exista
            """
            valida_uuid = DataSystem.objects.filter(uuid = uuid)

            print(valida_uuid)

            if valida_uuid == Notification.uuid:
                return valida_uuid




