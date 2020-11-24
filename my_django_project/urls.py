from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web_form.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
]
