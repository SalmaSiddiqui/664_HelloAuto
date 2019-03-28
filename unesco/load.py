from django.db import models
import csv
from unesco.models import States, Category, Iso, Region, Site

# print("Starting!")

fhand = open('unesco/whc-sites-2018-small.csv')
reader = csv.reader(fhand)
next(reader)

Site.objects.all().delete()
Category.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()
States.objects.all().delete()

# print("The CSV is loaded")

# i = 0
for row in reader:
    # if len(row[0]) < 1 : continue
    # print(row[0])
    # i = i + 1
    # if i > 5 : break

    try:
        c = Category.objects.get(name=row[7])
    except:
        # print("error")
        print("Inserting category",row[7])
        c = Category(name=row[7])
        c.save()

    try:
        s = States.objects.get(name=row[8])
    except:
        # print("Inserting state",row[8])
        s = States(name=row[8])
        s.save()

    # try:
    #     st = Site.objects.get(name=row[0])
    # except:
    #     # print("Inserting site",row[0])
    #     st = Site(name=row[0])
    #     st.save()

    try:
        y= int(row[3])
    except:
        y=None


    # try:
    #     d = Site.objects.get(description=row[1])
    # except:
    #     # print("Inserting description",row[1])
    #     d = Site(description=row[1])
    #     d.save()
    #
    # try:
    #     j = Site.objects.get(justification=row[2])
    # except:
    #     # print("Inserting justification",row[2])
    #     j = Site(justification=row[2])
    #     j.save()

    try:
        o = Iso.objects.get(name=row[10])
    except:
        # print("Inserting Iso",row[10])
        o = Iso(name=row[10])
        o.save()

    try:
        l=float(row[5])
    except:
        l=None

    try:
        lg = float(row[4])
    except:
        lg = None

    try:
        ah=float(row[6])
    except:
        ah = None

    try:
        r = Region.objects.get(name=row[9])
    except:
        # print("Inserting region",row[9])
        r = Region(name=row[9])
        r.save()

    site=Site(name=row[0], description=row[1], justification=row[2], latitude=l, longitude=lg, iso= o, area_hectares=ah, year=y, category=c, state=s, region=r)
    # site=Site(name=row[0], description=row[1], justification=row[2], latitude=l, longitude=lg, iso= o, area_hectares=ah, year=y, state=s, region=r)
    site.save()
