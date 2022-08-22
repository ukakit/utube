from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from .models import Video, Comment
from .form import CommentForm



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class VideoDetail(DetailView):
    model = Video
    template_name = "video_detail.html"
    # when video detail page loads, increment view to the video
    def add_view(self, request):
        my_video = Video.objects.get(id=self.kwargs['pk'])
        my_video.view = F('view') + 1
        my_video.save()

    def dispatch(self, request, *args, **kwargs):
        self.add_view(request)
        return super(VideoDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        form = CommentForm()
        video = get_object_or_404(Video, pk=pk)
        comments = video.comment_set.all()

        context['video'] = video
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        video = Video.objects.filter(id=self.kwargs['pk'])[0]
        comments = video.comment_set.all()

        context['video'] = video
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            body = form.cleaned_data['body']
            # creates the form on db
            comment = Comment.objects.create(
                body=body, video=video, user_id = self.request.user.id
            )
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)
        # currently, if text area is empty, page refreshes, no comment is added, but without the following line, breaks
        return self.render_to_response(context=context)

class VideoCreate(CreateView):
    model = Video
    fields = ['title', 'description', 'thumbnail']
    template_name = 'video_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VideoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('video_detail', kwargs={'pk': self.object.pk})

class VideoUpdate(UserPassesTestMixin, AccessMixin, UpdateView):
    model = Video
    fields = ['title', 'description', 'thumbnail']
    template_name = "video_update.html"
    permission_denied_message = 'not owner'    
    def test_func(self):
        return self.request.user == self.get_object().user
    def get_success_url(self):
        reverse('video_detail', kwargs={'pk': self.object.pk})

class VideoDelete(UserPassesTestMixin, AccessMixin, DeleteView):

    model = Video
    template_name = "video_delete_confirmation.html"
    success_url = "/"
    permission_denied_message = 'not owner'    
    def test_func(self):
        return self.request.user == self.get_object().user

class CommentUpdate(UserPassesTestMixin, AccessMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = "comment_update.html"
    permission_denied_message = 'not owner'
    def test_func(self):
        print(self.request.user)
        return self.request.user == self.get_object().user
    def get_success_url(self):
        video_id = self.object.video_id
        return (f'/video/{video_id}')