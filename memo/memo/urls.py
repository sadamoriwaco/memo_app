from django.contrib import admin
from django.urls import path,include
# import memo.views as memo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memo/', include('memo_app.urls')),
]
