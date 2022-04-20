from django.conf import settings

#third-party imports 
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt

#local imports
from authentication.models import User


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode('utf-8')

        auth_token = auth_data.split(" ")

        if len(auth_token)!=2:
            raise AuthenticationFailed('Token not valid.')

        token = auth_token[1]
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            username = payload["username"]

            user = User.objects.get(username=username)

            return (user, token)

        except jwt.ExpiredSignatureError as ex:
            raise AuthenticationFailed('Token is expired, login again.')

        except jwt.DecodeError as ex:
            raise AuthenticationFailed('Token is invaalid.')

        except User.DoesNotExist as no_user:
            raise AuthenticationFailed('No such user.')

        return super().authenticate(request)