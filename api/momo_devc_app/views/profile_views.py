from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Profile, User
from ..serializers import ProfileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ListCreate(ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(profile, read_only=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class Update(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.queryset
        user_id = self.kwargs['user_pk']
        user = get_object_or_404(User, pk=user_id)
        obj = get_object_or_404(Profile, user=user)
        self.check_object_permissions(self.request, obj)
        return obj

