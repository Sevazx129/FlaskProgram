from flask import Flask, request, render_template
import functions

candidates = functions.load_canditates('candidates.json')

app = Flask(__name__)


@app.route('/')
def hello():
  return render_template('print.html', candidates=candidates)

@app.route('/candidates/<int:uid>')
def user(uid):
  return render_template('user_pk.html', uid=uid, users=candidates)

@app.route('/skills/<uid>')
def skills(uid):
  return render_template('skills.html', uid=uid, users=candidates)

app.run()