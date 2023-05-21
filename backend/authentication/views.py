import rest_framework.status as status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request) -> Response:
        content = {'message': 'Welcome to the JWT Authentication page using React JS and Django!'}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as _:
            return Response(status=status.HTTP_400_BAD_REQUEST)