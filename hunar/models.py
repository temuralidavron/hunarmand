from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.text import slugify
# Create your models here.



class User(AbstractUser):
    nickname=models.CharField(max_length=50,blank=True,null=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'










class Anketa(models.Model):
    STATE =(
        ("O'zbekiston", "O'ZBEKISTON"),
        ("Avg'oniston", "Avg'oniston"),
        ("Eron", "ERON"),
        ("Ozarbayjon", "OZARBAYJON"),
        ("Qirg'iziston", "QIRG'IZISTON"),
        ("Qozaeg'iston","QOZOG'ISTON"),
        ("Rossiya","ROSSIYA"),
        ("Tojikiston","TOJIKISTON"),
        ("Turkiya","TURKIYA"),
        ("Turkmaniston","TURKMANISTON"),

    )
    JOB = (

        ("Bosh kiyimlar tayyorlash", "bosh_kiyimlar_tayyorlash"),
        ("Charm mahsulotlari", "charm mahsulotlari"),
        ("Chinni, fayans va sopol buyumlari", "chinni, fayans va sopol buyumlari"),
        ("Emallash ishlari", "emallash ishlari"),
        ("Esdalik buyumlari", "esdalik buyumlari"),
        ("Ganch o'ymakorligi", "ganch o'ymakorligi"),
        ("Gul bosilgan gazlamalar va chokli buyumlar","gul bosilgan gazlamalar va chokli buyumlar"),
        ("Hajmli va shaklli qoliplarda quyilgan buyumla", "hajmli va shaklli qoliplarda quyilgan buyumlar"),
        ("Kandakorlik, misgarlik buyumlari", "kandakorlik, misgarlik buyumlari"),
        ("Kashtachilik", "kashtachilik"),
        ("Ko'zgu tayyorlash", "ko'zgu tayyorlash"),
        ("Mayda haykaltaroshlik buyumlari", "mayda haykaltaroshlik buyumlari"),
        ("Metalldan yasalgan buyumlar", "metalldan yasalgan buyumlar"),
        ("Milliy liboslar tayyorlash", "milliy liboslar tayyorlash"),
        ("Milliy poyabzal tayyorlash", "milliy poyabzal tayyorlash"),
        ("Miniatyura, rang tasvir, naqqoshlik va bo'yoqli naqshlar", "miniatyura, rang tasvir, naqqoshlik va bo'yoqli naqshlar"),
        ("Mozaika ishlari", "mozaika ishlari"),
        ("Mualliflik mebellarini tayyorlash", "mualliflik mebellarini tayyorlash"),
        ("Musiqa asboblari", "musiqa asboblari"),
        ("Novdalardan buyumlar to'qish", "novdalardan buyumlar to'qish"),
        ("O'yinchoqla", "o'yinchoqlar"),
        ("Oddiy metalldan milliy uslubda tayyorlangan taqinchoqlar", "oddiy metalldan milliy uslubda tayyorlangan taqinchoqlar"),
        ("Pechka va kaminlar yasash","pechka va kaminlar yasash"),
        ("Qimmatbaho metalldan yasalgan zargarlik buyumlari", "qimmatbaho metalldan yasalgan zargarlik buyumlari"),
        ("Qo'lda gazlamalar to'qish", "qo'lda gazlamalar to'qish"),
        ("Qo'lda gilam to'qish","qo'lda gilam to'qish"),
        ("Shisha puflash ishlari", "shisha puflash ishlari"),
        ("Soatsozlik", "soatsozlik"),
        ("Suyakka o'yma naqsh solish", "suyakka o'yma naqsh solish"),
        ("Tosh o'ymakorligi", "tosh o'ymakorligi"),
        ("Tunukadan yasalgan buyumlar", "tunukadan yasalgan buyumlar"),
        ("Yog'och o'ymakorligi", "yog'och o'ymakorligi"),
        ( "Yog'ochdan tayyorlangan xalq hunarmandchiligi mahsulotlari", "yog'ochdan tayyorlangan xalq hunarmandchiligi mahsulotlari",),
        ( "Zardo'zlik buyumlari", "zardo'zlik buyumlari"),

    )
    photo = models.ImageField(upload_to='image/', blank=True, null=True)
    first_name = models.CharField(max_length=300,blank=True,null=True)  # ozgargan
    GRIFT = (

        ( "Tavsiyanoma", "tavsiyanoma"),
        ( "Xalq ustasi", "Xalq ustasi"),
        ( "Xalqaro ko'rgazma, ko'rik tanlov, festival g'olibi yoki lauriyati", "Xalqaro ko'rgazma, ko'rik tanlov, festival g'olibi yoki lauriyati"),
    )

    mid_name = models.CharField(max_length=300,blank=True,null=True)  # ozgargan
    sur_name = models.CharField(max_length=300,blank=True,null=True) # ozgargan
    ctzn = models.CharField(max_length=300,blank=True,null=True)
    birth_place = models.CharField(max_length=300,blank=True,null=True)  # tugilgan joyi
    state = models.CharField(max_length=50, choices=STATE, blank=True,null=True)
    pport_no = models.CharField(max_length=9)
    tin = models.CharField(max_length=9,blank=True,null=True)  #qo'shilgan STIR
    pin = models.CharField(max_length=14,blank=True,null=True)
    malumot = models.CharField(max_length=100,blank=True,null=True)
    per_id =models.CharField(max_length=300,blank=True,null=True)
    workadress = models.CharField(max_length=250,blank=True,null=True)
    mob_phone_no = models.CharField(max_length=14,blank=True,null=True)
    email = models.EmailField()
    web_chart = models.CharField(max_length=300, blank=True,null=True)
    studentcount = models.CharField(max_length=250,blank=True,null=True)
    job = models.CharField(max_length=300, choices=JOB,blank=True,null=True)
    grift = models.CharField(max_length=300,choices=GRIFT,blank=True,null=True)
    memberyear = models.CharField(max_length=250,blank=True,null=True)
    award = models.CharField(max_length=255,blank=True,null=True)
    festival = models.CharField(max_length=400,blank=True,null=True)
    nationalfest = models.CharField(max_length=555,blank=True,null=True)
    owngalery = models.CharField(max_length=400,blank=True,null=True)
    teacherabout = models.CharField(max_length=500,blank=True,null=True)
    orginalwork = models.CharField(max_length=300,blank=True,null=True)
    modepraduct = models.CharField(max_length=255,blank=True,null=True)
    addinform = models.CharField(max_length=400,blank=True,null=True)
    photos = models.FileField(blank=True, null=True)
    LIKE = (
        ('none', 'none'),
        ('like', 'like'),
        ('dislike', 'dislike')
    )
    like = models.CharField(max_length=123, choices=LIKE, default='none')
    likes = models.ManyToManyField(User, blank=True, null=True, related_name='like_user')
    dislike = models.ManyToManyField(User, blank=True, null=True, related_name='dislike_user')














class MarkAnketa(models.Model):
    like = models.BooleanField(default=False, )
    dislike = models.BooleanField(default=False,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anketa = models.ForeignKey(Anketa,on_delete=models.CASCADE)

    def number_of_like(self):
        return self.like.count()

    # def get_absolute_url(self):
    #     return reverse('kengash.html', args=[str(self.id)])












