
# Task Manager Application

## High-Level Overview

### Purpose
The Task Manager Application is designed to streamline task management for users, allowing them to efficiently handle their daily responsibilities. The app features task creation, viewing, updating, deletion, and marking tasks as complete, along with robust authentication and authorization for secure data management.

### Users
- **Individual Users:** People seeking to organize personal or professional tasks.
- **Registered Members:** Users who have signed up and logged in for a personalized experience.
- **Administrators:** Individuals with elevated privileges to manage backend and user data.

### Function
The core function of the Task Manager Application is to provide a secure platform for users to manage their tasks. The app ensures all interactions with task data are protected through stringent authentication and authorization measures, delivering a secure user experience.

### Inspiration
The inspiration behind this project was the necessity for a task management tool that not only offers essential functionalities but also emphasizes user data security. The goal was to create a reliable and trustworthy platform for users to manage their personal and sensitive information.

### Key Features
- **Task Management:**
  - Create new tasks with detailed descriptions.
  - View all tasks with comprehensive details.
  - Update existing tasks with new information.
  - Delete tasks that are no longer necessary.
  - Mark tasks as complete to track progress.
- **Authentication and Authorization:**
  - User registration and login functionalities.
  - Secure password storage using hashing and salting techniques.
  - Integration of OAuth for secure user authentication.
  - Robust authorization mechanisms to protect the API from unauthorized access.
  - Data access restrictions to authenticated users only.
- **User Feedback:**
  - Informative messages for unauthorized access attempts.
  - Ensure only authorized users can create, modify, or delete tasks.

## STAR Interview Questions

### Situation
The objective was to develop a Task Manager Application that provided essential task management functionalities and incorporated robust security features. This involved creating a secure environment for user data and ensuring that only authorized users could access and manipulate task information.

### Task
The task was to build an application allowing users to manage tasks securely. This required implementing CRUD functionalities for tasks and incorporating strong authentication and authorization mechanisms to protect user data.

### Action
1. **Task Management Development:**
   - Implemented features to create, read, update, delete, and mark tasks as complete.
   - Designed a user-friendly interface to display tasks and their statuses.

2. **Security Implementation:**
   - Developed functionalities for user registration and login.
   - Applied password hashing and salting for secure storage.
   - Integrated OAuth for secure user authentication.
   - Established authorization protocols to restrict data access to authenticated users only.

3. **User Feedback Integration:**
   - Added informative messages for unauthorized access attempts.
   - Ensured that only authorized users could create, modify, or delete tasks.

### Result
The Task Manager Application provides users with a secure and efficient platform for managing tasks. Users can create, read, update, delete, and mark tasks as complete, with all interactions protected by robust authentication and authorization measures.

![Task Manager Application Screenshot](../images/TaskManagerApp.png)

## Technologies

- **Languages and Frameworks:**
  - JavaScript: Core programming language used for both front-end and back-end development.
  - React: Front-end library for building dynamic user interfaces.
  - Node.js: Back-end runtime environment for handling server-side operations.
  - Express: Framework used for building the API and managing server-side routes.
- **Security:**
  - bcrypt: Library used for hashing and salting passwords to ensure secure storage.
  - OAuth: Protocol used for secure user authentication.
- **Database:**
  - MongoDB: NoSQL database used for storing user data and tasks.
- **APIs:**
  - Custom endpoints created for task management and user authentication.

## Competencies

### JF 6.4 - Demonstrates adaptability when facing new challenges, showing flexibility in their approach
- **Situation:** Developing the Task Manager Application required adapting to new challenges, especially in implementing security features.
- **Action:** I researched various security protocols and adapted the application to include robust authentication and authorization mechanisms.
- **Result:** The application successfully secures user data, providing a reliable and adaptable task management solution.

### JF 6.5 - Effectively collaborates with team members, sharing knowledge and ideas
- **Situation:** Collaboration was crucial in developing the Task Manager Application.
- **Action:** I worked closely with team members, sharing knowledge and brainstorming ideas to solve problems and improve the application.
- **Result:** This collaborative effort resulted in a well-rounded and functional application that meets user needs.

