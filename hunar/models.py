from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.text import slugify
# Create your models here.













class Anketa(models.Model):
    STATE =(

        ("107", "Avg'oniston"),
        ("105", "ERON"),
        ("87", "O'ZBEKISTON"),
        ("106", "OZARBAYJON"),
        ("89", "QIRG'IZISTON"),
        ("103","QOZOG'ISTON"),
        ("101","ROSSIYA"),
        ("88","TOJIKISTON"),
        ("104","TURKIYA"),
        ("102","TURKMANISTON"),

    )
    JOB = (

        ("118", "bosh kiyimlar tayyorlash"),
        ("129", "charm mahsulotlari"),
        ("125", "chinni, fayans va sopol buyumlari"),
        ("139", "emallash ishlari"),
        ("140", "esdalik buyumlari"),
        ("108", "ganch o'ymakorligi"),
        ("121","gul bosilgan gazlamalar va chokli buyumlar"),
        ("137", "hajmli va shaklli qoliplarda quyilgan buyumlar"),
        ("113", "kandakorlik, misgarlik buyumlari"),
        ("122", "kashtachilik"),
        ("135", "ko'zgu tayyorlash"),
        ("128", "mayda haykaltaroshlik buyumlari"),
        ("114", "metalldan yasalgan buyumlar"),
        ("117", "milliy liboslar tayyorlash"),
        ("116", "milliy poyabzal tayyorlash"),
        ("112", "miniatyura, rang tasvir, naqqoshlik va bo'yoqli naqshlar"),
        ("134", "mozaika ishlari"),
        ("130", "mualliflik mebellarini tayyorlash"),
        ("124", "musiqa asboblari"),
        ("133", "novdalardan buyumlar to'qish"),
        ("127", "o'yinchoqlar"),
        ("141r", "oddiy metalldan milliy uslubda tayyorlangan taqinchoqlar"),
        ("132","pechka va kaminlar yasash"),
        ("126", "qimmatbaho metalldan yasalgan zargarlik buyumlari"),
        ("110", "qo'lda gazlamalar to'qish"),
        ("109","qo'lda gilam to'qish"),
        ("136", "shisha puflash ishlari"),
        ("138", "soatsozlik"),
        ("120", "suyakka o'yma naqsh solish"),
        ("111", "tosh o'ymakorligi"),
        ("115   ", "tunukadan yasalgan buyumlar"),
        ("119", "yog'och o'ymakorligi"),
        ( "131", "yog'ochdan tayyorlangan xalq hunarmandchiligi mahsulotlari",),
        ( "123", "zardo'zlik buyumlari"),

    )
    photo = models.ImageField()
    name = models.CharField(max_length=50)
    GRIFT = (

        ( "100", "Tavsiyanoma"),
        ( "98", "Xalq ustasi"),
        ( "99", "Xalqaro ko'rgazma, ko'rik tanlov, festival g'olibi yoki lauriyati"),
    )

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    koyadress = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=STATE, blank=True,null=True)
    password = models.CharField(max_length=9)
    passwordpnfl = models.CharField(max_length=14)
    malumot = models.CharField(max_length=30)
    adress =models.CharField(max_length=50)
    workadress = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    email = models.EmailField()
    web_chart = models.CharField(max_length=30, blank=True,null=True)
    studentcount = models.CharField(max_length=30)
    job = models.CharField(max_length=150, choices=JOB,blank=True,null=True)
    grift = models.CharField(max_length=155,choices=GRIFT,blank=True,null=True)
    memberyear = models.CharField(max_length=50)
    award = models.CharField(max_length=155)
    festival = models.CharField(max_length=155)
    nationalfest = models.CharField(max_length=155)
    owngalery = models.CharField(max_length=155)
    teacherabout = models.CharField(max_length=155)
    orginalwork = models.CharField(max_length=155)
    modepraduct = models.CharField(max_length=155)
    addinform = models.CharField(max_length=155)
    photos = models.ImageField()
    # slug = models.SlugField()
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(GeeksModel, self).save(*args, **kwargs)



    # def __str__(self):
    #     self.name








class User(AbstractUser):
    nickname=models.CharField(max_length=50,blank=True,null=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'




class   MarkAnketa(models.Model):
    like = models.BooleanField(default=False)
    dislike =models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anketa = models.ForeignKey(Anketa,on_delete=models.CASCADE)



    def get_absolute_url(self):
        return reverse('kengash.html', args=[str(self.id)])












