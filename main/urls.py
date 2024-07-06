from django.urls import path
from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('blog/<int:id>/', views.BLogView.as_view(), name="Blog"),
]