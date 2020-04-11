from rest_framework import serializers

from fitclip.fit.models.fit_spec import FitSpecOption
from fitclip.fit.models.personal_fit import PersonalFitUIOption
from fitclip.fit.serializers import FitSpecOptionSerializer, PersonalFitUIOptionSerializer
from fitclip.mall.models.category import Category, Section, Sub


class CategorySerializer(serializers.ModelSerializer):
    sections = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='section-detail'
    )

    class Meta:
        model = Category
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    subs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='sub-detail'
    )

    class Meta:
        model = Section
        fields = '__all__'


class SubSerializer(serializers.ModelSerializer):
    fit_specs = serializers.SerializerMethodField()
    personal_fits = serializers.SerializerMethodField()

    class Meta:
        model = Sub
        fields = '__all__'

    def get_fit_specs(self, obj):
        qset = FitSpecOption.objects.filter(sub=obj)
        return FitSpecOptionSerializer(qset, many=True).data

    def get_personal_fits(self, obj):
        qset = PersonalFitUIOption.objects.filter(sub=obj)
        return PersonalFitUIOptionSerializer(qset, many=True).data
