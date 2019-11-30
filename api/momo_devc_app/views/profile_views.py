from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Profile
from ..serializers import ProfileSerializer


class Create(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        print(user)
        username = user.username
        password = user.password
        email = user.email
        serializer.save(user=user,
                        username=username, password=password, email=email
                        )


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
