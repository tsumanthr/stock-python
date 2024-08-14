from django.contrib import admin
# Register your models here.
from .models import stock
# Register your models here.
class StockDataAdmin(admin.ModelAdmin):
    list_display =['sno',
                   'arriveddate',
                   'productName',
                   'productQ',
                   'productP']
    
admin.site.register(stock,StockDataAdmin)
