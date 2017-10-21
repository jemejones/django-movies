"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from movies_app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^actors/$', views.ActorIndexView.as_view(), name='actor-index'),
    url(r'^actors/(?P<pk>[0-9]+)/$', views.ActorDetailView.as_view(), name='actor-detail'),
    url(r'^actors/(?P<pk>[0-9]+)/edit/$', views.ActorUpdateView.as_view(), name='actor-update'),
    url(r'^actors/create/$', login_required(views.ActorCreateView.as_view()), name='actor-create'),

    url(r'^movies/$', views.MovieIndexView.as_view(), name='movie-index'),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MovieDetailView.as_view(), name='movie-detail'),
    url(r'^movies/(?P<pk>[0-9]+)/edit/$', views.MovieUpdateView.as_view(), name='movie-update'),
    url(r'^movies/create/$', login_required(views.MovieCreateView.as_view()), name='movie-create'),

    url(r'^directors/$', views.DirectorIndexView.as_view(), name='director-index'),
    url(r'^directors/(?P<pk>[0-9]+)/$', views.DirectorDetailView.as_view(), name='director-detail'),
    url(r'^directors/(?P<pk>[0-9]+)/edit/$', views.DirectorUpdateView.as_view(), name='director-update'),
    url(r'^directors/create/$', login_required(views.DirectorCreateView.as_view()), name='director-create'),

    url(r'^accounts/login/$', auth_views.LoginView.as_view()),
]
