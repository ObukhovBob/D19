from django.urls import path, include
from .views import *


urlpatterns = [
   path('', AdsList.as_view(), name='ads_all'),
   path('<int:pk>/', AdDetail.as_view(), name='ad_id'),
   path('create/', AdCreate.as_view(), name='ad_create'),
   path('<int>/create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', AdUpdate.as_view(), name='ad_update'),
   path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
   path('<int>/postdelete/<int:pk>', PostDelete.as_view(), name='post_delete'),
   path('personalpage/', PersonalList.as_view(), name='personal_list'),


   path('about/', about, name='about'),
   path('contact/', contact, name='contact'),
]