from django.contrib import admin
from resale.models import ResaleProperty, ReImage
from aproperty.admin import SiteFilter


class ImageInline(admin.TabularInline):
    model = ReImage
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
            ),
        }),
        ('О лоте (дополнительно)', {
            'fields': (
                ('area', 'square'),
                ('map_script'),
                ('ownership',"penthouse", "terrace", "parking"),
                ("rooms_on_floor", "rooms_in_hous"),
                ("floor", "floor_number"),
                ("elevators", "freight_elevators"),
                ('window_to', 'rooms_number'),
                ("bulding_material", "construction_year"),
                ('entrances', 'decor', 'ceiling_height'),
            ),
        }),
    )
    prepopulated_fields = {'slug': ('name',)}
