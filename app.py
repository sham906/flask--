from flask import Flask,request,url_for,redirect,render_template
import os
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/post',methods=['POST','GET'])
def post():
    if request.method=='POST':
        text = request.form['content']
        characters = len(text)
        words = len(text.split())
        return redirect(url_for('result',text=text,characters=characters,words=words))
    return render_template('post.html',text='',characters=0,words=0)
@app.route('/result')#يمكن الاستغناء عن هي الدالة
def result():
    return render_template('result.html')
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)
