from django.contrib import admin
from resale.models import ResaleProperty, Image
from aproperty.admin import SiteFilter


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(ResaleProperty)
class ResalePropertyAdmin(admin.ModelAdmin):
    list_display = [
        'site_name', 'name', 'price', 'click_amount', 'main_order', 'addres', 'district', 
        'min_square', 'max_square',
        'area', "specialist", 'is_published',
    ]
    list_filter = [SiteFilter, 'specialist', 'district', 'area', 'is_published']
    search_fields = ('name', 'slug')
    inlines = [
        ImageInline,
    ]
    fieldsets = (
        ('Основное', {
            'fields': (
                ('site',),
                ("name", 'slug',),
                ('main_order', 'click_amount', 'is_published'),
                ('price',),
                ('addres', 'district'),
                ('specialist',)
            ),
        }),
        ('О лоте (основное)', {
            'fields': (
                ('short_phrase',),
                ('description',),
                ("title_image", "second_image"),
                ('logo', 'presentation'),
            ),
        }),
        ('О лоте (дополнительно)', {
            'fields': (
                ('subway', 'area',),
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
