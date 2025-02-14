import csv
from fpdf import FPDF

def csv_to_pdf(csv_file, pdf_file):
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the text
    pdf.set_font("Courier", size = 12)
   
    # Add file name at the center of the page
    pdf.set_xy(0, 10)
    pdf.cell(200, 10, txt = pdf_file, ln = True, align = 'C')

    # Open the CSV file and read its contents
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # Joining the elements of the row with a comma
            # and creating a string from the row.
            if row:
                space = 20 - len(row[0])
            text = (" "*space+"-").join(row)
            # Adding a cell to the PDF
            pdf.cell(200, 10, txt = text, ln = True, align = 'L')

    # Save the PDF
    pdf.output(pdf_file)

if __name__ == "__main__":
    csv_file = input("Enter CSV file name: ")
    pdf_file = input("Enter PDF file name: ")
    csv_to_pdf(csv_file, pdf_file)
    print("PDF created successfully!")
