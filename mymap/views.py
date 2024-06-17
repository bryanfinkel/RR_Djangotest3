from django.shortcuts import render
from mymap.models import MapPoint, Schools
from mymap.forms import CSVUploadForm   # Import the form class
import pandas as pd
import numpy as np


# Create your views here.
def index(request):
    allpoints = MapPoint.objects.all()
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file_content'])
            return render(request, "mymap/index.html", {'allpoints':allpoints, 'form':CSVUploadForm()})
        else:
            return render(request, "mymap/index.html", {'allpoints':allpoints, 'form':form})
    else:
        form = CSVUploadForm()
        return render(request, "mymap/index.html", {'allpoints':allpoints, 'form':form}) 
    
def handle_uploaded_file(f):
    df = pd.read_csv(f)
    df['# Classrooms'] = df['# Classrooms'].fillna(0)
    # loop thru rows
    for index, row in df.iterrows():
        school=Schools.objects.get_or_create(
            name=row['Name'], 
            lat=row['Latitude'], 
            lon=row['Longitude'], 
            Level=row['Level'], 
            Status=row['Status'], 
            Sponsor=row['Sponsor'], 
            Classrooms=row['# Classrooms'])

    print(df.head())



