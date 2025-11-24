import os
import json
import re
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
XLSX_PATH = os.path.join(BASE_DIR, '..', 'data', 'dashboard_raw_data.xlsx')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'data', 'dataframe')
COLLECTION = "dashboard_df"

county_names = [
    "California", "Alameda", "Alpine", "Amador", "Butte", "Calaveras", "Colusa", "Contra Costa",
    "Del Norte", "El Dorado", "Fresno", "Glenn", "Humboldt", "Imperial", "Inyo",
    "Kern", "Kings", "Lake", "Lassen", "Los Angeles", "Madera", "Marin", "Mariposa",
    "Mendocino", "Merced", "Modoc", "Mono", "Monterey", "Napa", "Nevada", "Orange",
    "Placer", "Plumas", "Riverside", "Sacramento", "San Benito", "San Bernardino",
    "San Diego", "San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
    "Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Sierra", "Siskiyou",
    "Solano", "Sonoma", "Stanislaus", "Sutter", "Tehama", "Trinity", "Tulare",
    "Tuolumne", "Ventura", "Yolo", "Yuba"
]

def load_tables(max_col=15, select_sheets=None):
    sheets = ['Employment Rate', 'Wage Progression', 'PostCWEmployment', 'Exits With Earnings', 'Reentry', 'Reentry After Exit with Earning']
    if select_sheets:
        sheets = [s for s in sheets if s in select_sheets]

    indicator_tables = {}
    for sheet in sheets:
        raw_df = pd.read_excel(
            XLSX_PATH,
            sheet_name=sheet,
            header=None,
            engine='openpyxl'
        )
        raw_df = raw_df.dropna(how='all')
        header = raw_df.iloc[1].to_list()
        df = raw_df[2:].copy()
        df.columns = header
        indicator = sheet.strip().lower().replace(' ', '_')
        indicator_tables[indicator] = df

    return indicator_tables

def split_by_county(indicator_tables):
    structured_data = {}
    for indicator, df in indicator_tables.items():
        df.columns = [str(c).strip().lower() for c in df.columns]
        structured_data[indicator] = {}

        for county in county_names:
            county_df = df[df["county"] == county]
            structured_data[indicator][county] = county_df
    return structured_data



if __name__ == '__main__':
    test_list = ["Employment Rate"]
    test_tables = load_tables(select_sheets=test_list)
    structured_data = split_by_county(test_tables)


