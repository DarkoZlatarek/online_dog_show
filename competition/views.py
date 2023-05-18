from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Enter
from django.contrib import messages
from .forms import CommentForm, EnterForm


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


def enter_page(request):
    """
    View for Enter page.
    """
    return render(request, 'enter.html')


class EntriesList(generic.ListView):

    model = Enter
    queryset = Enter.objects.filter(status=1).order_by('-created_on')
    template_name = 'all_entries.html'
    paginate_by = 6


class CurrentOrderList(generic.DetailView):
    model = Enter
    queryset = (
        Enter.objects.filter(status=1)
        .alias(nlikes=Count('likes'))
        .order_by('-nlikes')
    )
    template_name = 'competition.html'

    def get_object(self, *args, **kwargs):
        return self.get_queryset().first()


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


def enter_submit(request):
    """
    View for Enter page.
    """
    if request.method == 'POST':
        enter_form = EnterForm(request.POST, request.FILES)
        if enter_form.is_valid():
            enter_form.instance.competitor = request.user
            enter_form.save()
            return redirect('all_entries')
        else:
            enter_form = EnterForm()

    return render(
        request,
        'enter.html',
        {
            'enter_form': EnterForm(),
        },
    )


def edit_entry(request, slug):

    entry = get_object_or_404(Enter, slug=slug)
    edit_form = EnterForm(request.POST or None, instance=entry)
    context = {
        'edit_form': edit_form,
        'entry': entry
    }

    if request.method == 'POST':
        edit_form = EnterForm(
            request.POST, request.FILES, instance=entry)
        if edit_form.is_valid():
            entry = edit_form.save(commit=False)
            entry.competitor = request.user
            entry.save()
            return redirect('all_entries')
    else:
        edit_form = EnterForm(instance=entry)

    return render(request, 'edit_entry.html', context)


def delete_entry(request, slug):

    entry = get_object_or_404(Enter, slug=slug)
    entry.delete()
    return redirect('all_entries')
