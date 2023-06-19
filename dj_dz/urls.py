from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dj_dz import settings
from posts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('categories/', categories_view),
    path('products/<int:pk>/', product_detail)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
