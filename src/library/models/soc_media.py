from datetime import datetime
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, DateTimeField, URLField, EmailField, SlugField, UUIDField, \
    DurationField, ImageField, ForeignKey, CASCADE, SET_NULL, PROTECT, OneToOneField, \
    ManyToManyField


class Post(Model):
    id: uuid4 = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    title = CharField(
        max_length=95
    )
    content: str = TextField()
    created_at: datetime = DateTimeField(
        auto_now_add=True
    )
    updated_at: datetime = DateTimeField(
        auto_now=True
    )
    reading_time: int = DurationField(
        null=True,
        blank=True
    )
    screenshot = ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )
    attachment = ImageField(
        upload_to='files/',
        null=True,
        blank=True
    )
    published_at = DateTimeField(
        auto_now=True
    )
    image_url: str = URLField(
        max_length=255,
        null=True, # позволяет хранить в базе пустые значения
        blank=True # в формах хранить поле как необзязательное значение
    )
    contact_email: str = EmailField(
        max_length=80,
        null=True,
        blank=True
    )
    author = ForeignKey(
        'UserProfile',
        # on_delete=models.CASCADE,
        # on_delete=models.SET_NULL,
        null=True,
        # on_delete=models.SET_DEFAULT,
        # default=lambda: UserProfile.objects.filter(role='admin').first(),
        # on_delete=models.SET(),
        # on_delete=models.DO_NOTHING,
        on_delete=PROTECT,
    )

class UserProfile(Model):
    full_name = CharField(
        max_length=60
    )
    bio = TextField()
    slug = SlugField(
        unique=True
    )
    subscriptions = ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True,
    )
    user = OneToOneField(
        User,
        on_delete=CASCADE,
        related_name='profile' # поля мостики
    )
    def __str__(self):
        return self.full_name

class Comment(Model):
    post = ForeignKey(
        Post,
        on_delete=CASCADE,
        related_name='comments'
    )
    author = ForeignKey(
        UserProfile,
        on_delete=SET_NULL,
        null=True,
        related_name='comments'
    )
    content = TextField()
    created_at = DateTimeField(
        auto_now_add=True
    )
    parent = ForeignKey(
        'self',
        on_delete=CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )