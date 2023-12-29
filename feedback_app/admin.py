from django.contrib.admin import ModelAdmin,register
from .models import Comments

@register(Comments)
class CommentsAdmin(ModelAdmin):
    list_display =['name', 'last_name', 'email']