from django.shortcuts import render
from joblib import load
import pandas as pd
import os
from roboflow import Roboflow
from django.core.files.storage import default_storage
import os
from django.conf import settings

current_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_directory, '../model/modelMangrovia.sav')
model, tree_rules, accuracy = load(model_path)

# Create your views here.

def predict_mangrove(request):

    if request.method == 'POST':
        sst = float(request.POST.get('sst'))
        salinity = float(request.POST.get('salinity'))
        tss = float(request.POST.get('tss'))

        data_to_predict = {
            'sst' : sst,
            'salinity' : salinity,
            'tss' : tss
        }

        new_data_to_predict = pd.DataFrame([data_to_predict])

        prediction = model.predict(new_data_to_predict)

        data = {
            "heading" : "Identifikasi Lahan",
            "hasil" : prediction[0],
            "accuracy" : accuracy,
            "input_data" : data_to_predict
        }

        return render(request, 'predict.html', data)
    else:
        data = {
            "heading" : "Identifikasi Lahan",
            "tree_rules" : tree_rules,
            "accuracy" : accuracy
        }
        return render(request, 'predict.html', data)

def predict_mangrove_image(request):

    if request.method == "POST" :
        gambar_mangrove = request.FILES['gambar_mangrove']
        gambar_mangrove.name = 'image_to_predict.jpg'
        default_storage.save(gambar_mangrove.name, gambar_mangrove)

        path_gambar = os.path.join(settings.MEDIA_ROOT, gambar_mangrove.name)

        rf = Roboflow(api_key="1lj3LwBCdqf2TPysCarW")
        project = rf.workspace().project("object-detection-03ii5")
        model = project.version(1).model

        # infer on a local image
        prediction = model.predict(path_gambar, confidence=40, overlap=30).json()

        print(prediction)

        data = {
            "heading" : "Prediksi Jenis Mangrove",
            "prediction" : prediction
        }

        os.remove(path_gambar)

        return render(request, 'image_predict.html', data)
    
    else :
        data = {
            "heading" : "Prediksi Jenis Mangrove"
        }

        return render(request, 'image_predict.html', data)