from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from aproperty.models import *


class SiteFilter(SimpleListFilter):
    title = 'Сайты'
    parameter_name = 'site_pk'

    def lookups(self, request, model_admin):
        sites = set([o.site.site for o in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in sites]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(site__site__pk=self.value())
        else:
            return queryset


class YouTubeLinkInline(admin.TabularInline):
    model = YouTubeLink
    extra = 1


class MainSliderInline(admin.TabularInline):
    model = MainSlider
    extra = 1


@admin.register(SiteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'header_phone', 'created_at']
    search_fields = ['header_phone']
    inlines = [
        MainSliderInline,
        YouTubeLinkInline,
    ]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['site_name','name', 'phone', 'email', 'complex', 'created_at']
    search_fields = ['name', 'phone', 'email']
    list_filter = [SiteFilter]


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
    list_display = ['site_name', 'name']
    search_fields = ('name',)
    list_filter = [SiteFilter]
    inlines = [
        AreaPeculiarityInline,
    ]

admin.site.site_header = 'STATUS Админ панель'
admin.site.site_title ='Панель администратора STATUS'
admin.site.index_title = 'Администратор'

