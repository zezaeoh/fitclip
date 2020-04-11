from rest_framework import serializers

from fitclip.fit.models.fit_spec import FitSpecOption, FitSpec
from fitclip.fit.models.fit_store import FitStore


class FitSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitSpec
        fields = '__all__'


class FitSpecOptionSerializer(serializers.ModelSerializer):
    fit_spec = FitSpecSerializer(read_only=True)

    class Meta:
        model = FitSpecOption
        fields = ['fit_spec', 'is_required']


class FitStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitStore
        fields = '__all__'
