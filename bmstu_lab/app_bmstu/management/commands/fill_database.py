from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app_bmstu.models import Profile, Post, Comment, LikePost
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Fill the database with users, posts, comments, and post likes.'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Coefficient for data population')

    def handle(self, *args, **options):
        ratio = options['ratio']

        self.stdout.write(self.style.SUCCESS(f'Creating {ratio} users...'))
        self.create_users(ratio)

        self.stdout.write(self.style.SUCCESS(f'Creating {ratio * 10} posts...'))
        self.create_posts(ratio)

        self.stdout.write(self.style.SUCCESS(f'Creating {ratio * 50} comments...'))
        self.create_comments(ratio)

        self.stdout.write(self.style.SUCCESS(f'Creating {ratio * 100} post likes...'))
        self.create_likes(ratio)

        self.stdout.write(self.style.SUCCESS('Database population completed.'))

        for post in Post.objects.all():
            like_count = LikePost.objects.filter(post=post).count()
            post.rating = like_count
            post.save()


    def create_users(self, ratio):
        users = [
            User(username=fake.user_name(), email=fake.email(), password=fake.password())
            for _ in range(ratio)
        ]
        User.objects.bulk_create(users)

        profiles = [Profile(user=user) for user in users]
        Profile.objects.bulk_create(profiles)

    def create_posts(self, ratio):
        authors = list(Profile.objects.all())

        posts = [
            Post(
                text=fake.text(),
                author=random.choice(authors),
            )
            for _ in range(ratio * 10)
        ]
        Post.objects.bulk_create(posts)

    def create_comments(self, ratio):
        posts = list(Post.objects.all())
        authors = list(Profile.objects.all())
        comments = [
            Comment(
                text=fake.text(),
                post=random.choice(posts),
                author=random.choice(authors)
            )
            for _ in range(ratio * 50)
        ]
        Comment.objects.bulk_create(comments)

    def create_likes(self, ratio):
        posts = list(Post.objects.all())
        users = list(Profile.objects.all())
        like_post_objects = []

        for _ in range(ratio * 100):
            user = random.choice(users)
            post = random.choice(posts)

            like_post_objects.append(LikePost(user=user, post=post))

        LikePost.objects.bulk_create(like_post_objects, ignore_conflicts=True)