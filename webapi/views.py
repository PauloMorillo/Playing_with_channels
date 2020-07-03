from django.shortcuts import render
#from django.shortcuts import render_to_response
from rest_framework import generics, viewsets
from webapi.models import User, Help, Store
from webapi.serializers import UserSerializer, HelpSerializer, StoreSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import permissions
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)

class LiveConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)

# Create your views here.
#def principal(request):
#    return render_to_response("principal.html")
#
#def index(request):
#    return render_to_response("index.html")

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class HelpList(generics.ListCreateAPIView):
    serializer_class = HelpSerializer
    queryset = Help.objects.all()

class HelpDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HelpSerializer
    queryset = Help.objects.all()

class StoreList(generics.ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

