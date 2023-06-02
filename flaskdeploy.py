from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image
app = Flask(__name__)
model = load_model('Model.h5')
malayalamModel=load_model('malayalamModel.h5')
hindiModel=load_model('HindiModel.h5')
target_img = os.path.join(os.getcwd() , 'static/images')
@app.route('/')
def index_view():
    return render_template('index.html')
@app.route('/englishPredict')
def english_view():
    return render_template('englishPredict.html')
@app.route('/malayalamPredict')
def malayalam_view():
    return render_template('malayalamPredict.html')
@app.route('/hindiPredict')
def hindi_view():
    return render_template('hindiPredict.html')
@app.route('/aboutus')
def about_view():
    return render_template('aboutus.html')
#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
           
# Function to load and prepare the image in right shape
def read_image(filename):
    img = load_img(filename, target_size=(28, 28,3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x
@app.route('/englishPredict1',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename): #Checking file format
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = read_image(file_path) #prepressing method
            class_prediction=model.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            
            if classes_x == 0:
              alphabet = "A"
            elif classes_x == 1:
              alphabet = "B"
            elif classes_x == 2:
               alphabet = "C"
            elif classes_x == 3:
               alphabet = "D"
            elif classes_x == 4:
               alphabet = "E"
            elif classes_x == 5:
               alphabet = "F"
            elif classes_x == 6:
               alphabet = "G"
            elif classes_x == 7:
               alphabet = "H"
            elif classes_x == 8:
               alphabet = "I"
            elif classes_x == 9:
               alphabet = "J"
            elif classes_x == 10:
               alphabet = "K"
            elif classes_x == 11:
               alphabet = "L"
            elif classes_x == 12:
               alphabet = "M"
            elif classes_x == 13:
               alphabet = "N"
            elif classes_x == 14:
               alphabet = "O"
            elif classes_x == 15:
               alphabet = "P"
            elif classes_x == 16:
               alphabet = "Q"
            elif classes_x == 17:
               alphabet = "R"
            elif classes_x == 18:
               alphabet = "S"
            elif classes_x == 19:
               alphabet = "T"
            elif classes_x == 20:
               alphabet = "U"
            elif classes_x == 21:
               alphabet = "V"
            elif classes_x == 22:
               alphabet = "W"
            elif classes_x == 23:
               alphabet = "X"
            elif classes_x == 24:
               alphabet = "Y"
            elif classes_x == 25:
               alphabet = "Z"
            #'alphabet' , 'prob' . 'user_image' these names we have seen in predict.html.
            return render_template('englishPredict.html', alphabet = alphabet,prob=class_prediction, user_image = file_path)
        else:
            return "Unable to read the file. Please check file extension"
@app.route('/malayalamPredict1',methods=['GET','POST'])
def predictmalayalam():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename): #Checking file format
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = read_image(file_path) #prepressing method
            class_prediction=malayalamModel.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            
            if classes_x == 0:
              malayalamAlpha = "അ"
            elif classes_x == 1:
              malayalamAlpha = "ആ"
            elif classes_x == 2:
               malayalamAlpha = "ഐ"
            elif classes_x == 3:
               malayalamAlpha = "ഔ"
            elif classes_x == 4:
               malayalamAlpha = "ബ"
            elif classes_x == 5:
               malayalamAlpha = "ഭ"
            elif classes_x == 6:
               malayalamAlpha = "ച"
            elif classes_x == 7:
               malayalamAlpha = "ഛ"
            elif classes_x == 8:
               malayalamAlpha = "ദ"
            elif classes_x == 9:
               malayalamAlpha = "ഡ"
            elif classes_x == 10:
               malayalamAlpha = "ഢ"
            elif classes_x == 11:
               malayalamAlpha = "ധ"
            elif classes_x == 12:
               malayalamAlpha = "എ"
            elif classes_x == 13:
               malayalamAlpha = "ഏ"
            elif classes_x == 14:
               malayalamAlpha = "ഫ"
            elif classes_x == 15:
               malayalamAlpha = "ഗ"
            elif classes_x == 16:
               malayalamAlpha = "ഘ"
            elif classes_x == 17:
               malayalamAlpha = "ഹ"
            elif classes_x == 18:
               malayalamAlpha = "ഇ"
            elif classes_x == 19:
               malayalamAlpha = "ഈ"
            elif classes_x == 20:
               malayalamAlpha = "ജ"
            elif classes_x == 21:
               malayalamAlpha = "ഝ"
            elif classes_x == 22:
               malayalamAlpha = "ജ്ഞ"
            elif classes_x == 23:
               malayalamAlpha = "ക"
            elif classes_x == 24:
               malayalamAlpha = "ഖ"
            elif classes_x == 25:
               malayalamAlpha = "ല"
            elif classes_x == 26:
               malayalamAlpha = "ഴ"
            elif classes_x == 27:
               malayalamAlpha = "ള"
            elif classes_x == 28:
               malayalamAlpha = "ഌ"
            elif classes_x == 29:
               malayalamAlpha = "ൡ"
            elif classes_x == 30:
               malayalamAlpha = "മ"
            elif classes_x == 31:
               malayalamAlpha = "ന"
            elif classes_x == 32:
               malayalamAlpha = "ഞ"
            elif classes_x == 33:
               malayalamAlpha = "ഩ"
            elif classes_x == 34:
               malayalamAlpha = "ണ"
            elif classes_x == 35:
               malayalamAlpha = "ങ"
            elif classes_x == 36:
               malayalamAlpha = "ഒ"
            elif classes_x == 37:
               malayalamAlpha = "ഓ"
            elif classes_x == 38:
               malayalamAlpha = "പ"
            elif classes_x == 39:
               malayalamAlpha = "ര"
            elif classes_x == 40:
               malayalamAlpha = "റ"
            elif classes_x == 41:
               malayalamAlpha = "ഋ'"
            elif classes_x == 42:
                malayalamAlpha = "ൠ"
            elif classes_x == 43:
               malayalamAlpha = "സ"
            elif classes_x == 44:
               malayalamAlpha = "ശ"
            elif classes_x == 45:
               malayalamAlpha = "ഷ"
            elif classes_x == 46:
               malayalamAlpha = "ക്ഷ"
            elif classes_x == 47:
               malayalamAlpha = "ത"
            elif classes_x == 48:
               malayalamAlpha = "ട"
            elif classes_x == 49:
               malayalamAlpha = "ഠ"
            elif classes_x == 50:
               malayalamAlpha = "ഥ"
            elif classes_x == 51:
               malayalamAlpha = "ഉ"
            elif classes_x == 52:
               malayalamAlpha = "ഊ"
            elif classes_x == 53:
               malayalamAlpha = "വ"
            elif classes_x == 54:
               malayalamAlpha = "യ"
            return render_template('malayalamPredict.html', alphabet = malayalamAlpha,prob=class_prediction, user_image = file_path)
        else:
            return "Unable to read the file. Please check file extension"

@app.route('/hindiPredict1',methods=['GET','POST'])
def predicthindi():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename): #Checking file format
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)
            img = read_image(file_path) #prepressing method
            class_prediction=malayalamModel.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            
            if classes_x == 0:
              hindiAlpha = "अ"
            elif classes_x == 1:
              hindiAlpha = "आ"
            elif classes_x == 2:
               hindiAlpha = "ऐ"
            elif classes_x == 3:
               hindiAlpha = "औ"
            elif classes_x == 4:
               hindiAlpha = "ब"
            elif classes_x == 5:
               hindiAlpha = "भ"
            elif classes_x == 6:
               hindiAlpha = "च"
            elif classes_x == 7:
               hindiAlpha = "छ"
            elif classes_x == 8:
               hindiAlpha = "द"
            elif classes_x == 9:
               hindiAlpha = "ड"
            elif classes_x == 10:
               hindiAlpha = "ढ"
            elif classes_x == 11:
               hindiAlpha = "ध"
            elif classes_x == 12:
               hindiAlpha = "ऎ"
            elif classes_x == 13:
               hindiAlpha = "ए"
            elif classes_x == 14:
               hindiAlpha = "फ़"
            elif classes_x == 15:
               hindiAlpha = "ग"
            elif classes_x == 16:
               hindiAlpha = "घ"
            elif classes_x == 17:
               hindiAlpha = "ह"
            elif classes_x == 18:
               hindiAlpha = "इ"
            elif classes_x == 19:
               hindiAlpha = "ई"
            elif classes_x == 20:
               hindiAlpha = "ज"
            elif classes_x == 21:
               hindiAlpha = "झ"
            elif classes_x == 22:
               hindiAlpha = "ज्"
            elif classes_x == 23:
               hindiAlpha = "क"
            elif classes_x == 24:
               hindiAlpha = "ख"
            elif classes_x == 25:
               hindiAlpha = "ल"
            elif classes_x == 26:
               hindiAlpha = "ळ"
            elif classes_x == 27:
               hindiAlpha = "ऌ"
            elif classes_x == 28:
               hindiAlpha = "ॡ"
            elif classes_x == 29:
               hindiAlpha = "म"
            elif classes_x == 30:
               hindiAlpha = "न"
            elif classes_x == 31:
               hindiAlpha = "ञ"
            elif classes_x == 32:
               hindiAlpha = "ण"
            elif classes_x == 33:
               hindiAlpha = "ङ"
            elif classes_x == 34:
               hindiAlpha = "ऒ"
            elif classes_x == 35:
               hindiAlpha = "ओ"
            elif classes_x == 36:
               hindiAlpha = "प"
            elif classes_x == 37:
               hindiAlpha = "फ"
            elif classes_x == 38:
               hindiAlpha = "र"
            elif classes_x == 39:
               hindiAlpha = "ड़"
            elif classes_x == 40:
               hindiAlpha = "ऋ"
            elif classes_x == 41:
               hindiAlpha = "ॠ"
            elif classes_x == 42:
               hindiAlpha = "ढ़"
            elif classes_x == 43:
               hindiAlpha = "स"
            elif classes_x == 44:
               hindiAlpha = "श"
            elif classes_x == 45:
               hindiAlpha = "ष"
            elif classes_x == 46:
               hindiAlpha = "क्ष"
            elif classes_x == 47:
               hindiAlpha = "त"
            elif classes_x == 48:
               hindiAlpha = "ट"
            elif classes_x == 49:
               hindiAlpha = "ठ"
            elif classes_x == 50:
               hindiAlpha = "थ"
            elif classes_x == 51:
               hindiAlpha = "उ"
            elif classes_x == 52:
               hindiAlpha = "ऊ"
            elif classes_x == 53:
               hindiAlpha = "व"
            elif classes_x == 54:
               hindiAlpha = "य"
            elif classes_x == 55:
               hindiAlpha = "ज़"
            
            #'malayalamAlpha' , 'prob' . 'user_image' these names we have seen in predict.html.
            return render_template('hindiPredict.html', alphabet = hindiAlpha,prob=class_prediction, user_image = file_path)
        else:
            return "Unable to read the file. Please check file extension"

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False, port=8000)