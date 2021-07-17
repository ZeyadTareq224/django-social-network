from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Post
from .forms import PostForm




def feed(request):
	form = PostForm()
	posts = Post.objects.all().order_by('-created_at')
	
	context = {'form': form, 'posts':posts}
	return render(request, 'feed_templates/feed.html', context)




@login_required(login_url="account_login")
@require_http_methods(['POST'])
def post_save(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.user = request.user
			form.save()
			messages.success(request, "Your post added successfully.")
			return redirect('feed')
		else:
			messages.success(request, "Form validation error.")
			return redirect('feed')
	messages.success(request, "Something went wrong.")		
	return redirect('feed')




def post_details (request, post_id):
	post = Post.objects.get(id=post_id)
	context = {'post': post,}
	return render(request, 'feed_templates/post_details.html', context)
