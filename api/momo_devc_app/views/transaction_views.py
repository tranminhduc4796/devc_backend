from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import TransactionSerializer
from ..models import Transaction, Profile
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ListCreate(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(Profile, user=self.request.user)
        return Transaction.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = get_object_or_404(Profile, user=self.request.user)
        transaction = Transaction(user=user)
        serializer = self.serializer_class(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]