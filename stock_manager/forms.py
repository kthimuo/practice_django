from django import forms
from .models import Maker,Product,SmartPhone,Stock

class RegisterMakerForm(forms.ModelForm):
#    name = forms.CharField()
    class Meta:
        model = Maker
        fields = ('name',)
        labels = {
            'name': 'メーカー',
        }
        help_texts = {
            'name': 'メーカーを入力',
        }


class RegisterProductForm(forms.ModelForm):
    maker= forms.ModelChoiceField(
        label = 'メーカー名',
        queryset=Maker.objects.all(),
        to_field_name='name',
        )
    release_date = forms.DateField(
        label='発売日',
        widget=forms.DateInput(attrs={"type":"date"})
    )
    name = forms.CharField()
    class Meta:
        model = Product
        fields = ('maker', 'name', 'release_date')
    field_order = ('maker', 'name', 'release_date')


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.__str__


class RegisterSmartPhoneForm(forms.ModelForm):
    product= forms.ModelChoiceField(
        label = '機種名',
        queryset=Product.objects.all(),
        )
    storage = forms.IntegerField(label='データ容量(GB)')
    color = forms.CharField(label='色')
    class Meta:
        model = SmartPhone
        fields = ('product', 'storage', 'color')
    field_order = ('product', 'storage', 'color')


class RegisterStockForm(forms.ModelForm):
    smartphone = MyModelChoiceField(
        label = 'スマートフォン',
        queryset=SmartPhone.objects.all(),
        )
    version = forms.CharField(label='OSバージョン')
    price = forms.IntegerField(label='販売価格(円)')
    class Meta:
        model = Stock
        fields = ('smartphone', 'version', 'price')
    field_order = ('smartphone', 'version', 'price')

