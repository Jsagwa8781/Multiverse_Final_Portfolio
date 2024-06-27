Personal Budget Tracker

Overview
The Personal Budget Tracker is a Streamlit web application designed to help users manage their personal finances by tracking income and expenses. Users can input their income sources and corresponding amounts, as well as their expenses, for a selected time period. The application then visualizes the breakdown of incomes and expenses through pie charts and displays key metrics such as total income, total expense, and remaining budget.

Features
Data Entry: Users can input their income sources and expenses for a selected time period using interactive forms.
Data Visualization: The application visualizes the breakdown of incomes and expenses through pie charts for easy analysis.
Metric Display: Key financial metrics such as total income, total expense, and remaining budget are displayed prominently for quick reference.
Dependencies
Streamlit: For building and deploying the web application.
Plotly: For creating interactive data visualizations.
streamlit-option-menu: For creating dropdown menus in Streamlit.
Usage

Install the required dependencies:
pip install streamlit plotly streamlit-option-menu

Run the Streamlit application:
streamlit run app.py
Access the application in your web browser by following the link provided in the terminal.

Configuration
Currency: The currency used for displaying financial amounts. Default is set to USD.
Page Title and Icon: Customize the title and icon displayed on the web page.
Layout: Choose between wide or narrow layout for the web page.
Development
Incomes and Expenses: Customize the list of income sources and expenses to match your specific financial situation.
Data Persistence: Implement data persistence mechanisms to store user data across sessions.
Enhancements: Add additional features such as user authentication, budget forecasting, or expense categorization.
