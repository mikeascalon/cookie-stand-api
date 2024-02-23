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
    fields = ['name', 'location', 'cookie_sales', 'avg_cookie_per_hour']
    template_name = 'cookieStands/cookieStand_update.html'
    # Make sure to specify the correct success_url
    success_url = '/cookieStands/'  # Adjust as necessary

class CookieStandDeleteView(DeleteView):
    model = CookieStand
    # Specify the success_url to redirect to after a successful delete
    success_url = '/cookieStands/'  # Adjust as necessary