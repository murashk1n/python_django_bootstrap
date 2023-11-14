from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

# from cities.forms import TrainForm
from trains.models import Train

__all__ = (
    'home', 'TrainListView'
    # 'TrainDetailView', 'TrainCreateView',
    # 'TrainUpdateView', 'TrainDeleteView',
)


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'cities/home.html', context)


class TrainListView(ListView):
    paginate_by = 2
    model = Train
    template_name = 'trains/home.html'

# class TrainDetailView(DetailView):
#     queryset = Train.objects.all()
#     template_name = 'cities/detail.html'
#
#
# class TrainCreateView(SuccessMessageMixin, CreateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'cities/create.html'
#     success_url = reverse_lazy('cities:home')
#     success_message = "Train was created successfully"
#
#
# class TrainUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'cities/update.html'
#     success_url = reverse_lazy('cities:home')
#     success_message = "Train was updated successfully"
#
#
# class TrainDeleteView(DeleteView):
#     model = Train
#     # template_name = 'cities/delete.html'
#     success_url = reverse_lazy('cities:home')
#
#     def get(self, request, *args, **kwargs):
#         messages.success(request, 'Train was deleted successfully')
#         return self.post(request, *args, **kwargs)
