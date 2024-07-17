from rest_framework import serializers
from .models import Car, Maintenance, Complaint
from .models import UserProfile

class CarSerializer(serializers.ModelSerializer):
    technic_name = serializers.CharField(source='technic.name', read_only=True)
    engine_name = serializers.CharField(source='engine.name', read_only=True)
    transmission_name = serializers.CharField(source='transmission.name', read_only=True)
    driving_bridge_name = serializers.CharField(source='driving_bridge.name', read_only=True)
    controlled_bridge_name = serializers.CharField(source='controlled_bridge.name', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'car_number', 'technic', 'technic_name', 'engine', 'engine_name',
            'engine_number', 'transmission', 'transmission_name', 'transmission_number',
            'driving_bridge', 'driving_bridge_name', 'driving_bridge_number',
            'controlled_bridge', 'controlled_bridge_name', 'controlled_bridge_number',
            'date_shipment', 'consignee', 'delivery_address', 'equipment', 'client', 'service_company'
        ]

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'username_display', 'car', 'status')