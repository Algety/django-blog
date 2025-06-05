from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.


def about_me(request):
    about = About.objects.order_by("updated").first()
    # about = get_object_or_404(queryset, about=about)

    return render(
        request,
        "about/about.html",
        {"about": about},
    )