from stories import stories
from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        story_id = request.form['story_id']
        story = stories[story_id]
        return render_template('questions.html', story_id=story_id, prompts=story.prompts)
    return render_template('home.html', stories=stories)


@app.route('/questions/<story_id>', methods=['GET'])
def questions(story_id):
    story = stories[story_id]
    return render_template('questions.html', story_id=story_id, prompts=story.prompts)


@app.route('/story', methods=['POST'])
def create_story():
    story_id = request.form['story_id']
    story = stories[story_id]
    answers = {key: request.form[key] for key in story.prompts}
    result = story.generate(answers)
    return render_template('story.html', story=result)
