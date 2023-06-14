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


class MarkanketaGetPostView(TemplateView):
    model = MarkAnketa
    form_class  = Markanketaform
    queryset = MarkAnketa.objects.all()

    def post(self, request, *args, **kwargs):
        data=request.POST
        markanketapost = MarkAnketa.objects.create(
            like = data['like'],
            dislike = data['dislike'],

        )
        return render(request, 'kengash.html', {'markanketapost': markanketapost}, status=status.HTTP_201_CREATED)


class AnketaViewGet(TemplateView):
    model =Anketa
    form_class = Anketaform
    template_name = 'kengash.html'
    queryset = Anketa.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["anketa_list"] = Anketa.objects.all()
        return context







class AnketaPostView(TemplateView):
    queryset = Anketa.objects.all()
    success_url = reverse_lazy('markanketaview')
    template_name = "anketa.html"


    def post(self, request, *args, **kwargs):
        data = request.POST
        anketapost = Anketa.objects.create(
            rasmingizniyuklang=data['photo'],
            ism=data['name'],
            familiya=data['fname'],
            otasiningismi =data['lname'],
            tugulginvaqtjoy=data['koyadress'],
            fuqoroligi=data['state'],
            password= data['password'],
            passwordpnfl=data['passwordpnfl'],
            malumot=data['malumot'],
            adress=data['adress'],
            workadress=data['workadress'],
            number= data['number'],
            emial=data['email'],
            web_sahifa= data['web_chart'],
            shogirdlar= data['studentcount'],
            job= data['job'],
            mukofot= data['grift'],
            uyushmagaazolik= data['memberyear'],
            mukofothorijiy=data['award'],
            yutuqlar= data['festival'],
            horijdayutuq= data['nationalfest'],
            shaxsiyyutuq= data['owngalery'],
            ustozi= data['teacherabout'],
            ishjoyi=data['orginalwork'],
            mahsuloti= data['modepraduct'],
            qoshimcha= data['addinform'],
            rasm= data['photos'],
            # anketa=data ['anketa'],

            )
        return reverse_lazy('markanketaview')



class AnketaGetPostView(TemplateView):
    template_name = 'anketa.html'




def createMark(request):
    form =Markanketaform
    if request.method == 'POST':
        form=Anketaform(request.POST)
        if form.is_valid():
            form.is_valid()
            return redirect('/')



    context = {'form':form}
    return render(request,'kengash.hmtl', context)




class MarkanketaView(TemplateView):
    template_name = 'kengash.html'
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data = request.POST
        form = Markanketaform
        markanketapost = MarkAnketa.objects.create(
            like=data['like'],
            dislike=data['dislike'],
            anketa_id=data['id'],
            user=request.user
        )

        return render(markanketapost,'kengash.html', {'form':form})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user:
            return data
        reactions = MarkAnketa.objects.filter(anketa=self.get_object())
        data['reaction_value'] = reactions.filter(user=self.request.user).first()
        data['likes_count'] = reactions.filter(value=1).count()

        return data


class AnketaView(generic.CreateView):
    template_name = 'anketa.html'
    form_class = Anketaform
    queryset = Anketa.objects.all()
    success_url = reverse_lazy("anketapostview")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Anketaform
        return context

    def post(self, request, *args, **kwargs):
        form = Anketaform(request.POST)
        file = request.FILES
        print(file)
        anketa = Anketa.objects.create(
            photo=file['photo'],
            name=form.data['name'],
            fname=form.data['fname'],
            lname=form.data['lname'],
            koyadress=form.data['koyadress'],
            state=form.data['state'],
            password=form.data['password'],
            passwordpnfl=form.data['passwordpnfl'],
            malumot=form.data['malumot'],
            adress=form.data['adress'],
            workadress=form.data['workadress'],
            number=form.data['number'],
            email=form.data['email'],
            web_chart=form.data['web_chart'],
            studentcount=form.data['studentcount'],
            job=form.data['job'],
            grift=form.data['grift'],
            memberyear=form.data['memberyear'],
            award=form.data['award'],
            festival=form.data['festival'],
            nationalfest=form.data['nationalfest'],
            owngalery=form.data['owngalery'],
            teacherabout=form.data['teacherabout'],
            orginalwork=form.data['orginalwork'],
            modepraduct=form.data['modepraduct'],
            addinform=form.data['addinform'],
            photos=file['photos'],
        )
        return render(request, 'list.html',{'form':form})




def like_detail(request):
    markanketa = MarkAnketa.objects.get(like=like)
    permission_classes = [is_Authenticated]
    msg = False




    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user

            if markanketa.like.filter(id=user.id).exist():
                markanketa.like.remove(user)
                msg = False
            else:
                markanketa.like.add(user)
                msg = True
    return render(request, 'kengash.html', {'msg':msg })

#{{ markanketa.like.count}}


def like(request,anketa_id):
    user = request.user
    anketa = Anketa.objects.get(id=anketa_id)
    current_like = anketa.like
    liked = MarkAnketa.objects.filter(user=request.user, anketa=anketa).count()
    if not liked:
        liked = MarkAnketa.objects.create(user=user, anketa=anketa)
        current_like = current_like+ 1




class AnketaGetingView(TemplateView):
    model = Anketa
    template_name = 'kengash.html'
    form = Anketaform
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["anketa_list"] = Anketa.objects.all()
        return context


def like_post(request):
    anketa = get_object_or_404(MarkAnketa,id=request.POST.get(like_id))
    is_liked = False
    if anketa.like.filter(id=request.user.id).exist():
        anketa.like.remove(request.user)
        is_liked = False
    else:
        anketa.like.add(request.user)
        is_liked = True
    return HttpResponseRedirect(anketa.get_absolute_url())


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def sample(request):


    a = execute("Select a.id, a.name FROM hunar_anketa a LEFT OUTER  JOIN hunar_markanketa m ON a.id=m.anketa_id;")

    print(f"\n\n\n\n{a}\n\n\n")
    return JsonResponse({'foo': a})

    anketa = get_object_or_404(MarkAnketa,id=request.POST.get(like_id))
    is_liked = False
    if anketa.like.filter(id=request.user.id).exist():
        anketa.like.remove(request.user)
        is_liked = False
    else:
        anketa.like.add(request.user)
        is_liked = True
    return HttpResponseRedirect(anketa.get_absolute_url())




