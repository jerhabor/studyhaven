from django.contrib import admin
from .models import TutoringRate


class TutoringRateAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'price',
    )

    fields = ('subject', 'price',)


admin.site.register(TutoringRate, TutoringRateAdmin)
