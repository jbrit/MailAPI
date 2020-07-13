from django.contrib import admin
from django.urls import path
from core.views import login_view, logout_view, home, EmailList, EmailDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', home, name="home"),
    path('api/emails/', EmailList.as_view() ),
    path('api/emails/<int:pk>', EmailDelete.as_view() ),
]
