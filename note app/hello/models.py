from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    # def get_context_data(se3lf, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     context['count'] = context['tasks'].filter(complete=False).count()

    
    # def __str__(self):
    #     return self.title
    
    class Meta:
        ordering = ['complete']


