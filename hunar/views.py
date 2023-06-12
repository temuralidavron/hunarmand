from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from rest_framework import generics, status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .forms import Anketaform, Markanketaform
from .models import Anketa, User, MarkAnketa








#
# class UserView(TemplateView):
#     queryset = User.objects.all()
#     template_name = "base.html"
#     def get_userview(self, request):
#         user = User.objects.all()
#         context = {
#             'login':user.login,
#             'parol' : user.parol,
#         }
#         return render(request, 'kengash.html', {'form':context})



# class UserPostview(TemplateView):
#     model = User
#     queryset = User.objects.all()
#     succsess_url = reverse_lazy('markanketapostview')
#     def post(self, request, *args, **kwargs):
#
#         data=request.POST
#         userpost =User.objects.create(
#             username = data['username'],
#             password = data['password'],
#
#         )
#         return render(request, 'kengash.html',{'form': userpost })




#
#
#
# class AnketaGetView(TemplateView):
#     form_class = Anketaform
#     model = Anketa
#     success_url = reverse_lazy('anketaview')
#     def get_index(self ,request ):
#         form = Anketaform
#         anketa = Anketa.objects.all()
#         context = {
#             'anketa':anketa,
#
#
#         }
#         return render(request, 'kengash.html',{'form': context })







#
# class MarkAnketaView(TemplateView):
#     queryset = MarkAnketa.objects.all()
#     model = MarkAnketa
#     form_class = Markanketaform
#     def get_index(self,request):
#         form = Markanketaform
#         markanketa = MarkAnketa.objects.all()
#         context = {
#             'markanketa':markanketa,
#         }
#         return render(request, 'kengash.html', {'form':form })


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



    # def post(request):
    #     submitted = False
    #     if request.method =='POST':
    #         form = Anketaform(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect('/markanketaview?submitted=True')
    #     else:
    #         form = Anketaform
    #         if 'submitted' in request.GET:
    #             submitted  = True
    #     return render(request,'anketa/kengash.html', {'form':form, 'submitted':submitted})

# class MarkView(TemplateView):
#     template_name = 'kengash.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs('like','dislike') = "bar"
#         return kwargs
#         kwargs = super(MarkView, self).get_context_data(**kwargs)
#
#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         bar = self.request.POST.get('like', 'dislike')
#         if bar: self.template_name = 'kengash.html'
#         previous_like = context['like', 'dislike']
#         context['new_variable'] = 'new_variable' + ' updated'
#
#         return self.render_to_response(context)




# class Anketaview(TemplateView):
#     queryset = Anketa.objects.all()
#     template_name = "anketa.html"
#     def get_anketa(self,request):
#         anketa = Anketa.objects.all()
#         return render(request,"anketa.html",{'anketa':anketa})


#



class MarkanketaView(TemplateView):
    template_name = 'kengash.html'
    def post(self, request, *args, **kwargs):
        data = request.POST
        form = Markanketaform
        markanketapost = MarkAnketa.objects.create(
            like=data['like'],
            dislike=data['dislike'],
        )
        return render(markanketapost,'kengash.html', {'form':form})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_anonymous:
            return data
        reactions = MarkAnketa.objects.filter(anketa=self.get_object())
        data['reaction_value'] = reactions.filter(user=self.request.user).first()
        data['likes_count'] = reactions.filter(value=1).count()
        return data


