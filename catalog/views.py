from .models import Animal
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'catalog/index.html')


class AnimalDetailView(LoginRequiredMixin, generic.ListView):
    model = Animal


class AnimalCreate(CreateView):
    model = Animal
    fields = ['animal_name', 'animal_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('animal_image_list'))


class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['animal_name', 'animal_image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('animal_list'))


def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    messages.success(request, (animal.animal_name + " has been deleted"))
    return redirect('animal_list')


def animal_image_list(request):
    animals = Animal.objects.exclude(animal_image='').order_by('animal_name').select_related('user')
    return render(request, 'catalog/animal_image_list.html', {'animals': animals})


class AnimalListView(LoginRequiredMixin, generic.ListView):
    model = Animal
    template_name = 'catalog/animal_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Animal.objects.filter(user=self.request.user)


