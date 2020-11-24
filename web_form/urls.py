from django.urls import path

from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.list_forms, name='list_forms'),
    path('form_create/', views.form_create, name='form_create'),
    path('<int:form_id>/', views.form, name='form'),
]

