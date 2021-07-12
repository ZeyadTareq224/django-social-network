from django.shortcuts import render, redirect

# django forms imports
from .forms import User_ProfileForm, ProfileFrom

# django models imports
from .models import Profile, User




def account_info (request):
	user = User.objects.get(email=request.user.email)
	context = {
		'user': user,
	}
	return render(request, 'user_templates/pages/account_info.html')


def account_settings (request):
	user = request.user
	profile = Profile.objects.get(user=user)

	user_profile_form = User_ProfileForm(instance=user)
	profile_from = ProfileFrom(instance=profile)

	if request.method == "POST":
		user_profile_form = User_ProfileForm(request.POST, instance=user)
		profile_from = ProfileFrom(request.POST, instance=profile)

		if user_profile_form.is_valid() and profile_from.is_valid():
			user_profile_form.save()
			profile_from.save()
			return redirect('account_info')
	context = {
	'user_profile_form': user_profile_form,
	'profile_from': profile_from,
	}		
	return render(request, 'user_templates/pages/account_settings.html', context)	