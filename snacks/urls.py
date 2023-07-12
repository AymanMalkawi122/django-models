from django.urls import path
from .views import SnacksListView,SnackDetailsView

urlpatterns = [
 
    path('',SnacksListView.as_view(), name='snacks'),
    path('<pk>/',SnackDetailsView.as_view(), name='snack_details')
]
