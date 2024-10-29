from gingerdj.urls import re_path
from gingerdj.views.generic import TemplateView

view = TemplateView.as_view(template_name="dummy.html")

urlpatterns = [
    re_path("^nl/foo/", view, name="not-translated"),
]
