from django.db import models

# Create your models here.
class Klient(models.Model):
    idKlient = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    Wiek = models.IntegerField()
    NrTel = models.IntegerField()
    Email = models.CharField(max_length=200)
    RodzajUlgi = models.CharField(max_length=100)


class Przystanek(models.Model):
    idPrzysanek = models.AutoField(primary_key=True)
    Nazwa = models.CharField(max_length=100)

class Trasa(models.Model):
    idTrasa = models.AutoField(primary_key=True)
    czas = models.DateTimeField()
    idPrzystanek = models.ForeignKey(Przystanek, on_delete=models.CASCADE)


class Kurs(models.Model):
    idKurs = models.AutoField(primary_key=True)
    Przewoniznik = models.CharField(max_length=45)
    ilosc_miejsc = models.BigIntegerField()
    Cena = models.FloatField()
    idTrasa = models.ForeignKey(Trasa, on_delete=models.CASCADE)


class KupioneBilety(models.Model):
    idBilet = models.AutoField(primary_key=True)
    idKlient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    idKurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)



