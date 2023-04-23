from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Enter
from .forms import CommentForm


def home_page(request):
    """
    View for home page.
    """
    return render(request, 'index.html')


def about_page(request):
    """
    View for about page.
    """
    return render(request, 'about.html')


class EntriesList(generic.ListView):

    model = Enter
    queryset = Enter.objects.filter(status=1).order_by('-created_on')
    template_name = 'competition.html'
    paginate_by = 6


class EntryDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Enter.objects.filter(status=1)
        entry = get_object_or_404(queryset, slug=slug)
        comments = entry.comments.filter(approved=True).order_by('created_on')
        liked = False
        if entry.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            'entry_detail.html',
            {
                'entry': entry,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Enter.objects.filter(status=1)
        entry = get_object_or_404(queryset, slug=slug)
        comments = entry.comments.filter(approved=True).order_by('created_on')
        liked = False
        if entry.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = entry
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            'entry_detail.html',
            {
                'entry': entry,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )


class EntryLike(View):

    def post(self, request, slug):
        entry = get_object_or_404(Enter, slug=slug)

        if entry.likes.filter(id=request.user.id).exists():
            entry.likes.remove(request.user)
        else:
            entry.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('entry_detail', args=[slug]))
