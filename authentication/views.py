from django.contrib.auth import authenticate

from rest_framework import (authtoken, generics, permissions, response, status,
                            views)


class LoginUser(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return response.Response({'error': 'Please provvide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return response.Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_401_UNAUTHORIZED)
        else:
            token, _ = authtoken.models.Token.objects.get_or_create(user=user)
            return response.Response(
                {'token': token.key, "is_superuser": user.is_superuser},
                status=status.HTTP_200_OK
            )
