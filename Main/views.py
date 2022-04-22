from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import Blog, Contact

# ML
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Create your views here.

def home(request):
    fs = FileSystemStorage()
    data = fs.open('DiseasePredict.csv')
    dataset=pd.read_csv(data).iloc[:,:-1].columns.values
    diseaselist = []
    count=0
    for i in dataset:
        diseaselist.insert(count, i.replace("_"," ").title())
        count+=1
    return render(request, 'home.html', {"diseases":diseaselist})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {"blogs":blogs})

def blog(request, slug):
    blog = Blog.objects.get(sno=slug)
    tags = blog.tags.split()
    return render(request, 'blogpost.html', {"blog": blog, "tags":tags})

def predict(request):
    if(request.method=='POST'):

        fs = FileSystemStorage()
        data = fs.open('DiseasePredict.csv')
        dataset=pd.read_csv(data)

        encoder = LabelEncoder()
        dataset["prognosis"] = encoder.fit_transform(dataset["prognosis"])

        X = dataset.iloc[:,:-1]
        y = dataset.iloc[:, -1]
        
        inp=""
        for col in X:
            data_front_end = int(request.POST[col.replace("_"," ").title()])
            if(data_front_end==1):
                a=col.replace("_", " ")
                inp+=","+a
        inp=inp[1:]

        symptoms = X.columns.values
        
        symptom_index = {}
        for index, value in enumerate(symptoms):
            symptom = value.replace("_", " ")
            symptom_index[symptom] = index

        data_dict = {
            "symptom_index":symptom_index,
            "predictions_classes":encoder.classes_
        }

        final_svm_model = SVC()
        final_nb_model = GaussianNB()
        final_rf_model = RandomForestClassifier(random_state=18)

        final_svm_model.fit(X, y)
        final_nb_model.fit(X, y)
        final_rf_model.fit(X, y)

        inp = inp.split(",")

        input_data = [0] * len(data_dict["symptom_index"])
        for symptom in inp:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
                
        input_data = np.array(input_data).reshape(1,-1)
            
        rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
        nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
        svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
            
        final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0].title()

        return render(request, 'output.html', {"final_prediction": final_prediction.title(), "sympt":inp})


    return redirect('/')

def contact(request):
    if(request.method=='POST'):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'home.html', {"contactsubmittion":"true"})

    return redirect('/')