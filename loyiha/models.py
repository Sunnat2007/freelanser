from django.db import models

class Darslar(models.Model):
    video = models.FileField('Videoni joylashtring:' ,max_length=100)
    popular = models.IntegerField('Ko\'rilganlar soni' ,default=0)
    image = models.ImageField('Video yuzi uchun rasm:' ,upload_to='maruzaimg/')
    title = models.CharField('Sarlavha', max_length=150)
    date = models.CharField('Video muallifi:', max_length=150)
    slug = models.SlugField('Slug Masalan: "1-dars" (bo\'shliqsiz yozilishi shart)' ,max_length=150)
    

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'
        
  

    def get_absolute_url(self):
        return f"/darslar/{self.slug}"

    def __str__(self):
        return str(self.title)

class Vakansiyalar(models.Model):
    malumot = models.CharField('Ish haqida malumot...' ,max_length=200)
    ismi = models.CharField('Ish beruvchining ismi:' ,max_length=200)
    narx = models.CharField('Taklif qilinayotgan narx:' ,max_length=100)
    image = models.ImageField('Rasm:' ,upload_to='maruzaimg/', default='static/img/team-1.jpg')
    
    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'

    def __str__(self):
        return self.ismi

class Istedodlilar(models.Model):
    image = models.ImageField('Rasm:' ,upload_to='maruzaimg/', default='static/img/team-1.jpg')
    ismi = models.CharField('Ismi:' ,max_length=200)
    narx = models.CharField('Ism Familiyasi:' ,max_length=100)
    
    class Meta:
        verbose_name = 'Istedod'
        verbose_name_plural = 'Istedodlilar'

    def __str__(self):
        return self.ismi
    
class FoydaliHavolalar(models.Model):
    sayt_nomi = models.CharField('Sayt nomi:' ,max_length=200)
    malumoti = models.CharField('Ozgina malumot:' ,max_length=100)
    url = models.URLField('Sayt linki:' ,max_length=200)
    
    class Meta:
        verbose_name = 'Foydali havola'
        verbose_name_plural = 'Foydali havolalar'

    def __str__(self):
        return self.sayt_nomi
    
    