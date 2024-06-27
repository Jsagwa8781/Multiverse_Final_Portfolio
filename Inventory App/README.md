
# Inventory App

## Project Overview

### Purpose
The Inventory Tracking App is a comprehensive full-stack (front-end and back-end) RESTful CRUD application developed to manage the inventory of an e-commerce company. This application aims to provide a seamless and efficient method for tracking, adding, updating, and deleting inventory items, ensuring the inventory data is accurate and up-to-date.

### Users
- **E-commerce Staff:** Employees responsible for the daily management of the inventory.
- **Administrators:** Managers who need to oversee inventory operations and validate changes.
- **Customers:** Users who can browse and view inventory items, enhancing their shopping experience.

### Job
The primary job of the Inventory Tracking App is to facilitate efficient inventory management. It enables users to view all items, inspect individual items, add new items, update existing items, and delete items from the inventory. The application ensures that inventory operations are streamlined and that data integrity is maintained.

### Inspiration
The need for a reliable inventory management system in e-commerce businesses inspired the development of this application. Manual inventory management is prone to errors and inefficiencies. This project aims to automate and simplify the inventory management process, providing a robust solution for e-commerce companies to maintain accurate and efficient inventory records.

### Key Features
- **View All Items:** Display a comprehensive list of all items in the inventory, including details like name, description, price, category, and image.
- **View Single Item:** Allow users to click on an item to view detailed information about it.
- **Add Item:** Provide a user-friendly form for adding new items to the inventory.
- **Delete Item:** Enable users to remove items from the inventory with a simple click.
- **Update Item:** Offer an intuitive form for editing the details of existing items.

### Situation
As part of the Engineering team at an e-commerce company, we were tasked with rebuilding the inventory tracking application from the ground up. The goal was to create a full-stack RESTful CRUD application to efficiently track and manage inventory items.

### Task
The task was to design and develop an application that supports comprehensive inventory management. This included creating models for inventory items, setting up routes for CRUD operations, and developing front-end views for displaying and interacting with the inventory data.

### Action
1. **Setting Up the Project:**
    - Initialized the project and installed necessary dependencies (e.g., Express, Sequelize, React).
    - Created the structure of the application, including models, routes, and front-end components.

2. **Model and Routes Configuration:**
    - Defined a Sequelize model for inventory items with fields like name, description, price, category, and image.
    - Set up Express routes for CRUD operations (GET, POST, PUT, DELETE) to interact with the inventory data.

3. **Front-End Development:**
    - Developed the front-end views using React, including components for displaying all items, individual item details, and forms for adding and updating items.
    - Implemented fetch requests to connect the front-end with the back-end routes for data operations.

4. **Additional Features:**
    - Added search functionality to allow users to find items based on specific criteria.
    - Ensured the application is mobile-responsive for better user experience on different devices.
    - Implemented server-side validations for adding and updating items to maintain data integrity.

### Result
The final application successfully meets its goal of providing an efficient inventory management system. Users can view, add, update, and delete inventory items with ease. The application offers a user-friendly interface and robust functionality, ensuring that the inventory data is always accurate and up-to-date.

## Technologies

- **Languages:**
  - JavaScript (ES6+)
- **Libraries and Frameworks:**
  - Express 4.x: Back-end framework for building the server and API routes.
  - Sequelize 6.x: ORM for interacting with the database.
  - React 17.x: Front-end library for building user interfaces.
  - Node.js 14.x: JavaScript runtime for the back-end.
- **Dependencies:**
  - express==4.x.x: Core framework for the server-side application.
  - sequelize==6.x.x: ORM for database operations.
  - react==17.x.x: Library for building the front-end components.
  - npm scripts: For running the server and client development environments.
- **Deployment Tools:**
  - Docker: Containerized the application for consistent deployment.
  - Heroku: Used for deploying the back-end server.
  - Vercel: Used for deploying the front-end application.

## Competencies

### JF XX.XX: Developing Full-Stack Applications
- **Situation:** Tasked with creating a full-stack application for inventory management.
- **Action:** Designed the application's architecture, implemented back-end routes with Express and Sequelize, and developed front-end views with React.
- **Result:** Delivered a fully functional inventory tracking application that meets the needs of the e-commerce company, providing efficient inventory management and a seamless user experience.

### JF XX.XX: Implementing Server-Side Logic
- **Situation:** Required to implement server-side logic for handling inventory data.
- **Action:** Set up Express routes for CRUD operations, integrated Sequelize for database interactions, and ensured server-side validations.
- **Result:** Achieved robust server-side functionality that maintains data integrity and supports efficient inventory management operations.

