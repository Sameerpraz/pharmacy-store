from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('src.store.urls')),
    path('api/gettoken/',TokenObtainPairView.as_view(), name="get_token"),
    path('api/refreshtoken/',TokenRefreshView.as_view(), name="refresh_token"),
]
