from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Accra, Ghana',
        'salary': 'GHC 4500'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Accra, Ghana',
        'salary': 'GHC 5000'
    },
    {
        'id': 3,
        'title': 'UI/UX Designer',
        'location': 'Remote',
        'salary': 'GHC 5000'
    }
]


@app.route('/')
def home_page():
    return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
