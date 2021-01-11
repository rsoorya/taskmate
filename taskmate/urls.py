from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todolist_views

urlpatterns = [
    path('', todolist_views.index,name="index"),
    path('admin/', admin.site.urls),
    path('todolist/',include('todolist_app.urls')),
    path('contact', todolist_views.contact,name='contact'),
    path('about', todolist_views.about,name='about'),
    path('account/', include('users_app.urls')),
]
