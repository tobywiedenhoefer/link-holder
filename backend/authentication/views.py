from typing import List

import rest_framework.status as status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models.card import Card


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request) -> Response:
        auth_token = request.META['HTTP_AUTHORIZATION']
        if not auth_token:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cards: List[Card] = [
            Card(
                user_id='1',
                card_id='1',
                link='https://www.twitter.com',
                description="Twitter's official website",
                tags=['Official', 'twitter'],
                collection=1
            ),
            Card(
                user_id='1',
                card_id='2',
                link='https://www.google.com',
                description="Google's official website",
                tags=['Official', 'google'],
                collection=1
            ),
        ]
        content = {
            'message': 'Welcome to the JWT Authentication page using React JS and Django!',
            'cards': [card.build_dict() for card in cards]
        }
        print('content: ', content)
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
