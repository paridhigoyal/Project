from django import forms
from .models import *
from django.forms import CharField, ModelForm
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    type = (
        ('T', 'Transporter'),
        ('C', 'Customer'),
    )
    email = forms.EmailField(label='Email', required=True)
    profile_type = forms.CharField(max_length=1, widget=forms.Select(choices=type))  # type: CharField
    phone = forms.CharField(max_length=12, label='Phone', required=True)
    address = forms.CharField(max_length=100, label='Address')
    city = forms.CharField(max_length=30, label='City')
    state = forms.CharField(max_length=30, label='State')
    pin_code = forms.IntegerField(label='Pin Code')

    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        p = Profile(profile_type=self.cleaned_data['profile_type'], phone=self.cleaned_data['phone'],
                    address=self.cleaned_data['address'], city=self.cleaned_data['city'],
                    state=self.cleaned_data['state'], pin_code=self.cleaned_data['pin_code'], user=user)

        p.save()
        return user


# class CustomerForm(ModelForm):
#     class Meta:
#         model=Profile
#
# class TransporterForm(ModelForm):
#     class Meta:


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {'transporter': forms.HiddenInput()}


class DealForm(ModelForm):
    rating = forms.CharField(required=False)

    # customer = forms.CharField(required=False)
    class Meta:
        model = Deal
        fields = '__all__'


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
