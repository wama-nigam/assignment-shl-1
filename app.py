from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
app = Flask(__name__, template_folder='template')
# Function to read data from CSV
data = pd.read_csv('C:/Users/DELL/Desktop/assignment-shl/venv/dataset/Parsed_FE Interviews_Cleaned.xlsx - Sheet1.csv')

@app.route('/')
def index():
    return render_template('index.html', data=data.to_dict(orient='records'))

@app.route('/gallery')
def gallery_view():
    data_list = data.to_dict(orient='records')
    return render_template('gallery.html', data=data_list)

if __name__ == '__main__':
    app.run(debug=True)
