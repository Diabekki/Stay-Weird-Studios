from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from cart_checkout.models import Purchase


def user(request):

    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user)
    purchases = user.purchases.all()

    template = 'user_profiles/user.html'
    context = {
        'form': form,
        'purchases': purchases,
        'on_profile_page': True,
    }
        
    return render(request, template, context)