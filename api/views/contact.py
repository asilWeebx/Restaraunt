from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main.models import Contact
from api.serializer.contact import ContactModelSerializer


class ContactCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = (IsAuthenticated, )


class ContactDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = (IsAdminUser, )