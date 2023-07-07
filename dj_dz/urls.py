from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dj_dz import settings
from posts.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('categories/', CategoriesCBV.as_view()),
    path('products/<int:pk>/', ProductDetailCBV.as_view()),
    path('products/create/', ProductCreateCBV.as_view()),
    path('categories/create/', CategoriesCreateCBV.as_view()),
    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
