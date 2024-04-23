from flask import Flask, render_template, send_from_directory, request
from flask_mysqldb import MySQL
import numpy as np
import os
import matplotlib.pyplot as plt
import io
import base64

if not os.path.exists("Conv.py"):
    raise RuntimeError("Incorrect Working Directory: set directory to Server")

app = Flask(__name__)
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "123@Lalith"
app.config["MYSQL_DB"] = "es113"
mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def Home():
    return render_template("Home_1.html")

@app.route('/search', methods=['GET', 'POST'])
def Search():
    if request.method == "POST":
        search_query = request.form['search_query']
        # Modify the query to search based on bond number or any other column
        query = f"SELECT * FROM Table_2 WHERE bond_number LIKE '%{search_query}%' OR Company name LIKE '%{search_query}%';"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return render_template('search_results.html', data=data)

@app.route('/company', methods=['GET', 'POST'])
def Company():
    if request.method == "POST":
        selected_company = request.form['selected_company']
        # Fetch data from the database based on the selected company
        # Calculate totahbkbhjl bonds and value per year
        # Generate bar plot
        # Save plot to a bytes buffer
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        base64_image = base64.b64encode(bytes_image.read()).decode('utf-8')
        plt.close()
        return render_template('company_data.html', image=base64_image)

# Add similar routes for other functionalities (e.g., political party selection, company donation analysis)

if __name__ == "__main__":
    app.run(debug=True)
