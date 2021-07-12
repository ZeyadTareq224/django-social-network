from allauth.account.forms import SignupForm
from django import forms
from  .models import User, Profile


GENDER = [
	('Male', 'Male'),
	('Female', 'Female'),
	('Other', 'Other')
]

class CustomSignupFrom(SignupForm):
	first_name = forms.CharField(max_length=30, label='First Name')
	last_name = forms.CharField(max_length=30, label='Last Name')
	gender= forms.CharField(label='Select your gender', widget=forms.Select(choices=GENDER))
	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.gender = self.cleaned_data['gender']
		user.save()
		return user



class User_ProfileForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

class ProfileFrom(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['gender', 'location', 'phone_number']


