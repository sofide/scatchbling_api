from backscratcher.models import Backscratcher
from backscratcher.serializers import BackscratcherSerializer
from rest_framework import generics, mixins


class BackscratcherList(generics.ListCreateAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer


class BackscratcherDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        generics.GenericAPIView):
    queryset = Backscratcher.objects.all()
    serializer_class = BackscratcherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
