
# Personal Budget Tracker

## Project Overview

### Purpose
The Personal Budget Tracker is a comprehensive tool designed to help users efficiently manage their finances. By tracking various sources of income and categories of expenses, users can gain a clear understanding of their financial situation. This application aims to provide an easy-to-use interface for data entry, powerful visualizations for financial insights, and summary metrics to help users make informed financial decisions.

### Users
- **Individuals:** This tool is ideal for anyone looking to gain better control over their personal finances. Whether you're saving for a major purchase, trying to stick to a budget, or simply want to understand where your money is going, this application is designed to meet your needs.
- **Financial Advisors:** Professionals who assist clients with budgeting and financial planning can use this tool to create detailed financial overviews and provide actionable advice.

### Job
The primary function of the Personal Budget Tracker is to enable users to keep track of their financial inflows (incomes) and outflows (expenses). By providing a structured format for data entry and generating insightful visualizations, the application helps users understand their spending habits, identify areas for savings, and plan for future expenses.

### Inspiration
The inspiration for this project came from a personal need for a simple, yet powerful budgeting tool. Existing solutions in the market are often either too complex for everyday use or come with a steep learning curve. My goal was to create an application that combines ease of use with essential budgeting features, making financial management accessible to everyone.

### Key Features
- **Data Entry:** Users can input various types of incomes (e.g., salary, side hustle, other income) and expenses (e.g., rent, utilities, groceries, car, other expenses, savings) through a simple and intuitive interface.
- **Visualization:** The application generates pie charts for both income and expense breakdowns, providing a visual representation of the financial data.
- **Summary Metrics:** The tool calculates and displays total income, total expenses, and remaining budget, helping users quickly assess their financial status.
- **User-Friendly Interface:** The interface is designed to be straightforward and user-friendly, ensuring that users can easily navigate and utilize the application.

### Situation
I created the Personal Budget Tracker application to address the need for a straightforward and effective tool for personal financial management. With an emphasis on simplicity and functionality, this application aims to help users gain control over their finances by providing a clear and concise overview of their budget.

### Task
The primary task was to design and develop an application that allows users to input their monthly incomes and expenses, visualize the data, and get summary metrics to understand their financial health. This involved creating a user-friendly interface, implementing data entry and storage functionalities, and developing visualizations to present the financial data clearly.

### Action
1. **Setting Up the Project:**
    - Imported necessary libraries (calendar, datetime, streamlit, plotly) to provide the required functionality for the application.
    - Created the structure of the webpage using Streamlit, which serves as the framework for the application.
    - Defined the categories for incomes and expenses to ensure comprehensive data tracking.

2. **Page Configuration:**
    - Configured the page title, icon, and layout to enhance the user experience.
    - Displayed the title on the webpage to ensure users know the purpose of the application at a glance.

3. **Data Entry Form:**
    - Developed dropdown menus for selecting the month and year, allowing users to specify the period for their financial data.
    - Added number input fields for various income and expense categories to facilitate easy data entry.
    - Implemented a form submission button to save the data, ensuring users can store and retrieve their financial information.

4. **Data Visualization:**
    - Created summary metrics for total income, total expenses, and remaining budget to provide users with a quick overview of their financial status.
    - Generated pie charts for income and expense breakdowns using Plotly, offering a visual representation of the financial data that is easy to understand.

### Result
The final application successfully meets its goal of helping users manage their personal finances. Users can input their incomes and expenses, view summary metrics, and visualize their budget distribution through interactive charts. The application provides a clear and concise overview of the user's financial status, empowering them to make informed financial decisions.

## Technologies

- **Languages:**
  - Python 3.x
- **Libraries:**
  - Streamlit 0.x: Used for creating the web application interface.
  - Plotly 4.x: Utilized for generating interactive visualizations.
  - Streamlit-Option-Menu 0.x: Added for enhanced navigation and user interface options.
- **Dependencies:**
  - streamlit==0.x.x: Provides the core functionality for the web application.
  - plotly==4.x.x: Enables the creation of interactive and visually appealing charts.
  - streamlit-option-menu==0.x.x: Enhances the navigation experience within the application.
- **Deployment Tools:**
  - Streamlit Sharing: Used for deploying the web application and making it accessible to users.
  - Docker: Containerized the application for consistent and efficient deployment.

## Competencies

### JF XX.XX: Managing and Developing Data
- **Situation:** In this project, I needed to manage and develop data entry and visualization features to create an effective personal budget tracker.
- **Action:** I designed a data entry form to capture various incomes and expenses and implemented functions to handle and visualize the data. This involved setting up the project, configuring the page, developing the data entry form, and creating visualizations.
- **Result:** The application enables users to easily input and track their finances, leading to better financial management and decision-making. By providing clear visualizations and summary metrics, the tool helps users understand their financial status and identify areas for improvement.

### JF XX.XX: Building Data-Driven Applications
- **Situation:** The project required building a data-driven application that allows users to manage their personal finances effectively.
- **Action:** I utilized Streamlit for the front-end development and Plotly for data visualization to create an interactive and user-friendly application. The process involved setting up the project structure, configuring the user interface, and implementing features for data entry and visualization.
- **Result:** The resulting application is a functional and effective budget tracker that provides valuable insights into users' financial status. The tool's ease of use and powerful features make it a valuable resource for anyone looking to manage their finances better.

