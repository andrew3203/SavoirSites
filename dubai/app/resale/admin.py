from django.contrib import admin
from resale.models import ResaleProperty

# Register your models here.
#@admin.register(ResaleProperty)
class ResalePropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'addres', 'district', 
        'rooms_number', 'floor',
        'click', 'area', "specialist",
    ]
    list_filter = ['specialist', 'decor', 'bulding_material', 'district', 'area']
    fieldsets = (
        ('Основное', {
            'fields': (
                ("name", 'slug'),
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
                ('images',),
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
    filter_horizontal = ('images',)
