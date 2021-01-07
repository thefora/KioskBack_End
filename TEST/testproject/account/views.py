from django.shortcuts import render
from rest_auth.views import LoginView, LogoutView
from rest_framework import status

from .serializer import k_userSerializer
from .models import k_user

# Create your views here.pi
class CustomLoginView(LoginView):
    queryset = k_user.objects.all()
    serializer_class = k_userSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        self.data = get_tokens_for_user(self.user)

        # return self.get_response()
    
        return Response(
                    data=self.data,
                    headers={'content-type': 'application/json', 'charset': 'utf-8'},
                    status=status.HTTP_200_OK,
                )