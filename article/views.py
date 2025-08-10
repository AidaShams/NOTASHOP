from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "article/list.html"
    context_object_name = "data"
    queryset = Article.objects.filter(is_published=True)
    ordering = ['-publish_date']

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Article
from .forms import CommentForm

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article/detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = kwargs.get('form') or CommentForm()
        context['comments'] = self.object.comments.filter(is_approved=True).order_by('created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.writer = request.user
            comment.save()
            return redirect(self.get_success_url())
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.object.slug})

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/create.html"
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/update.html"
    success_url = reverse_lazy('list')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy('list')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user