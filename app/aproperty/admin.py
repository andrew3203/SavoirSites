from django.contrib import admin
from aproperty.models import SiteData, Client, Specialist, Area, AreaPeculiarity

# Register your models here.
@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ['site', 'header_phone', 'created_at']
    search_fields = ['site', 'header_phone']
    list_filter = ['site',]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['site','name', 'phone', 'email', 'complex', 'created_at']
    search_fields = ['site', 'name', 'phone', 'email']
    list_filter = ['site',]


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
    list_display = ['site', 'name']
    search_fields = ('site', 'name',)
    list_filter = ['site',]
    inlines = [
        AreaPeculiarityInline,
    ]
