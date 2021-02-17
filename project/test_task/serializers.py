from rest_framework import serializers
from datetime import datetime


class YearSerializer(serializers.Serializer):
    year = serializers.IntegerField(default=None)
    checkbox = serializers.NullBooleanField(default=None)

    def validate_year(self, year):
        if not year:
            raise serializers.ValidationError("год не введен")
        if year == 2018:
            raise serializers.ValidationError("год не должен быть равен 2018")
        return year

    def validate(self, attrs):
        year = attrs.get('year')
        check = attrs.get('checkbox')
        current_year = datetime.now().year
        if year > current_year and not check:
            raise serializers.ValidationError(
                {"common": ["введенный год не больше текущего", ]})
        return attrs
