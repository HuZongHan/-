from django.conf.urls import url

from lianxi import views

urlpatterns = [
    url(r'tologin/', views.tologin),
    url(r'login/', views.login, name='login'),
    url(r'welcome/', views.welcome, name='welcome'),
    url(r'logout/',views.logout,name='logout')
]
