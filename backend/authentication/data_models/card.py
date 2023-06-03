from typing import List, AnyStr, Optional
import json

from ..models import Cards


class Card:
    def __init__(self,
                 user_id: Optional[int] = None,
                 card_id: Optional[int] = None,
                 link: AnyStr = "",
                 description: AnyStr = "",
                 tags: Optional[List[AnyStr]] = None,
                 title: AnyStr = "",
                 collection: int = 1):
        self.user_id: Optional[int] = user_id
        self.card_id: Optional[int] = card_id
        self.link: AnyStr = link
        self.description: AnyStr = description
        self.tags: List[AnyStr] = tags or []
        self.title: AnyStr = title
        self.collection: int = collection

    def build_dict(self) -> dict:
        return {
            "user_id": str(self.user_id),
            "card_id": str(self.card_id),
            "link": self.link,
            "description": self.description,
            "tags": self.tags,
            "collection": str(self.collection),
            "title": self.title
        }

    def build_json_str(self) -> str:
        return json.dumps(self.build_dict())

    def build_from_queryset(self, card_query: Cards):
        self.user_id = card_query.user.pk
        self.card_id = card_query.pk
        self.link = card_query.link
        self.description = card_query.description
        self.tags = [tag.title for tag in card_query.tags_set.all()]
        self.collection = card_query.collection
        self.title = card_query.title
        return self
