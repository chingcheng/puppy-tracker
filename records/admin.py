from django.contrib import admin
from records.models import Category, Log

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "id"
    )

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "description",
        "category",
        "id"
    )

    class Meta:
        verbose_name_plural = "Tracker Log"
