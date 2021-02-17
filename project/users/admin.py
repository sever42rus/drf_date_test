from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group

from .models import User, UserGroup, UserLog

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = User

    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональные данные', {
         'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Разрешения', {'fields': ('is_active',
                                   'is_staff', 'is_superuser', 'groups',)}),
        ('Информация о входе', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(UserGroup)
class UserGroupAdmin(GroupAdmin):
    pass


@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = 'action_time', 'user', 'content_type', '__str__',
    raw_id_fields = 'user',
    date_hierarchy = 'action_time'
    list_filter = 'content_type',
