from django.db import models

# Create your models here.

class Voter(models.Model):
    Last_Name = models.TextField
    First_Name = models.TextField
    RA_Street_Number = models.IntegerField()
    RA_Street_Name = models.TextField
    RA_Apartment_Number = models.TextField
    RA_Zip_Code = models.TextField
    DOB = models.DateField
    DOR = models.DateField
    Party_Affiliation = models.CharField(max_length=2)
    Precinct_Number = models.IntegerField()

    v20state = models.BooleanField(null=True, blank=True, default=None)
    v21town = models.BooleanField(null=True, blank=True, default=None)
    v21primary = models.BooleanField(null=True, blank=True, default=None)
    v22general = models.BooleanField(null=True, blank=True, default=None)
    v23town = models.BooleanField(null=True, blank=True, default=None)
    voter_score = models.IntegerField()

def load_data():
    filename = "/Users/davidchung/Downloads/newton_voters.csv"
    f = open(filename, 'r')
    for i in range(5):
        line = f.readline()
        print(line)
