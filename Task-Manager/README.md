# Task Manager App

## Project Overview

### Purpose
The Task Manager App is a comprehensive application designed to help users efficiently manage their tasks. It offers functionalities for creating, reading, updating, and deleting tasks, along with the ability to mark tasks as complete. Additionally, the app incorporates robust authentication and authorization mechanisms to ensure user data privacy and security.

### Users
- **General Users:** Individuals looking to manage their daily tasks efficiently.
- **Registered Users:** Users who sign up and log in to access personalized task management features.
- **Administrators:** Users with elevated privileges to manage the application's backend and user data.

### Job
The primary job of the Task Manager App is to provide users with an efficient and secure way to manage their tasks. It offers a user-friendly interface for task management while ensuring that user data is protected through authentication and authorization mechanisms.

### Inspiration
The inspiration for this project came from the need for a reliable and secure task management system. Many existing task management tools lack robust security features, which prompted the development of this app with a focus on user data protection and privacy.

### Key Features
- **Task Management:**
  - Create, read, update, and delete tasks.
  - Mark tasks as complete.
- **Authentication and Authorization:**
  - User registration and login.
  - Password hashing and salting for security.
  - OAuth for user login authentication.
  - Authorization to protect API from unauthorized users.
  - Restrict data and API access to authorized users only.
- **User Experience:**
  - Informative messages for unauthorized access attempts.
  - Data access limited to authenticated users.

## STAR Interview Questions

### Situation
We decided to create the Task Manager App to provide a secure and efficient task management solution. The goal was to implement essential CRUD functionalities for tasks and integrate strong authentication and authorization features to protect user data.

### Task
Our task was to develop an application that allows users to manage their tasks securely. This included creating CRUD functionalities for tasks, implementing user authentication and authorization, and ensuring data protection through robust security measures.

### Action
1. **Task Management:**
   - Developed functionalities to create, read, update, delete, and mark tasks as complete.
   - Designed a user-friendly interface to display tasks and their statuses.

2. **Authentication and Authorization:**
   - Implemented user registration and login features.
   - Used password hashing and salting for secure password storage.
   - Integrated OAuth for user authentication.
   - Developed authorization mechanisms to restrict data access to authenticated users only.

3. **Security Enhancements:**
   - Ensured unauthorized users receive helpful messages when attempting to access restricted areas.
   - Restricted API access to prevent unauthorized creation, modification, or deletion of tasks.

### Result
The Task Manager App successfully provides a secure and efficient platform for task management. Users can create, read, update, delete, and mark tasks as complete. The app ensures data protection through robust authentication and authorization mechanisms.

## Technologies

- **Languages and Frameworks:**
  - JavaScript: For implementing application logic.
  - React: Front-end library for building user interfaces.
  - Node.js: Server-side JavaScript runtime for handling requests.
  - Express: Web framework for building the API.
- **Security:**
  - bcrypt: Library for hashing and salting passwords.
  - OAuth: Protocol for secure user authentication.
- **Database:**
  - MongoDB: NoSQL database for storing user data and tasks.
- **APIs:**
  - Custom API endpoints for task management and user authentication.

## Competencies

### JF 6.6 - Shows initiative for solving problems within their own remit, being resourceful when faced with a problem to solve
- **Situation:** As a self-taught programmer, I frequently encounter new coding challenges. I approach these by breaking down the problem into smaller steps and conducting thorough research.
- **Action:** During this project, I demonstrated problem-solving skills by implementing secure authentication and authorization mechanisms. I researched best practices for password security and chose to integrate OAuth for user authentication.
- **Result:** This approach ensured the app's security, protecting user data from unauthorized access and enhancing my problem-solving skills by demonstrating the importance of resourcefulness and adaptability in coding.

