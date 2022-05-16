from django.contrib import admin
from .models import Profile, Repo
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'bio', 'followers', 'following')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset
        return queryset.filter(owner=user)


@admin.register(Repo)
class RepoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'language',
                    'description', 'profile_username')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset
        return queryset.filter(profile__owner=user)
