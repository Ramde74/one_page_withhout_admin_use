from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'our service is very Reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to use'
    feature3.is_true = False
    feature3.details = 'our service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'our service is very affordable'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Trustworthy'
    feature5.is_true = False
    feature5.details = 'our service is filled with trust'

    features = [feature1,feature2,feature3,feature4,feature5]



    return render(request,'index.html',{'features' : features})