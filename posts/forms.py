from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=36, min_length=3)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()


class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=255)
