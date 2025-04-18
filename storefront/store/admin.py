from django.contrib import admin,messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html,urlencode
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        ]
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt =10)
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price','inventory_status','collection__title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection','last_update',InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
           return 'Low'
        return 'Ok'
    @admin.action(description='Clear invetory')
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR
        )
        
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','membership']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name__startswith', 'last_name__startswith']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']

    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url =( reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id':str(collection.id)
            }))
        return format_html('<a href= "{}">{}</a>',url,collection.products_count)
       
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count = Count('product'))
    
class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']
    inlines= [OrderItemInline]
    autocomplete_fields =['customer']