from flask import Flask, render_template, request, send_file
from static.benchmark_data import BENCHMARK_DATA  # Import the benchmark data
from table_gen import generate_table
import pandas as pd
from io import BytesIO

app = Flask(__name__)

def process_data(form_data):
    table_data = generate_table(
        form_data["face_amount"], 
        form_data["spread"], 
        form_data["issue_date"], 
        form_data["maturity_date"],
        form_data["yield"], 
        BENCHMARK_DATA
    )
    return table_data

@app.route('/download_excel', methods=['GET', 'POST'])
def download_excel():
    form_data = request.args
    table_data = process_data(form_data)
    
    df = pd.DataFrame(table_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Payment Schedule")
    
    output.seek(0)
    
    return send_file(output, as_attachment=True, download_name="payment_schedule.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = {
            'face_amount': request.form['face_amount'],
            'spread': request.form['spread'],
            'issue_date': request.form['issue_date'],
            'first_payment_date': request.form['first_payment_date'],
            'maturity_date': request.form['maturity_date'],
            'yield': request.form['yield']
        }

        result = process_data(form_data)

        return render_template('table.html', result=result, data=form_data)

    return render_template('input_form.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
