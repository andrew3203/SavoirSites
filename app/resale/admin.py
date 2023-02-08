from django.contrib import admin
from resale.models import ResaleProperty, Image
from aproperty.admin import SiteFilter, LivingType, LivingPropertyType


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(ResaleProperty)
class ResalePropertyAdmin(admin.ModelAdmin):
    list_display = [
        'site_name', 'name', 'price', 'click_amount', 'addres',
        'area', "specialist", 'is_published',
    ]
    list_filter = [SiteFilter, 'specialist', 'area', 'is_published']
    search_fields = ('name', 'slug')
    inlines = [
        ImageInline,
    ]
    fieldsets = (
        ('Основное', {
            'fields': (
                ('site',),
                ("name", 'slug',),
                ('click_amount', 'is_published'),
                ('price',),
                ('addres',),
                ('specialist',)
            ),
        }),
        ('О лоте (основное)', {
            'fields': (
                ('description',),
                ("title_image",),
                ('living_type',)
            ),
        }),
        ('О лоте (дополнительно)', {
            'fields': (
                ('map_script'),
                ('area', 'square'),
                ('ownership', "terrace",),
                ('parking', "rooms_on_floor", "rooms"),
                ("floor", "floors_number"),
                ("elevators", "freight_elevators"),
                ('window_to', 'rooms_number'),
                ("bulding_material", "construction_year"),
                ('decor', 'entrances', 'ceiling_height'),
            ),
        }),
    )
    prepopulated_fields = {'slug': ('name',)}

    def publish(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, f"{len(queryset)} опубликовано")

    def unpublish(self, request, queryset):
        queryset.update(is_published=False)
        self.message_user(
            request, f"{len(queryset)} обьектов снято с публикации")

    actions = [publish, unpublish]
    publish.short_description = 'Опубликовать обьекты'
    unpublish.short_description = 'Снять с публикации'
    