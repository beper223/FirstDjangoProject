from django.contrib import admin

# Register your models here.
from src.library.models.book import Book
from src.library.models.soc_media import Post, UserProfile, Comment
from src.library.models.author import Author

admin.site.register(Book)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Author)
