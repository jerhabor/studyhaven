from django import forms
from .models import Product, Category


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        all_categories = Category.objects.all()
        shop_names = [(category.id, category.get_shop_name()) for category in all_categories]

        self.fields['category'].choices = shop_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border border-dark'
