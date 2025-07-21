from django.urls import path, include

urlpatterns = [
    path('first_app/', include('src.firstapp.urls')),
    path('taskmanager/', include('src.taskmanager.urls'))
]