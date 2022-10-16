from django.contrib import admin
from primary.models import PrimaryProperty, Image

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(PrimaryProperty)
class PrimaryPropertyAdmin(admin.ModelAdmin):
    list_display = [
        'site', 'name', 'price', 'click_amount', 'main_order', 'addres', 'district', 
        'min_square', 'max_square',
        'area', "specialist", 'is_published',
    ]
    list_filter = ['site', 'specialist', 'district', 'area', 'is_published']
    search_fields = ('site', 'name', 'slug')
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
        ('О комплексе', {
            'fields': (
                ('short_phrase',),
                ('description',),
                ("title_image", "second_image"),
                ('logo', 'presentation'),
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
