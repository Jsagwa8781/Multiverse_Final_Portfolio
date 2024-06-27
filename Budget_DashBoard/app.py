#--Importing the required dependencies
import calendar
from datetime import datetime
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
    #---Creating the structure of the webpage---
incomes = ["Salary", "Side Hustle", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
Currency = "USD"
page_title = "Personal Budget Tracker"
page_icon = "💰💸" 
layout = "wide"

#---Creating Page Configurations
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

#---Drop Down Values for selecting the time period
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

# --- INPUT & SAVE PERIODS ---
st.header(f"Data Entry in {Currency}")
with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)

        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            st.success("Data saved!")

    # --- PLOT PERIODS ---
st.header("Data Visualization")
with st.form("saved_periods"):
    period = st.selectbox("Select Period:",months)
    submitted = st.form_submit_button("Plot Period")
    if submitted:
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        
    # Create metrics
total_income = sum(incomes.values())
total_expense = sum(expenses.values())
remaining_budget = total_income - total_expense
col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"{total_income} {Currency}")
col2.metric("Total Expense", f"{total_expense} {Currency}")
col3.metric("Remaining Budget", f"{remaining_budget} {Currency}")
            
# Plot pie chart for incomes
fig = go.Figure(data=[go.Pie(labels=list(incomes.keys()), values=list(incomes.values()))])
fig.update_layout(title_text='Incomes Breakdown')
st.plotly_chart(fig, use_container_width=True)

# Plot pie chart for expenses
fig = go.Figure(data=[go.Pie(labels=list(expenses.keys()), values=list(expenses.values()))])
fig.update_layout(title_text='Expenses Breakdown')
st.plotly_chart(fig, use_container_width=True)
