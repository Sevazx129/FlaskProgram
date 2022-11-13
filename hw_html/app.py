from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>')
def candidate_page(uid):
    candidate: dict = utils.get_candidate(uid)
    if not candidate:
        return 'Кандидат не найден'
    return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidates_page(candidate_name):
    candidates: list[dict] = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def search_candidates_by_skill_page(skill_name):
    candidates: list[dict] = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill=skill_name)



app.run()
