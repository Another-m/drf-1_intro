from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

# class SensorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

from measurement.models import Sensor, MeasurementTemp


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasurementTemp
        fields = '__all__'
        # read_only_fields = ("name_sensor", "id")


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)


    class Meta:

        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

