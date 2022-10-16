from django.contrib import admin
from primary.models import PrimaryProperty

# Register your models here.

@admin.register(PrimaryProperty)
class PrimaryPropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'click_amount', 'addres', 'district', 
        'min_square', 'max_square',
        'area', "specialist", "logo",
    ]
    list_filter = ['specialist', 'district', 'area']
    search_fields = ('name', 'slug')
    fieldsets = (
        ('Основное', {
            'fields': (
                ("name", 'slug', 'click_amount'),
                ('price',),
                ('addres', 'district'),
                ('specialist',)
            ),
        }),
        ('О комплексе', {
            'fields': (
                ('short_phrase',),
                ('description',),
                ("title_image", "second_image"),
                ('logo', 'presentation'),
                ('images',),
            ),
        }),
        ('Дополнительно', {
            'fields': (
                ('subway',),
                ('area',),
                ("min_square", "max_square"),
                ('map_script')
            ),
        }),
    )
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('images',)
