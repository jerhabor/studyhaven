from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'occupation',
        'heading',
        'date',
    )

    fields = ('name', 'occupation', 'heading',
              'description',)


admin.site.register(Review, ReviewAdmin)
