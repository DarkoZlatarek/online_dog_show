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


def rules_page(request):
    """
    View for rules page.
    """
    return render(request, 'rules.html')


def enter_page(request):
    """
    View for Enter page.
    """
    return render(request, 'enter.html')


class EntriesList(generic.ListView):
    """
    View for All Entries page.
    """
    model = Enter
    queryset = Enter.objects.filter(status=1).order_by('-created_on')
    template_name = 'all_entries.html'
    paginate_by = 12


# Class created using help from StackOverflow.
class CurrentOrderList(generic.DetailView):
    """
    View for Competition page.
    Lists entry with most liked at the top.
    """
    model = Enter
    queryset = (
        Enter.objects.filter(status=1)
        .alias(nlikes=Count('likes'))
        .order_by('-nlikes')
    )
    template_name = 'competition.html'

    def get_object(self, *args, **kwargs):
        """
        Show only entry with most likes.
        """
        return self.get_queryset().first()


# Class used from "I think therefore I blog" walkthrough.
class EntryDetail(View):
    """
    Render the individual entry
    to the browser.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Create a new URL path for each blog post.
        Create a comments section on the page.
        """
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
        """
        Submit a new comment to an entry.
        """
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


# Class used from "I think therefore I blog" walkthrough.
class EntryLike(View):
    """
    Allow a user to like an entry
    """
    def post(self, request, slug):
        """
        Check if user already liked the entry.
        Allow like/unlike accordingly.
        """
        entry = get_object_or_404(Enter, slug=slug)

        if entry.likes.filter(id=request.user.id).exists():
            entry.likes.remove(request.user)
        else:
            entry.likes.add(request.user)

        return HttpResponseRedirect(reverse('entry_detail', args=[slug]))


# Function built using instructions from "Hello Django",
# "I think therefore I blog",
# a previous generation fellow student - credited in README.
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
    """
    Edit a submitted entry
    """
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


# Instructed by "Hello Django"
def delete_entry(request, slug):
    """
    Delete a submitted entry
    """
    entry = get_object_or_404(Enter, slug=slug)
    entry.delete()
    return redirect('all_entries')
