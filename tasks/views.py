from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Task, Subtask
from tasks.forms import TaskModelForm, SubtaskModelForm


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/add.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['title'] = "Task creation"
        return context

    def form_valid(self, form):
        message = super(TaskCreateView, self).form_valid(form)
        mes = "Task has been successfully added."
        messages.success(self.request, mes)
        return message

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/edit.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Task update"
        return context

    # def get_success_url(self):
    #     return reverse_lazy('tasks:edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        message = super(TaskUpdateView, self).form_valid(form)
        mes = "The changes have been saved."
        messages.success(self.request, mes)
        return super(TaskUpdateView, self).form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/remove.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Task deletion."
        return context

    def delete(self, request, *args, **kwargs):
        ret_msg = super(TaskDeleteView, self).delete(request, *args, **kwargs)
        mes = "Task has been deleted."
        messages.success(self.request, mes)
        return ret_msg

class SubtaskCreateView(CreateView):
    model = Subtask
    template_name = "tasks/add_subtask.html"

    def form_valid(self, form):
        message = super(SubtaskCreateView, self).form_valid(form)
        mes = "Subtask has been successfully added."
        messages.success(self.request, mes)
        return message

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={'pk': self.object.task.pk})

    def get_initial(self):
        return {'task': self.kwargs['pk']}

class SubtaskUpdateView(UpdateView):
    model = Subtask
    template_name = "tasks/edit_subtask.html"

    def get_context_data(self, **kwargs):
        context = super(SubtaskUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Subtask update"
        return context

    # def get_success_url(self):
    #     return reverse_lazy('tasks:edit', kwargs={'pk': self.object.pk})

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={'pk': self.object.task.pk})

    def form_valid(self, form):
        message = super(SubtaskUpdateView, self).form_valid(form)
        mes = "The changes have been saved."
        messages.success(self.request, mes)
        return super(SubtaskUpdateView, self).form_valid(form)

class SubtaskDeleteView(DeleteView):
    model = Subtask
    template_name = "tasks/remove_subtask.html"

    def get_context_data(self, **kwargs):
        context = super(SubtaskDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Subtask deletion."
        return context

    def delete(self, request, *args, **kwargs):
        ret_msg = super(SubtaskDeleteView, self).delete(request, *args, **kwargs)
        mes = "Subtask has been deleted."
        messages.success(self.request, mes)
        return ret_msg

    def get_success_url(self):
        return reverse_lazy('tasks:detail', kwargs={'pk': self.object.task.pk})