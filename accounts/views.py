from django.shortcuts import render, get_object_or_404

from .models import Profile


def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()


	return render(request, "profile.html")