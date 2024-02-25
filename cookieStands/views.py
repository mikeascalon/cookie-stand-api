from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic.edit import UpdateView, DeleteView
from .models import CookieStand  
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer  
from django.urls import reverse_lazy

class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()  
    serializer_class = CookieStandSerializer  

class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()  
    serializer_class = CookieStandSerializer  

class CookieStandUpdateView(UpdateView):
    model = CookieStand
    fields = ['name', 'location', 'owner', 'description', 'hourly_sales', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale']
    template_name = 'cookieStands/cookieStand_update.html'
    success_url = reverse_lazy('cookieStand_list')  

class CookieStandDeleteView(DeleteView):
    model = CookieStand
    # Specify the success_url to redirect to after a successful delete
    success_url = '/cookieStands/'  