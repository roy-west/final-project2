from django.contrib import admin

from .models import Advantage, Address, Question


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

