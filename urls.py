from django.contrib import admin
from django.urls import path
from sixth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/' , views.book_view)
]
