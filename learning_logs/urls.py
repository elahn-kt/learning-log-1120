

"""Defines URL patterns for learning_logs."""

#from django.conf.urls import url
from django.urls import path
from . import views
#from django.contrib import admin
#from django.urls import path
from django.urls import re_path


#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
    # Home page
#    url('$', views.index, name='index'),
    path(r'', views.index, name='index'),

    # Show all topics.
    path(r'topics/', views.topics, name='topics'),

    # Detail page for a single topic
 #   path(r'topics/<topic_id>/', views.topic, name='topic'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    # Page for adding a new topic
    path(r'new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
#    path(r'new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    re_path(r'new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    
    # Page for editing an entry
#    path(r'edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
    re_path(r'edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]