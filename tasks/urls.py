from django.conf.urls import patterns, include, url
from django.contrib import admin
from tasks import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name="detail"),
	url(r'^add/$', views.TaskCreateView.as_view(), name="add"),
	url(r'^edit/(?P<pk>\d+)/$', views.TaskUpdateView.as_view(), name="edit"),
	url(r'^remove/(?P<pk>\d+)/$', views.TaskDeleteView.as_view(), name="remove"),
	url(r'^(?P<pk>\d+)/add_subtask$', views.SubtaskCreateView.as_view(), name='add-subtask'),
	url(r'^edit_subtask/(?P<pk>\d+)/$', views.SubtaskUpdateView.as_view(), name="edit_subtask"),
   url(r'^remove_subtask/(?P<pk>\d+)/$', views.SubtaskDeleteView.as_view(), name="remove_subtask"),


					   )

