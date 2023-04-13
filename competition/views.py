from django.shortcuts import render
from django.views import generic
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
