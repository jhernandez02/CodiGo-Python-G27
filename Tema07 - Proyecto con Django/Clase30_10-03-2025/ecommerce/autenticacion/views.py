from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .serializers import LoginSerializer

# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            # Intentamos obtener el token
            return super().post(request, *args, **kwargs)
        except AuthenticationFailed:
            return Response({
                'message': 'Credenciales incorrectas'
            }, 401)


