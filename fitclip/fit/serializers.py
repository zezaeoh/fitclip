from rest_framework import serializers

from fitclip.fit.models.fit_spec import FitSpecOption, FitSpec
from fitclip.fit.models.personal_fit import PersonalFitUIOption, PersonalFit
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


class PersonalFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalFit
        fields = '__all__'


class PersonalFitUIOptionSerializer(serializers.ModelSerializer):
    personal_fit = PersonalFitSerializer(read_only=True)

    class Meta:
        model = PersonalFitUIOption
        fields = ['personal_fit', 'group', 'desc', 'personal_fit_ui_type']

