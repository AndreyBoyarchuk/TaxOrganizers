from fpdf import FPDF

class TaxOrganizer(FPDF):
    def __init__(self, selected_categories, include_cogs, company_name):
        super().__init__()
        self.selected_categories = selected_categories
        self.include_cogs = include_cogs
        self.company_name = company_name

    def generate_report(self):
        self.add_page()
        self.set_font("Arial", "B", size=16)
        self.cell(0, 10, "Tax Organizer Report", ln=True, align="C")

        # Add company name or sole proprietor name
        self.set_font( "Arial", "b",size=12,)
        self.cell(0, 10, f" Name: {self.company_name}", ln=True, align="C")

        self.set_font("Arial", "b", size=12)
        self.cell(0, 10, "Total Income: S _________", ln=True)

        if self.include_cogs:
            self.add_cost_of_goods_sold_section()

        self.set_font("Arial", size=10)
        for category in self.selected_categories:
            self.cell(0, 10, f"{category}: $________", ln=True)

        # ... (rest of the code)


        self.cell(0, 14, "", ln=True)
        self.set_font("Arial", "B", size=12)
        self.cell(0, 10, "Signature: ________________________", ln=True)
        self.cell(0, 10, "Date: __________", ln=True)

        self.output("TaxOrganizerReport.pdf")

    # ... (rest of the code)


    def add_cost_of_goods_sold_section(self):
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Cost of Goods Sold", ln=True)

        self.set_font("Arial", size=10)
        cogs_items = ["Beginning inventory", "Purchases", "Ending inventory"]
        for item in cogs_items:
            self.cell(0, 10, f"{item}: $________", ln=True)
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 10, "Total Cost of Goods Sold: $__________", ln=True)

    def add_section(self, section, items):
        self.set_font("Arial", size=12, style="B")
        self.cell(0, 10, section, ln=True)

        self.set_font("Arial", size=12)
        for item in items:
            self.cell(0, 10, item, ln=True)

