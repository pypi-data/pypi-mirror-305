import os
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

def generate(invoices_path, pdfs_path, image_path, product_id, product_name, amount_purchased, price_per_unit, total_price):
    """
    This function converts the Excel invoices into pdf invoices.

    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """

    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:

        pdf = FPDF(orientation="P")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_no = filename.split("-")[0]
        date = filename.split("-")[1]

        # Header
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=12, txt=f"Invoice no.{invoice_no}", ln=1)
        pdf.cell(w=50, h=12, txt=f"Date: {date}", ln=1)

        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        columns = list(df.columns)
        columns = [item.replace("_", " ").title() for item in columns]

        # Title
        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=70, h=8, txt=columns[1], border=1)
        pdf.cell(w=37, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

        for index, row in df.iterrows():
            # Products
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=37, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)

        total = df["total_price"].sum()

        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=37, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

        # Total Statement
        pdf.set_font(family="Times", style="B", size=11)
        pdf.cell(w=30, h=8, txt=f"The total prize is {total}", ln=1)

        # Company Name
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=25, h=8, txt=f"PythonHow")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")
