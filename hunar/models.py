from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.text import slugify
# Create your models here.













class Anketa(models.Model):
    STATE =(

        ("Avg'oniston", "Avg'oniston"),
        ("Eron", "ERON"),
        ("O'zbekiston", "O'ZBEKISTON"),
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
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=50)
    GRIFT = (

        ( "Tavsiyanoma", "tavsiyanoma"),
        ( "Xalq ustasi", "Xalq ustasi"),
        ( "Xalqaro ko'rgazma, ko'rik tanlov, festival g'olibi yoki lauriyati", "Xalqaro ko'rgazma, ko'rik tanlov, festival g'olibi yoki lauriyati"),
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
    photos = models.FileField(blank=True, null=True)
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
    like = models.BooleanField(User,default=False, related_name='liked')
    dislike =models.BooleanField(User, default=False, related_name ='disliked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    anketa = models.ForeignKey(Anketa,on_delete=models.CASCADE)



    def get_absolute_url(self):
        return reverse('kengash.html', args=[str(self.id)])












