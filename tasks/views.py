from rest_framework import generics, permissions
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from tasks.models import Task, User, Priority
from tasks.serializers import TaskSerializer, RegisterSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskGetUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = RegisterSerializer


# Html rendering view
@login_required
def cute_task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(
                title=title,
                user=request.user,
                priority=Priority.MEDIUM
            )
            return redirect('cute_task_list')

    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def cute_task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "update":
            title = request.POST.get("title")
            description = request.POST.get("description", "")
            priority = request.POST.get("priority", Priority.MEDIUM)
            status = request.POST.get("status", task.status)
            due_date = request.POST.get("due_date") or None
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            task.due_date = due_date
            task.save()
            return redirect('cute_task_detail', pk=task.pk)
        elif action == "delete":
            task.delete()
            return redirect('cute_task_list')

    return render(request, "tasks/task_detail.html", {"task": task, "priorities": Priority.choices})
