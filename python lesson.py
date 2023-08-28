from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICES = [
    {
        'id' : 1,
        'title': 'Software design and development',
        'Hiring fees': '$5,000 p/w',
    },
       {
        'id' : 2,
        'title': 'UI/UX design / Graphic design',
        
    },
       {
        'id' : 3,
        'title': 'Data Analysis',
        'Hiring fees': '$3,850 p/w',
    },

       {
        'id' : 4,
        'title': 'Database design and managment',
        'Hiring fees': '$7,500 p/w',
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html',
                           Jobs=SERVICES, company_name= 'Genex Technologies Unlimited')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(SERVICES)


if __name__ == "__main__":
    app.run(host='192.168.202.1', port=5000 , debug=True)


