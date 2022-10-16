from django.contrib import admin
from aproperty.models import *

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'complex', 'created_at']
    search_fields = ['name', 'phone', 'email']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'role', 'phone', 'email',
    ]
    search_fields = ('name', 'role')
    fieldsets = (
        ('Основное', {
            'fields': (
                ("name",),
                ('role',),
                ('photo',),
                ('phone', 'email'),
            ),
        }),
        ('Сот. сети', {
            'fields': (
                ('tg_link',),
                ("wh_link",)
            ),
        }),
    )


class AreaPeculiarityInline(admin.TabularInline):
    model = AreaPeculiarity
    extra = 1


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    inlines = [
        AreaPeculiarityInline,
    ]


admin.site.site_header = 'Dubai RU Админ панель'
admin.site.index_title = 'Dubai RU Администратор'
admin.site.site_title = 'Admin'