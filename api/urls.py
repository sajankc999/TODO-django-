from .views import *
from django.urls import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('todo',TodoView,basename='Todo')
urlpatterns = [
    path('login/',loginViewset.as_view()),
    path('register/',RegisterView.as_view()),
    
]+router.urls
