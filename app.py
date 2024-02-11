from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('task')
    tasks.append({'text': new_task})
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
