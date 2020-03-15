from rest_framework import serializers

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
    class Meta:
        model = Sub
        fields = '__all__'
