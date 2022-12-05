from django.contrib import admin

from .models import ComputerRoom, Computer, Order, RateComputerRoom


admin.site.register(ComputerRoom)
admin.site.register(Computer)
admin.site.register(Order)
admin.site.register(RateComputerRoom)

