from django.contrib import admin
from primary.models import PrimaryProperty, Image
from aproperty.admin import SiteFilter

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(PrimaryProperty)
class PrimaryPropertyAdmin(admin.ModelAdmin):
    list_display = [
        'site_name', 'name', 'price', 'click_amount', 'main_order', 'addres', 'district',
        'min_square', 'max_square',
        'area', "specialist", 'is_published',
    ]
    list_filter = [SiteFilter, 'specialist', 'is_published']
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
                ('lots_number',),
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
