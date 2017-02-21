from django.conf.urls import patterns, include, url
from django.contrib import admin
from task_list import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^tasks/', include('tasks.urls', namespace="tasks")),
    # url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="detail"),
    # url(r'^add/$', views.CourseCreateView.as_view(), name="add"),
	# url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name="edit"),
	# url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name="remove"),
	# url(r'^(?P<pk>\d+)/add_subtask$', views.SubtaskCreateView.as_view(), name='add-subtask'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
