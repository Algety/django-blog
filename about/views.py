from django.shortcuts import render, get_object_or_404
from .models import About, CollaborateRequest
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.


def about_me(request):
    about = About.objects.order_by("updated").first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
    )

    collaborate_form = CollaborateForm()
    # about = get_object_or_404(queryset, about=about)

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form
        },
    )

def comment_edit(request):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))