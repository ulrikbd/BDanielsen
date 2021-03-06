from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AboutForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context =  {
        'posts': Post.objects.all()
    }
    # if request.GET:
    #     query = request.GET['q']
    #     context['queary'] = str(query)

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            like_website = form.cleaned_data['like_website']
            like_pizza = form.cleaned_data['like_pizza']
            favourite_food = form.cleaned_data['favourite_food']
            options = form.cleaned_data['options']

            context = {
                'title': 'Success!',
                'like_website': like_website,
                'like_pizza': like_pizza,
                'favourite_food': favourite_food,
                'options': options
            }
            return render(request, 'blog/success.html', context)
    else:
        form = AboutForm()
    return render(request, 'blog/about.html', {'form': form, 'title': 'About'})


def about_success(request):
    return render(request, 'blog/success.html', {'title': 'Success?', 'like_pizza': 'no'})


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        found_entries = Post.objects.filter(title__icontains=query_string).order_by('date_posted')
        if found_entries:
            return render(request, 'blog/home.html', {'query_string': query_string, 'posts': found_entries})
        else:
            messages.info(request, f'Your search matches nothing')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))











