from django.urls import path
from .views import home, ProjectListView, ProjectDetailView, education, contacts

app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('education/', education, name='education'),
    path('portfolio/', ProjectListView.as_view(), name='projects'),
    path('portfolio/<int:pk>/', ProjectDetailView.as_view(), name='project'),

]