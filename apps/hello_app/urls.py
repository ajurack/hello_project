# APP URLS!
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), # localhost:8000
    url(r'^goodbye$', views.goodbye), # localhost:8000/goodbye
    url(r'^message$', views.message),
    url(r'^(?P<my_var>\w+)$', views.greet)

]
