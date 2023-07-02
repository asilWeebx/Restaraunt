from django.db import models

# Create your models here.


#Categoriya menyu
class Categoriya(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Menyu(models.Model):
    categoriya = models.OneToOneField(Categoriya, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/')
    text = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Bron(models.Model):
    ism = models.CharField(max_length=250)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    qushilgan = models.DateTimeField(auto_now_add=True)
    vaqt = models.CharField(max_length=19)
    odam = models.IntegerField()
    xabar = models.TextField()


    def __str__(self):
        return self.ism

class Chefs(models.Model):
    fmi = models.CharField(max_length=250)
    subject = models.CharField(max_length=26)
    img = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.fmi

class Galery(models.Model):
    img = models.ImageField(upload_to='images/')

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    xabar = models.TextField()

    def __str__(self):
        return self.email



class Specials(models.Model):
    name = models.CharField(max_length=250)
    newname = models.CharField(max_length=250)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
