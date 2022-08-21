from django.shortcuts import redirect, render
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
from .models import Video
from django.db.models import F
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context

class Signup(View):
    # show a form to fill out
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
        return context

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