from django.contrib import admin

from .models import RulesCategory, Rules

@admin.register(RulesCategory)
class RulesCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    pass