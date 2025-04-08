from django.urls import path
from .views import ItemsView,ItemPartialUpdateView


urlpatterns = [
    path('items/', ItemsView.as_view(), name='items'),
    path('items/update/<int:item_id>/', ItemPartialUpdateView.as_view(), name='item-partial-update'),
    
]