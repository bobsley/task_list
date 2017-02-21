from django.db import models

class Task(models.Model):
    description = models.TextField(max_length=100)

class Subtask(models.Model):
    description = models.TextField(max_length=100)
    task = models.ForeignKey(Task)
    # def __unicode__(self):
		# return self.description