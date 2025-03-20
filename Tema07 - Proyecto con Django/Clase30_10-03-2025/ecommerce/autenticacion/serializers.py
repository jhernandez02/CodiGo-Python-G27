from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self, user):
        # Obtenemos el token principal
        token = super().get_token(user)

        # Agregamos datos personalizados al token
        token['name'] = user.get_full_name()

        return token