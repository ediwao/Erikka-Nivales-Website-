from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path ("", HomePageView.as_view(), name="Home_View"),
    path ("about/", AboutPageView.as_view(), name="About_View")
]
