from django.contrib import admin
from group_yum.models import Group, User

admin.site.register(User)
admin.site.register(Group)