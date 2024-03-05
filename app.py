from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        if 'names' not in session:
            session['names'] = []
        session['names'].append(name)
        session.modified = True
        return render_template('greeting.html', name=name)
    return render_template('index.html')

@app.route('/names')
def names():
    return render_template('names.html', names=session.get('names', []))

if __name__ == '__main__':
    app.run(debug=True)