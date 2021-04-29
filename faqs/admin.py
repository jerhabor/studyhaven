from django.contrib import admin
from .models import FAQ


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
    )

    fields = ('question', 'answer',)


admin.site.register(FAQ, FaqAdmin)
