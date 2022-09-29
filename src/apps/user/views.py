import requests

from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken as StandartObtainAuthToken
from rest_framework.response import Response

from .serializers import AuthTokenSerializer
from .models import User


class ObtainAuthToken(StandartObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "role": user.role,
                    "name": user.full_name,
                    "id": user.id,
                }
            )
        response = self.__check_user(request)
        return Response(response)

    def __check_user(self, request):
        base_url = settings.AUTH_URL
        auth = requests.post(
            url=f"{base_url}/login/",
            json={
                "login": request.data['username'],
                "password": request.data['password']
                }
        )
        if auth.status_code == 200:
            full_name = requests.post(
                url=f"{base_url}/me",
                params={
                    "token": auth.json()['token']
                }
            )
            user = User.objects.update_or_create(
                full_name=full_name.json()['full_name'],
                username=request.data['username']
            )
            user.set_password(request.data['password'])
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return {
                    "token": token.key,
                    "role": user.role,
                    "name": user.full_name,
                    "id": user.id,
                }
        return {
            "status_code": auth.status_code
        }


obtain_auth_token = ObtainAuthToken.as_view()
