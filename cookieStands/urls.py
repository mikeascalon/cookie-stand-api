from django.urls import path
from .views_front import CookieStandListView, CookieStandDetailView, CookieStandUpdateView, CookieStandCreateView, CookieStandDeleteView

urlpatterns = [
    path('', CookieStandListView.as_view(), name='cookieStand_list'),
    path('cookieStands/<int:pk>/', CookieStandDetailView.as_view(), name='cookieStand_detail'),
    path('cookieStands/<int:pk>/update/', CookieStandUpdateView.as_view(), name='cookieStand_update'),
    path('cookieStands/create/', CookieStandCreateView.as_view(), name='cookieStand_create'),
    path('cookieStands/<int:pk>/delete/', CookieStandDeleteView.as_view(), name='cookieStand_delete'),
]