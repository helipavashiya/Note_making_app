from flask import Flask, render_template, request,redirect,url_for,session
import uuid
app = Flask(__name__)
app.secret_key = 'hella'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True

def generate_unique_identifier():
    return str(uuid.uuid4())

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        note_id = generate_unique_identifier()
        session[note_id] = request.form['note']
        return redirect(url_for('index'))
    notes = [session[note_id] for note_id in session.keys()]
    return render_template("home.html", notes=notes)

# 127.0.0.1 => loopback or localhost address  
# run on local host -->  app.run(debug=True)
# 0.0.0.0 => broadcasting 
# we can deploy the app on LAN through broadacasting

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
