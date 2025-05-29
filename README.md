## Healthcare-Analytics-Visualization-Engine
📊 HAVE – Healthcare Analytics and Visualization Engine is a Python tool that processes medical datasets (Excel format) to generate visual reports and descriptive statistics. It helps healthcare move from volume to value-based care through insightful data analysis using pandas, matplotlib, and seaborn.

📊 HAVE – Healthcare Analytics and Visualization Engine

HAVE is a Python-powered healthcare analytics solution that combines automated data cleaning with insightful visualization to support value-based healthcare decisions. This project uses a real-world patient discharge dataset and processes it to generate clean, structured outputs for further analysis in Power BI.

🩺 Objective

As the healthcare industry shifts from volume-based to value-based care, there's an increasing need for meaningful data insights to support operational and clinical decisions. HAVE automates the process of cleaning and validating healthcare discharge data and provides a Power BI dashboard for rich, visual storytelling.

🔧 How It Works

1. Data Cleaning (Python Script)

The `PatientDischargeCleaning` class performs the following:

- ✅ Reads the raw patient discharge CSV file
- 🧪 Validates it against predefined benchmarks (headers, column count, delimiter)
- 🧹 Cleans and transforms the data:
  - Standardizes column names
  - Converts date formats
  - Normalizes phone numbers
  - Fills missing values
- 📁 Outputs a clean CSV file to `clean_files/` directory

```bash
python patient_discharge_details_scipt.py
