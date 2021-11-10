from flask import *
import os
from emotion import *

app=Flask(__name__)
app.config['SECRET_KEY']='emotion'
app.config['UPLOAD_FOLDER']="E:\CHRIST_MDS2\MDS_2\CA\Project_Sandra\Images"

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        file=request.files['file']
        file_loc=os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_loc)
        out=detect_faces(file_loc)
        return render_template('result.html',data=out,image=file_loc)
    return render_template('image_sentiment.html')