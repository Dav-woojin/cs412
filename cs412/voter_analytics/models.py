from django.db import models

# Create your models here.

class Voter(models.Model):
    Last_Name = models.TextField()
    First_Name = models.TextField()
    RA_Street_Number = models.IntegerField()
    RA_Street_Name = models.TextField()
    RA_Apartment_Number = models.TextField()
    RA_Zip_Code = models.TextField()
    DOB = models.DateField()
    DOR = models.DateField()
    Party_Affiliation = models.CharField(max_length=2)
    Precinct_Number = models.IntegerField()

    v20state = models.TextField(max_length=5, default='', blank=True)
    v21town = models.TextField(max_length=5, default='', blank=True)
    v21primary = models.TextField(max_length=5, default='', blank=True)
    v22general = models.TextField(max_length=5, default='', blank=True)
    v23town = models.TextField(max_length=5, default='', blank=True)
    voter_score = models.IntegerField()

def load_data():
    filename = "/Users/davidchung/Downloads/newton_voters.csv"
    f = open(filename, 'r')

    for i in range(5):
        line = f.readline()
        fields = line.strip().split(',')
        # for j in range(len(fields)):
        #     print(f'fields[{j}] = {fields[j]}')
    try:
        for line in f:
            line = f.readline().strip()
            fields = line.split(",")
            # print(fields)
            result = Voter(
                    Last_Name=fields[1],
                    First_Name=fields[2],
                    RA_Street_Number=fields[3],
                    RA_Street_Name = fields[4],
                    RA_Apartment_Number = fields[5],
                    RA_Zip_Code = fields[6],
                    
                    DOB = fields[7],
                    DOR = fields[8],

                    Party_Affiliation = fields[9],
                    Precinct_Number = fields[10],

                    v20state = fields[11],
                    v21town = fields[12],
                    v21primary = fields[13],
                    v22general = fields[14],
                    v23town = fields[15],
                    voter_score = fields[16],
                    )

            result.save()
            # print(f'Created result: {result}')
            # print(line)
    # except:
    #     print("Something went wrong")
    #     print(f"line = {line}")
    except Exception as e:
        print(f"Something went wrong: {e!r}")
        print(f"line = {line}")
    print(f"Done. Created {len(Voter.objects.all())} results")
