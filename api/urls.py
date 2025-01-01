from app.views import person_view
# from app.views import index

from django.urls import path

urlpatterns = [
    # path("index/",index),
    path("person/",person_view),
]
