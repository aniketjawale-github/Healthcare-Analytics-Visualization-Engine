import pandas as pd
import numpy as np


class PatientDischargeCleaning:

    def read_csv(self):
        """
        Reads the patient discharge CSV file and returns the DataFrame.
        """
        patient_discharge_df = pd.read_csv(
            r"C:\Users\anike\OneDrive\Desktop\DEKSTOP FILES TEMP SAVED\DE SEM 6\HAVE GITHUB\patient_discharge_details_dump.csv",
            header=0, delimiter=','
        )
        return patient_discharge_df

    def benchmark(self):
        """
        Sets benchmark values for number of columns and expected headers.
        """
        no_of_columns = 20
        list_of_headers = ['REGISTRATIONNO', 'PATIENTNAME', 'CITYNAME', 'DISTRICTNAME',
                           'STATENAME', 'PHONE', 'ADMITDATETIME', 'DISCHARGEDATETIME',
                           'COMPANY NAME', 'DEPARTMENT', 'DISCOUNTAMOUNT', 'BILLAMOUNT',
                           'ROOM TARIFF', 'PHARMACY', 'Investigations', 'Bedside Procedures',
                           'Physiotherapy', 'Surgeries', 'CONSUMABLES', 'Doctor Consultations']
        return no_of_columns, list_of_headers

    def validation_fn(self, patient_discharge_df, no_of_columns, list_of_headers):
        """
        Validates delimiter, header contents, and column count.
        """
        delimiter_check = len(patient_discharge_df.columns) > 1
        header_content_check = list_of_headers == list(patient_discharge_df)
        no_of_columns_check = len(patient_discharge_df.columns) == no_of_columns
        return delimiter_check, header_content_check, no_of_columns_check

    def clean_data(self, patient_discharge_df):
        """
        Cleans inconsistent data and converts column data types:
        - Lowercases and renames columns
        - Parses datetime columns
        - Standardizes phone numbers
        - Fills NaN with 0
        """
        patient_discharge_df.columns = map(str.lower, patient_discharge_df.columns)
        patient_discharge_df.columns = patient_discharge_df.columns.str.replace(" ", "_")

        patient_discharge_df['admitdatetime'] = pd.to_datetime(
            patient_discharge_df['admitdatetime'], dayfirst=True, errors='coerce'
        )
        patient_discharge_df['dischargedatetime'] = pd.to_datetime(
            patient_discharge_df['dischargedatetime'], dayfirst=True, errors='coerce'
        )

        patient_discharge_df['phone'] = patient_discharge_df['phone'].astype(str).apply(
            lambda x: x if len(x) == 10 and x.isdigit() else '8888999999'
        )

        patient_discharge_df.fillna(0, inplace=True)
        return patient_discharge_df

    def write_clean_csv(self, patient_discharge_clean_df):
        """
        Writes cleaned data to a new CSV file.
        """
        patient_discharge_clean_df.to_csv(
            r'C:\Users\anike\OneDrive\Desktop\DEKSTOP FILES TEMP SAVED\DE SEM 6\HAVE GITHUB\Clean File/clean_patient_discharge_details_dump.csv',
            encoding='utf-8', index=False
        )
        return True


if __name__ == '__main__':
    pdclean = PatientDischargeCleaning()
    patient_discharge_df = pdclean.read_csv()
    no_of_columns, list_of_headers = pdclean.benchmark()
    delimiter_check, header_content_check, no_of_columns_check = pdclean.validation_fn(
        patient_discharge_df, no_of_columns, list_of_headers
    )

    if delimiter_check and header_content_check and no_of_columns_check:
        patient_discharge_clean_df = pdclean.clean_data(patient_discharge_df)
        pdclean.write_clean_csv(patient_discharge_clean_df)
        print("✅ Script executed successfully!")
    else:
        print("❌ Validation failed. Please check the input file structure.")
