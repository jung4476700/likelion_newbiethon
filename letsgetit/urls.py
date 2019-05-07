"""letsgetit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import polls.views
import main.views
import free.views
import login.views
import apply.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', apply.views.applying, name="applying"),
    path('apply/<int:apply_id>', apply.views.apply_detail, name="apply_detail"),
    path('apply/apply_new', apply.views.apply_new, name='apply_new'),
    path('apply/apply_create', apply.views.apply_create, name='apply_create'),
    path('free/free_new', free.views.free_new, name='free_new'),
    path('free/free_create', free.views.free_create, name='free_create'),
    path('polls/polls_new', polls.views.polls_new, name='polls_new'),
    path('polls/polls_create', polls.views.polls_create, name='polls_create'),
    path('polls/', polls.views.ranking, name="ranking"),
    path('polls/<int:score_id>', polls.views.rank_detail, name="rank_detail"),
    path('', main.views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('free/', free.views.free, name="free"),
    path('free/<int:content_id>', free.views.free_detail, name="free_detail"),
    path('login/', login.views.login, name="login"),
    path('signup/', login.views.signup, name="signup"),
    path('logout/', login.views.logout, name='logout'),
]
