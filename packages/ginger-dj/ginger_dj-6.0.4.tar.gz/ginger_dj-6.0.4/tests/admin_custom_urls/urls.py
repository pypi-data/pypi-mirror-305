from gingerdj.urls import path

from .models import site

urlpatterns = [
    path("admin/", site.urls),
]
