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


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {'transporter': forms.HiddenInput()}


class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'


class SearchForm(ModelForm):
    start_city = forms.CharField(required=False)
    end_city = forms.CharField(required=False)
    start_Date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    class Meta:
        model = Deal
        fields = ['start_city', 'end_city', 'start_Date', 'end_date']


class QueryRequestForm(ModelForm):
    class Meta:
        model = QueryRequest
        fields = '__all__'
        widgets = {'deal': forms.HiddenInput(), 'username': forms.HiddenInput()}


class QueryResponseForm(ModelForm):
    class Meta:
        model = QueryResponse
        fields = '__all__'
        widgets = {'request_id': forms.HiddenInput(), 'username': forms.HiddenInput()}


class RatingForm(ModelForm):
    rate = (('1', 'Worst Experience'), ('2', 'Bad Experience',),
            ('3', 'Good Experience'), ('4', 'Very Good Experience'),
            ('5', 'Excellent Experience')
            )
    rating = forms.CharField(max_length=1, widget=forms.Select(choices=rate))

    class Meta:
        model = Rating
        fields = '__all__'
