from django.db import models

class Priority(models.TextChoices):
    LOW = 'low', 'Low'
    MEDIUM = 'medium', 'Medium'
    HIGH = 'high', 'High'


class Status(models.TextChoices):
    TODO = 'todo', 'To Do'
    IN_PROGRESS = 'in_progress', 'In Progress'
    DONE = 'done', 'Done'
