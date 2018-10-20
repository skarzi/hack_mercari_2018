from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.permissions import AnonymousOnly
from users.serializers import LoginUserSerializer


class AuthViewSet(ViewSet):

    @list_route(methods=["post"], permission_classes=[AnonymousOnly])
    def login(self, request):
        """
        Login user creating new Token
        """
        credentials_serializer = LoginUserSerializer(data=request.data)
        credentials_serializer.is_valid(raise_exception=True)
        user = authenticate(**credentials_serializer.data)
        if not user:
            raise AuthenticationFailed(
                detail="Incorrect credentials."
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    @list_route(methods=["post"])
    def logout(self, request):
        """
        Logout user by removing Device Token from database
        """
        token = request.auth
        token.delete()
        return Response()
