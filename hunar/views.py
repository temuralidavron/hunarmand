from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, DetailView, CreateView
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .forms import Anketaform, Markanketaform
from .models import Anketa, User, MarkAnketa

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from db_client import execute

#Jo&#039;natish
class AnketaView(generic.CreateView):
    template_name = 'anketa.html'
    form_class = Anketaform
    queryset = Anketa.objects.all()
    success_url = reverse_lazy("anketapostview")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Anketaform
        context['ankita'] = Anketa.objects.get(id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = Anketaform(request.POST)
        file = request.FILES
        print(file)
        print(form.data)
        ankita = Anketa.objects.get(id=self.kwargs['id'])
        ankita.photo = file['photo']
        ankita.birth_place = form.data['birth_place']
        ankita.malumot =form.data['malumot']
        ankita.workadress = form.data['workadress']
        ankita.mob_phone_no = form.data['mob_phone_no']
        ankita.web_chart=form.data['web_chart']
        ankita.studentcount=form.data['studentcount']
        ankita.job = form.data['job']
        ankita.grift=form.data['grift']
        ankita.memberyear = form.data['memberyear']
        ankita.award = form.data['award']
        ankita.festival = form.data['festival']
        ankita.nationalfest = form.data['nationalfest']
        ankita.owngalery = form.data['owngalery']
        ankita.teacherabout = form.data['teacherabout']
        ankita.orginalwork = form.data['orginalwork']
        ankita.modepraduct = form.data['modepraduct']
        ankita.addinform = form.data['addinform']
        ankita.photos = file['photos']
        ankita.save()
        return redirect('data_item', ankita.pk)




@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sample(request):


    a = execute("Select  a.id,a.photo, a.name, a.name, a.lname  FROM hunar_anketa a LEFT OUTER  JOIN hunar_markanketa m ON a.id=m.anketa_id;")

    print(f"\n\n\n\n{a}\n\n\n")
    return JsonResponse({'foo': a})


class AnketaGetingView(TemplateView):
    model = Anketa
    template_name = 'anketa.html'
    form = Anketaform
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["anketa_like"] = Anketa.objects.filter(likes=request.user)
        context["anketa_dislike"] = Anketa.objects.filter(dislike=request.user)
        print(Anketa.objects.filter(likes=request.user))
        print(Anketa.objects.filter(dislike=request.user))
        print(Anketa.objects.filter(dislike=request.user))
        # context["anketa_none"] = Anketa.objects.filter(user=request.user, like='dislike')
        return context


class InetgerView(generic.CreateView):
    queryset = Anketa.objects.all()
    template_name = 'integratsiya.html'
    form_class = Anketaform

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(form)
        ankita = Anketa.objects.create(
            tin = form['tin'],
            pin=form['pin'],
            # ctzn=form["O'zbekiston"],
            pport_no =form['pport_no'],
            per_id='pop tuman',
            first_name = 'salomat',
            mid_name = 'Valomat',
            sur_name = 'balakala',
            email = '@gmail.com',
            mob_phone_no = '17536717',
        )
        return redirect('anketaview', ankita.pk)


class DataItemView(TemplateView):
    queryset = Anketa.objects.all()
    template_name = 'data_item.html'
    form_class = Anketaform
    def get(self, request, *args, **kwargs):
        item = Anketa.objects.get(id=self.kwargs['id'])
        context = {
            'item': item
        }
        return render(request, 'data_item.html', context)


class AnketaEditView(generic.CreateView):
    template_name = 'edit.html'
    form_class = Anketaform
    queryset = Anketa.objects.all()
    # success_url = reverse_lazy("anketapostview")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Anketaform
        context['ankita'] = Anketa.objects.get(id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = Anketaform(request.POST)
        file = request.FILES
        print(file)
        print(form.data)
        ankita = Anketa.objects.get(id=self.kwargs['id'])
        ankita.photo = file['photo']
        ankita.birth_place = form.data['birth_place']
        ankita.malumot = form.data['malumot']
        ankita.workadress = form.data['workadress']
        ankita.mob_phone_no = form.data['mob_phone_no']
        ankita.web_chart = form.data['web_chart']
        ankita.studentcount = form.data['studentcount']
        ankita.job = form.data['job']
        ankita.grift = form.data['grift']
        ankita.memberyear = form.data['memberyear']
        ankita.award = form.data['award']
        ankita.festival = form.data['festival']
        ankita.nationalfest = form.data['nationalfest']
        ankita.owngalery = form.data['owngalery']
        ankita.teacherabout = form.data['teacherabout']
        ankita.orginalwork = form.data['orginalwork']
        ankita.modepraduct = form.data['modepraduct']
        ankita.addinform = form.data['addinform']
        ankita.photos = file['photos']
        ankita.status = True
        ankita.save()
        return redirect('data_item', ankita.pk)

class TasdiqlashEditView(generic.CreateView):
    template_name = 'edit.html'
    form_class = Anketaform
    queryset = Anketa.objects.all()
    # success_url = reverse_lazy("anketapostview")

    def post(self, request, *args, **kwargs):
        ankita = Anketa.objects.get(id=self.kwargs['id'])
        ankita.status = True
        ankita.save()
        return redirect('data_item', ankita.pk)


class HomeListView(TemplateView):
    queryset = Anketa.objects.all()
    template_name = 'home.html'
    form_class = Anketaform

    def get(self, request, *args, **kwargs):
        item = Anketa.objects.filter(status=True)
        context = {
            'items': item
        }
        return render(request, 'home.html', context)


class KengashView(generic.CreateView):
    queryset = Anketa.objects.all()
    template_name = 'kengash.html'
    form_class = Anketaform

    def get(self, request, *args, **kwargs):
        print( Anketa.objects.filter(status=True))

        context = {
            'ankita': Anketa.objects.filter(status=True)
        }
        return render(request, 'kengash.html', context)

    def post(self, request, *args, **kwargs):
        ankita = Anketa.objects.get(id=request.GET.get('id'))
        if request.GET.get('like') == 'yes':
            ankita.likes.add(User.objects.get(id=request.user.pk))
            ankita.save()
        elif request.GET.get('like') == 'no':
            ankita.dislike.add(User.objects.get(id=request.user.pk))
            ankita.save()

        return redirect('kengashview')

class ConfirmView(generic.CreateView):
    queryset = Anketa.objects.all()
    template_name = 'confirmation.html'
    form_class = Anketaform


    def get(self, request, *args, **kwargs):
        like =Anketa.objects.filter(likes=request.user, status=True)
        context = {
            'likes': like,

        }
        return render(request, 'confirmation.html', context)

    def post(self, request, *args, **kwargs):
        ankita = Anketa.objects.get(id=request.GET.get('id'))
        ankita.likes.add(User.objects.get(id=request.user.pk))
        ankita.save()
        return redirect('kengashview')



class RejectionView(generic.CreateView):
    queryset = Anketa.objects.all()
    template_name = 'rejection.html'
    form_class = Anketaform

    def get(self, request, *args, **kwargs):
        dislike = Anketa.objects.filter(dislike=request.user, status=True)
        print(dislike)
        context = {

            'dislikes': dislike,
        }
        return render(request, 'rejection.html', context)

    def post(self, request, *args, **kwargs):
        ankita = Anketa.objects.get(id=request.GET.get('id'))
        ankita.dislike.add(User.objects.get(id=request.user.pk))
        ankita.save()

        return redirect('kengashview')







