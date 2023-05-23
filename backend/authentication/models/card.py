from dataclasses import dataclass
from typing import List, AnyStr
import json

@dataclass
class Card:
    user_id: AnyStr
    card_id: AnyStr
    link: AnyStr
    description: AnyStr
    tags: List[AnyStr]
    collection: int
    def build_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "card_id": self.card_id,
            "link": self.link,
            "description": self.description,
            "tags": self.tags,
            "collection": self.collection
        }
    def build_json_str(self) -> str:
        return json.dumps(self.build_dict())
