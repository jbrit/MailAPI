from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import EmailAdded
from .serializers import EmailAddedSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

def login_view(request):
    alert = None
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        email = request.POST.get("login-email")
        password = request.POST.get("login-password")
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            username = 'No one'

        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            alert = {
                'message': 'Invalid Login Details!',
                'class': 'danger',
                'icon': "error",
            }
    context = {
        "alert": alert
    }
    return render(request, 'core/auth.html', context)

def logout_view(request):
    logout(request)
    return redirect("/")

def home(request):
    token = "None"
    if request.user.is_authenticated:
        token = str(Token.objects.get_or_create(user=request.user)[0])
    print(token)
    context = {"token":token}
    return render(request, 'core/home.html', context)


class EmailList(ListCreateAPIView):
    serializer_class = EmailAddedSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return EmailAdded.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EmailDelete(DestroyAPIView):
    serializer_class = EmailAddedSerializer

    def get_queryset(self):
        return EmailAdded.objects.filter(owner=self.request.user)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)