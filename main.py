import streamlit as st
import json
import tempfile
from tax_org import TaxOrganizer
from home_office_table import HomeOfficeTable

from auto_expense_table import AutoExpenseTable
with open("categories.json", "r") as file:
    categories_data = json.load(file)

st.set_page_config(page_title="Tax Organizer", layout="wide", initial_sidebar_state="expanded")


st.title("Tax Organizer")
company_name = st.text_input("Company Name or Sole Proprietor Name:")
st.write("Check the categories you want to include in the report:")
st.markdown(
    """
   <style>
        .category-header {
            color: orange;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #ffffff;
            color: orange;
            font-weight: bold;
            font-size: 14px;
            border: 2px solid orange;  /* Add an orange border */
            transition: background-color 0.2s;
        }
        .stButton > button:hover {
            background-color: darkorange;
        }
       
       .cogs-title {
            font-family: 'Roboto', sans-serif;
            color: orange;
            font-size: 19px;
            cursor: pointer;
        }
        .collapsible-content {
            display: none;
        }
    </style>
    
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("<div class='cogs-title' onclick='toggleCollapsible()'>Cost of Goods Sold (COGS):</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='collapsible-content' id='collapsible'>", unsafe_allow_html=True)
include_cogs = st.sidebar.radio(
    "Cogs should be include if your company sells products or tracks inventory.",
    ('Exclude COGS', 'Include COGS'))
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Add JavaScript to toggle the collapsible container
st.markdown(
    """
    <script>
        function toggleCollapsible() {
            var content = document.getElementById("collapsible");
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        }
    </script>
    """,
    unsafe_allow_html=True,
)



max_items = 15
column_items = []
col_index = 0
current_items = 0

cols = st.columns(7)

for category, items in categories_data.items():
    if current_items + len(items) > max_items:
        col_index += 1
        current_items = 0

    if col_index < len(cols):
        cols[col_index].markdown(f"<div class='category-header'>{category}</div>", unsafe_allow_html=True)
        for item in items:
            if current_items >= max_items:
                col_index += 1
                current_items = 0
                if col_index >= len(cols):
                    break
            if cols[col_index].checkbox(item, key=f"{category}-{item}"):
                column_items.append(item)
            current_items += 1


button_columns = st.columns(3)

if st.sidebar.button("Generate Report"):
    report = TaxOrganizer(column_items, include_cogs == 'Include COGS', company_name)
    report.generate_report()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        report.output(tmp_file.name, "F")
        with open(tmp_file.name, "rb") as file:
            st.sidebar.download_button("Download Report", data=file.read(), file_name="TaxOrganizerReport.pdf", mime="application/pdf")
if st.sidebar.button("Generate Home Office Report"):
    home_office_report = HomeOfficeTable()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        home_office_report.output(tmp_file.name, "F")
        with open(tmp_file.name, "rb") as file:
            st.sidebar.download_button("Download Home Office Report", data=file.read(), file_name="HomeOfficeReport.pdf", mime="application/pdf")

if st.sidebar.button("Generate Auto Expense Report"):
    auto_expense_report = AutoExpenseTable()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        auto_expense_report.generate_report()
        auto_expense_report.pdf.output(tmp_file.name, "F")

        with open(tmp_file.name, "rb") as file:
            st.sidebar.download_button("Download Auto Expense Report", data=file.read(), file_name="AutoExpenseReport.pdf",
                               mime="application/pdf")