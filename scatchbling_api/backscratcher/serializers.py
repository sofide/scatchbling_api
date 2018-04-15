from rest_framework import serializers

from backscratcher.models import Backscratcher


class BackscratcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Backscratcher
        fields = ('id', 'name', 'description', 'cost')
