from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookieStands/cookieStand_list.html"
    model = CookieStand
    context_object_name = "cookieStands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookieStands/cookieStand_detail.html"
    model = CookieStand


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookieStands/cookieStand_detail.html"
    model = CookieStand
    context_object_name = "cookieStand"


class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookieStands/cookieStand_create.html"
    model = CookieStand
    fields = ["name", "location", "cookie_sales", "avg_cookie_per_hour"] # "__all__" for all of them

class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    model = CookieStand
    fields = ['name', 'location', 'cookie_sales', 'avg_cookie_per_hour']
    template_name = 'cookieStands/cookieStand_update.html'
    success_url = reverse_lazy('cookieStand_list')
    
class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookieStands/cookieStand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookieStand_list")
