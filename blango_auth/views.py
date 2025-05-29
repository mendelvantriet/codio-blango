from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@login_required
#@csrf_protect # We need this because we disabled CsrfViewMiddleware, but we use a csrf_token in the view
def profile(request):
    return render(request, "blango_auth/profile.html")

