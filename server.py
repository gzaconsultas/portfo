from flask import Flask, render_template, request, redirect
from markupsafe import escape
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    	    data = request.form.to_dict()
    	    write_to_csv(data)
    	    return redirect('/thankyou.html')
    	except:
    		return 'No se grabo en la base de datos'
    else:
        return 'Error al enviar submit_form. Intente otra vez'


def write_to_file(data):
	with open("database.txt", 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		database.writelines(f"\n{email}, {subject}, {message}")
		

def write_to_csv(data):
	with open("database.csv", 'a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]

		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])



		

# @app.route("/index.html")
# def index():
#     return render_template("index.html")

# @app.route("/work.html")
# def work():
#     return render_template("work.html")

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

