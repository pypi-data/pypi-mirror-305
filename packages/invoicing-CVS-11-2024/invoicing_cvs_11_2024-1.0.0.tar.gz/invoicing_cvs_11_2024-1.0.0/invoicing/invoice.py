import os
from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

C = 0

def generate(invoices_path, pdfs_path, product_id, product_name,
             amount_purchased, price_per_unit, total_price):
    """
    This function converts invoice Excel files into PDF invoices.
    :param invoices_path:
    :param pdfs_path:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """

    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_nr, invoice_date = filename.split("-")

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice date: {invoice_date}", ln=1)

        excel_df = pd.read_excel(filepath, sheet_name="Sheet 1")

        columns = list(excel_df.columns)
        columns = [item.replace("_", " ").title() for item in columns]
        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(
            C,
            C,
            C,
        )
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(w=36.5, h=8, txt=columns[0], align="C", fill=True, border=1)
        pdf.cell(w=45.0, h=8, txt=columns[1], align="C", fill=True, border=1)
        pdf.cell(w=36.5, h=8, txt=columns[2], align="C", fill=True, border=1)
        pdf.cell(w=36.5, h=8, txt=columns[3], align="C", fill=True, border=1)
        pdf.cell(w=36.5, h=8, txt=columns[4], align="C", fill=True, border=1, ln=1)

        for index, row in excel_df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(C, C, C)
            pdf.cell(w=36.5, h=8, txt=str(row[product_id]), align="C", border=1)
            pdf.cell(w=45.0, h=8, txt=str(row[product_name]), align="C", border=1)
            pdf.cell(w=36.5, h=8, txt=str(row[amount_purchased]), align="C", border=1)
            pdf.cell(w=36.5, h=8, txt=str(row[price_per_unit]), align="C", border=1)
            pdf.cell(w=36.5, h=8, txt=str(row[total_price]), align="C", border=1, ln=1)

        total_sum = sum(excel_df[total_price])
        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(
            C,
            C,
            C,
        )
        pdf.cell(w=36.5, h=8, txt="", border=1)
        pdf.cell(w=45.0, h=8, txt="", border=1)
        pdf.cell(w=36.5, h=8, txt="", border=1)
        pdf.cell(w=36.5, h=8, txt="", border=1)
        pdf.cell(w=36.5, h=8, txt=str(total_sum), align="C", border=1, ln=1)

        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(
            C,
            C,
            C,
        )
        pdf.cell(w=0, h=8, ln=1)
        pdf.cell(w=0, h=8, ln=1)
        pdf.cell(w=0, h=8, txt=f"The total price to pay is: {total_sum} $.", align="C")

        company_name = "Tech Solutions"
        pdf.set_font(family="Times", size=14, style="IB")
        pdf.set_text_color(
            C,
            C,
            C,
        )
        pdf.cell(w=0, h=8, ln=1)
        pdf.cell(w=0, h=8, ln=1)
        pdf.cell(w=0, h=8, txt=f"{company_name.upper()} Group.", align="L")

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)

        pdf.output(f"{pdfs_path}/{filename}.pdf")