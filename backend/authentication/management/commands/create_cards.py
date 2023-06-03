from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Cards, Tags


class Command(BaseCommand):
    help = 'Load card data'

    def handle(self, *args, **options):
        primary_user = User.objects.get(username='tobyw')
        google_card = Cards.objects.get_or_create(
            user_id=primary_user,
            description="Google's website.",
            collection=1,
            title='Google',
            link='https://www.google.com'
        ) [0]
        twitter_card = Cards.objects.get_or_create(
            user_id=primary_user,
            description="Twitter's website.",
            collection=1,
            title='Twitter',
            link='https://www.twitter.com'
        )[0]
        google_official_tag = Tags.objects.get_or_create(
            user_id=primary_user,
            card_id=google_card,
            tag='Official'
        )[0]
        google_google_tag = Tags.objects.get_or_create(
            user_id=primary_user,
            card_id=google_card,
            tag='google',
        )[0]
        twitter_official_tag = Tags.objects.get_or_create(
            user_id=primary_user,
            card_id=twitter_card,
            tag='twitter',
        )[0]
        twitter_twitter_tag = Tags.objects.get_or_create(
            user_id=primary_user,
            card_id=twitter_card,
            tag='twitter',
        )[0]
