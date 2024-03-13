from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Accra, Ghana',
        'salary': '4500'
    },
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'Accra, Ghana',
        'salary': '5000'
    }
]


@app.route('/')
def home_page():
    return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
