from .models import Student, Homework

from django.views.generic.edit import CreateView

class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_form.html'
    fields = ['commit_date','headline','attach','remark', 'student']