```markdown
# Payment Schedule Generator

This Flask web application generates a bond payment schedule based on user inputs, such as face amount, spread, issue date, yield, first payment date, and maturity date. The user can download the generated payment schedule as an Excel file.

## Features

- **Form Input**: Users input bond details (face amount, spread, issue date, yield, first payment date, maturity date) via a form.
- **Payment Schedule**: The application processes the input data and generates a bond payment schedule table.
- **Excel Export**: The user can download the payment schedule as an Excel file.

## Installation

Follow these steps to set up the application on your local machine.

### 1. Clone the repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/TanishqCIC/hl.git
```

### 2. Install dependencies

Make sure you have Python 3.x installed on your machine. Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

Here are the libraries required:

- `Flask`: A web framework for building the application.
- `pandas`: A data manipulation library used to generate Excel files.
- `openpyxl`: A library to handle `.xlsx` Excel files.

### 3. Run the application

To start the Flask web application, navigate to the project directory and run:

```bash
python home.py
```

By default, the app will run on `http://127.0.0.1:5000/`.

### 4. Open the web application

Open your browser and go to `http://127.0.0.1:5000/`. You will see the input form where you can provide the details.

### 5. Generate and Download Payment Schedule

- After filling out the form, click the "Generate Schedule" button to see the payment schedule displayed in a table.
- You can download the generated payment schedule as an Excel file by clicking the "Download as Excel" button.

## Folder Structure

```
/hl
│
├── /static
│   ├── /css
│   │   └── style.css              # CSS file for styling the application
│   └── benchmark_data.py          # Benchmark data used for calculations
│
├── /templates
│   ├── input_form.html            # Input form HTML template
│   └── table.html          # Table display and Excel download HTML template
│
├── home.py                        # Main Flask app
├── table_gen.py                   # Helper function to generate the table
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Explanation of Files

### 1. `home.py`

This is the main file containing the Flask web application. It includes:

- A route (`/`) for rendering the input form and handling form submissions.
- A route (`/download_excel`) to generate and download the payment schedule as an Excel file.

### 2. `table_gen.py`

This file contains the `generate_table` function that processes the user input data and generates a payment schedule table.

### 3. `static/benchmark_data.py`

Contains benchmark data used in the calculation of the payment schedule.

### 4. `templates/input_form.html`

HTML form where users input details such as face amount, spread, issue date, yield, etc.

### 5. `templates/table.html`

Displays the generated payment schedule in an HTML table and provides a "Download as Excel" button.

## Dependencies

- Python 3.x
- Flask
- pandas
- openpyxl

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```
