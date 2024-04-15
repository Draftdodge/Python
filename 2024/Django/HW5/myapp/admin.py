from django.contrib import admin
from . import models

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['-amount']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    fields = ['name', 'description', 'price', 'amount', 'image', 'added_at']
    readonly_fields = ['added_at']
    # fieldsets = [
    #     (
    #         None, {  # используем поле без определенного названия
    #             'classes': ['wide'],  # класс ['wide'] максимально большое поле в панели
    #             'fields': ['name'],  # в качестве поля name
    #         },
    #     ),
    #     (
    #         'Подробности',  # блок подробности
    #         {
    #             'classes': ['collapse'],  # схлопнутое поле(скрытое)
    #             'description': 'Категория товара и его подробное описание',  # при развороте выдает описание
    #             'fields': ['category', 'description'],  # те поля которые мы спрятали
    #         },
    #     ),
    #     (
    #         'Бухгалтерия',
    #         {
    #             'fields': ['price', 'quantity'],
    #         }
    #     ),
    #     (
    #         'Рейтинг и прочее',
    #         {
    #             'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
    #             'fields': ['rating', 'added_at'],
    #         }
    #     ),
    # ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'
    readonly_fields = ['reg_date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'common_price']

    readonly_fields = ['date']


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)