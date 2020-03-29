from rest_framework import serializers

from fitclip.fit.models.fit_spec import FitSpecOption, FitSpec


class FitSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitSpec
        fields = '__all__'


class FitSpecOptionSerializer(serializers.ModelSerializer):
    fit_spec = FitSpecSerializer(read_only=True)

    class Meta:
        model = FitSpecOption
        fields = ['fit_spec', 'is_required']
