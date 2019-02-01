#Import Flask
from flask import Flask, render_template, request, redirect,url_for, session, logging,flash 

#initiate the app
app = Flask(__name__) 

#create routes
@app.route('/', methods=['POST','GET'])#root folder
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        flash('Data posted successfully','success')
        session['username'] = request.form['username']
        session['log']=True
        username = request.form["username"]
        password=request.form['password']
        if username=='admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('voters'))
        
        if username is None:
            flash('Please Enter Your Username', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/admin') #admin url
def admin():
    return render_template('admin.html')

@app.route('/voters')#voters url
def voters():
    return render_template('voters.html')

@app.route('/logout')
def logout():
    session['log']= False
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/vote')
def vote():
    return render_template('vote.html')

#run application
if __name__=='__main__': 
    app.secret_key="1234567collins"
    app.run(debug=True)
