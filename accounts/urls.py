from django.urls import include, path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name="logout")
]
