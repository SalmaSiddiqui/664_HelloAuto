from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from autos.models import Auto, Comment
from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path, reverse_lazy
from autos.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


from autos.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from autos.forms import CreateForm

class AutoListView(OwnerListView):
    model = Auto
    template_name = "auto_list.html"

    # def get(self, request) :
    #     ad_list = Auto.objects.all()
    #     favorites = list()
    #     if request.user.is_authenticated:
    #         # rows = [{'id': 2}]  (A list of rows)
    #         # rows = request.user.favorite_things.values('id') #not sure where favorite_things is coming from
    #         rows = request.user.favorite_autos.values('id')
    #         favorites = [ row['id'] for row in rows ]
    #     ctx = {'ad_list' : ad_list, 'favorites': favorites}
    #     return render(request, self.template_name, ctx)

class AutoDetailView(OwnerDetailView):
    model = Auto
    template_name = "auto_detail.html"

    def get(self, request, pk) :
        auto = Auto.objects.get(id=pk)
        comments = Comment.objects.filter(auto=auto).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)



class AutoDeleteView(OwnerDeleteView):
    model = Auto
    template_name = "auto_delete.html"

class AutoFormView(LoginRequiredMixin, View):
    template = 'auto_form.html'
    success_url = reverse_lazy('auto')

    def get(self, request, pk=None):
        if pk:
            auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = CreateForm(instance=auto)
            ctx = { 'form': form }
            return render(request, self.template, ctx)
        else:
            form = CreateForm()
            ctx = { 'form': form }
            return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if pk:
            auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=auto)

            if not form.is_valid() :
                ctx = {'form' : form}
                return render(request, self.template, ctx)

            auto.save()
            return redirect(self.success_url)
        else:
             form = CreateForm(request.POST, request.FILES or None)

             if not form.is_valid() :
                 ctx = {'form' : form}
                 return render(request, self.template, ctx)

             auto = form.save(commit=False)
             auto.owner = self.request.user
             auto.save()
             return redirect(self.success_url)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Auto, id=pk)
        comment_form = CommentForm(request.POST)
        comment = Comment(text=request.POST['comment'], owner=request.user, auto=f)
        comment.save()
        return redirect(reverse_lazy('auto_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "comment_delete.html"
    # template_name = "auto_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])
