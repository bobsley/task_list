# -*- coding: utf-8 -*-
from django import forms
from tasks.models import Task, Subtask

class TaskModelForm(forms.ModelForm):
	class Meta:
		model = Task
	fields = ['description']

class SubtaskModelForm(forms.ModelForm):
	class Meta:
		model = Subtask
	fields = ['description']
