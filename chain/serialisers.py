from rest_framework import serializers
from . import models


class CattleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cattle
        fields = '__all__'
        read_only_fields = ['date_added']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organisation
        fields = '__all__'
        read_only_fields = ['registration_date']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        read_only_fields = ['date_added']
        
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'
        read_only_fields = ['date_added']
        

class CattleProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cattle_process
        fields = '__all__'
        read_only_fields = ['date_added']
        
        
class ProductProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cattle_process
        fields = '__all__'
        read_only_fields = ['date_added']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = "__all__"
        read_only_fields = ['date_added']
        

class ProcessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Process_type
        fields = "__all__"
        read_only_fields = ['date_added']


class TransportionModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transportation_mode
        fields = "__all__"
        read_only_fields = ['date_added']


class OrganizationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organisation_type
        fields = "__all__"
        read_only_fields = ['date_added']
