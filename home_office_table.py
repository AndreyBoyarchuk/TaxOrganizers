from fpdf import FPDF

class HomeOfficeTable:
    def __init__(self):
        self.pdf = FPDF()
        self.add_home_office_table()

    def add_home_office_table(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=16 , style="B")
        title = "Home Office Expenses - Form 8829"
        self.pdf.cell(0, 10, title, ln=True, align="C")
        self.pdf.set_font("Arial", size=8, style="B")
        self.pdf.cell(0, 10, "This is simlified form and doesnt copmletelly resembles form 8829 ", ln=True)

        self.pdf.set_font("Arial", size=10)

        # Add total square footage and business square footage lines
        self.pdf.cell(0, 10, "Total square footage of the home: ________", ln=True)
        self.pdf.cell(0, 10, "Square footage exclusively used for business: ________", ln=True)

        # Add table headers
        header = ["Description", "Amount"]
        col_widths = [125, 65]
        for i in range(len(header)):
            self.pdf.cell(col_widths[i], 10, header[i], 1)
        self.pdf.ln()

        # Add table rows
        expenses = [
            "Rent",
            "Mortgage interest",
            "Insurance",
            "Utilities",
            "Maintenance",
            "Property taxes",

            "Other"
        ]
        for expense in expenses:
            self.pdf.cell(col_widths[0], 10, expense, 1)
            self.pdf.cell(col_widths[1], 10, "$", 1)
            self.pdf.ln()

        # Add total, percentage, and adjusted total rows
        self.pdf.set_font(style="B")  # Set font style to bold
        self.pdf.cell(col_widths[0], 10, "Total", 1)
        self.pdf.cell(col_widths[1], 10, "$", 1)
        self.pdf.set_font(style="")  # Reset font style to normal

        self.pdf.ln()
        self.pdf.cell(col_widths[0], 10, "Business Use Percentage", 1)
        self.pdf.cell(col_widths[1], 10, "________%", 1)
        self.pdf.ln()
        self.pdf.set_font(style="B")  # Set font style to bold
        self.pdf.cell(col_widths[0], 10, "Adjusted Total", 1)
        self.pdf.cell(col_widths[1], 10, "$", 1)
        self.pdf.set_font(style="")
        self.pdf.ln()

        # Add additional information lines

        self.pdf.set_font("Arial", size=12, style="B")
        self.pdf.cell(0, 14, "Purchase Price of Home:", ln=True)

        self.pdf.set_font("Arial", size=12, style="")
        self.pdf.cell(0, 10, "House purchased date: ________", ln=True)
        self.pdf.cell(0, 10, "Place in service: ________", ln=True)
        self.pdf.cell(0, 10, "Purchase price: $________", ln=True)
        self.pdf.cell(0, 10, "Land value: $________", ln=True)
        self.pdf.cell(0, 10, "Adjusted basis: $________", ln=True)
        self.pdf.set_font("helvetica", size=8, style="B")
        self.pdf.cell(0, 10, "Note: Your accurate depreciation amount will be determined based on the depreciation method chosen and the business-use percentage.", ln=True)
        self.pdf.set_font("Arial", size=12, style="B")
        self.pdf.cell(0, 14, "Please Sing Date It: _______________________ and Date it: _________", ln=True)
        self.pdf.ln()

    def output(self, name, dest):
        self.pdf.output(name, dest)

