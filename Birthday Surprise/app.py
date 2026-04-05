from flask import Flask, render_template, request, redirect

app = Flask(__name__)

PASSWORD = "0504"   # 🔐 Password set to 0504

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/final')
def final():
    return render_template('final.html')

if __name__ == '__main__':
    app.run(debug=True)