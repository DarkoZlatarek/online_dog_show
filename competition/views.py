from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Enter


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
        queryset = Entry.objects.filter(status=1)
        entry = get_object_or_404(queryset, slug=slug)
        comments = entry.comments.filter(approved=True).order_by('created_on')
        liked = False
        if entry.liked.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            'entry_detail.html',
            {
                'entry': entry,
                'comments': comments,
                'liked': liked
            }
        )
