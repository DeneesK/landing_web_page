from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

# Register your models here.
class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ("coment_date", "coment_text")
    readonly_fields = ("coment_date",)
    extra = 1

class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    readonly_fields = ('id', 'order_dt')

    inlines = [Coment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
