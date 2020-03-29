from rest_framework import serializers

from fitclip.fit.models.fit_spec import FitSpecOption
from fitclip.fit.serializers import FitSpecOptionSerializer
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

    class Meta:
        model = Sub
        fields = '__all__'

    def get_fit_specs(self, obj):
        qset = FitSpecOption.objects.filter(sub=obj)
        return [FitSpecOptionSerializer(m).data for m in qset]
