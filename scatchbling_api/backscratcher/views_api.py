from backscratcher.models import Backscratcher
from backscratcher.serializers import BackscratcherSerializer
from rest_framework import generics, mixins


class BackscratcherList(generics.ListCreateAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer


class BackscratcherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer
