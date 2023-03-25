
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    # path('StudentApi/',views.List_Create_Api.as_view(), name='api1'),
    # path('StudentApi/<int:pk>/', views.Retrieve_Update_Destroy.as_view(), name='api2')
]
