from typing import List, AnyStr
from functools import reduce
import operator

from django.db.models.query import QuerySet
from django.db.models.query import Q
import rest_framework.status as status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .data_models.card import Card
from .models import Tags, Cards


class AddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request) -> Response:
        auth_token = request.data.get('access_token')
        if not auth_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        user_id = request.user.pk
        cards = request.data.get('cards')
        if not cards:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            for card_dict in cards:
                card = Cards()
                card.title = card_dict['title']
                card.description = card_dict.get('description', '')
                card.user = user_id
                card.save()
                for tag_dict in card_dict.get('tags', []):
                    tag = Tags()
                    tag.user = user_id
                    tag.card = card.pk
                    tag.title = tag_dict['tag']
                    tag.save()
        except Exception as e:
            print("An exception has occurred:", e)
            print("Request data:", request.data)
            return Response(status=status.HTTP_418_IM_A_TEAPOT)
        return Response(status=status.HTTP_201_CREATED)


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request) -> Response:
        auth_token = request.META.get('HTTP_AUTHORIZATION')
        if not auth_token:
            return Response(status=status.HTTP_404_NOT_FOUND)
        current_user = request.user
        if request.data.get('search'):
            search_tags: List[AnyStr] = request.data.get('tags', [])
            clauses = (Q(tags__title__iexact=search_tag, user=current_user) for search_tag in search_tags)
            query = reduce(operator.or_, clauses)
            print('search tags:', search_tags)
            cards: QuerySet[Cards] = Cards.objects.filter(query).distinct()
        else:
            cards: QuerySet[Cards] = Cards.objects.filter(user=current_user)
        card_dicts: List[dict] = [Card().build_from_queryset(card).build_dict() for card in cards]
        content = {
            'cards': card_dicts
        }
        print("content:", content)
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
