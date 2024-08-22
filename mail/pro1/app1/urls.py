from django.urls import path
from .views import mail_view


urlpatterns = [
	path('mv/', mail_view),
]