class AnketaView(CreateView):
    queryset = Anketa.objects.all()
    def get(self, request, *args, **kwargs):
        form = Anketaform
        context = {
            'form':form
        }
        return render(request, 'anketa.html', context)

    def post(self, request, *args, **kwargs):
        # form = Anketaform(request.POST)
        # if form.is_valid():
        #     print('sdsdsdsdsdsd')
        #     form.save()
        print("dfdfdf")

        if request.method == "POST":
            print(request.POST)
            name = request.POST['uz_listing_firstname_name_field'],
            print('name',name)
            fname = request.POST['uz_listing_lastname_text_field'],
            print('fname', fname)
            lname = request.POST['uz_listing_otch_text_field'],
            print('lname',lname)
            koyadress = request.POST['uz_listing_tgmanzil_field'],
            print('koyadrres',koyadress)
            state = request.POST['uz_listing_fuqoroligi'],
            print('state',state)
            password = request.POST['uz_listing_passport_field'][0],
            print('password', password)
            passwordpnfl = request.POST['uz_listing_passport_field'][1],
            print('passwordpnfl', passwordpnfl)
            malumot = request.POST['uz_listing_malumoti_field'],
            print('malumot',malumot)
            adress = request.POST['uz_listing_yshmanzil_field'],
            print('adress', adress)
            workadress = request.POST['uz_listing_flmanzil_field'],
            print('workadress',workadress)
            number = request.POST['uz_listing_phone_field'],
            print('number',number)
            email =request.POST['uz_listing_mail_field'],
            print('email', email)
            web_chart = request.POST['uz_listing_site_field'],
            print('web_chart', web_chart)
            studentcount = request.POST['uz_listing_shogirdlar_field'],
            print('studentcount', studentcount)
            job = request.POST['typetaxonomy'],
            print('job', job)
            grift = request.POST['type_unvoni_field'],
            print('grift', grift)
            memberyear = request.POST['uz_listing_azo_field'],
            print('memberyear', memberyear)
            award = request.POST['uz_listing_mukofot_field'],
            print('award', award)
            festival = request.POST['uz_listing_korgazma_field'],
            print('festival',festival)
            nationalfest = request.POST['uz_listing_hkorgazma_field'],
            print('nationalfest', nationalfest)
            owngalery = request.POST['uz_listing_shkorgazma_field'],
            print('owngalery', owngalery)
            teacherabout= request.POST['uz_listing_sulola_field'],
            print('teacherabout', teacherabout)
            orginalwork= request.POST['uz_listing_ijod_field'],
            print('orginalwork', orginalwork)
            modepraduct =request.POST['uz_listing_ishmahsulot_field'],
            print('modepraduct', modepraduct)
            addinform = request.POST['uz_listing_qoshimcha_malumotlar_field'],
            print('addinform', addinform)
            photos = request.POST['my_file_upload_nonce'],
            print('photos', photos)
            anketa = Anketa.objects.create(
                name=name,
                fname=fname,
                lname=lname,
                koyadress=koyadress,
                state=state,
                password=password,
                passwordpnfl=passwordpnfl,
                malumot=malumot,
                adress=adress,
                workadress=workadress,
                number=number,
                email=email,
                web_chart=web_chart,
                studentcount=studentcount,
                job=job,
                grift=grift,
                memberyear=memberyear,
                award=award,
                festival=festival,
                nationalfest=nationalfest,
                owngalery=owngalery,
                teacherabout=teacherabout,
                orginalwork=orginalwork,
                modepraduct=modepraduct,
                addinform=addinform,
                photos=photos,
            )
            anketa.save()  # save to database
        return redirect("anketapostview")




class AnketaGetingView(TemplateView):
    model = Anketa
    template_name = 'kengash.html'
    form = Anketaform
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["anketa_list"] = Anketa.objects.all()
        return context


























#
#
# class MarkAnketaPostView(TemplateView):
#     queryset = MarkAnketa.objects.all()
#     serializer_class = MarkAnketaSerializer
#
#     def post(self, request, *args, **kwargs):
#         data = request.POST
#         markanketapost = MarkAnketa.objects.create(
#             mark=data['mark'],
#
#         )
#         return Response(status=status.HTTP_201_CREATED)
#
#
#
#
# class UserPostView(TemplateView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#         data = request.POST
#         userpost = User.objects.create(
#             username=data['username'],
#             password=data['password'],
#
#         )
#         return Response(status=status.HTTP_201_CREATED)
#
#
#
#
#
#
# class LikeClass(TemplateView):






    # status =MarkAnketa(**kwargs['status'])


    # def post(self, request, *args, **kwargs):
    #     likestatus = kwargs['status']
    #     if likestatus is True:
    #         queryset = MarkAnketa.objects.all()
    #         likestatus += 1
    #     else:
    #         likestatus=None
    #
    #
    #     return Response(status=status.HTTP_201_CREATED)



#
# class AnketaView(TemplateView):
#     queryset = Anketa.objects.all()
#
#     template_name = "anketa.html"
#
#     def anketa_create(request):
#         queryset = Anketa.objects.filter(id=id)
#
#         form = Anketaform
#         if request.method=='POST':
#            form = Anketaform(data=request.POST)
#            if form.is_valid():
#                anketa = form.save(commit=True)
#                return redirect(anketa,'anketa.html', {'form':form})
#            else:
#                return render(request,'base.html', {'form':form})
#         else:
#            return render(request, 'base.html', {'form': form})





#
# def homeview(request,id):
#     queryset = Anketa.objects.all().order_by('-date')
#
#     context = {
#
#
#
#     }
#     return render(request, 'base.html', context)