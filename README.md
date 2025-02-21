this is a web app that i created using the help from chatgpt , joseph tan , ashley khng ---> this app aims to solve the hastle of having to wait in line after book in to sign the BIBO(book in book out) book and therefore making it easier and faster for individuals to sign online using thier smartphones , via a qr code that leads to the URL or it can be a link that is sent to the whatsapp group chat 
the security features that i have thought through is , 
Firstly , only 1 login is allowed for 1 device and i have restricted this by limiting 1 ip adress to one login
Secondly , the users location will be automatically recorded when marking attendance , this is so that if someone tries to cheat the system and gets caught there is proof to show that he or she is not in camp and had lied to superiors.

Project Report: Camp Attendance System

1. Introduction

The Camp Attendance System is a digital solution designed to efficiently track and manage attendance at camps, events, or training programs. The application leverages a web-based interface built using Flask and SQLite to facilitate seamless attendance marking and retrieval of attendance records. This system replaces traditional paper-based attendance methods, enhancing accuracy, accessibility, and efficiency.

2. Objectives

The primary objectives of this project include:

Providing a secure and efficient method to record attendance.

Reducing administrative workload by automating attendance management.

Ensuring real-time data retrieval for better decision-making.

Minimizing errors and fraud associated with manual attendance tracking.

Enabling easy access and retrieval of attendance history.

Verifying attendance using location radius to ensure users log in within the camp premises.

3. System Overview

The Camp Attendance System is built using Flask (a Python web framework) and SQLite (a lightweight relational database). The system comprises the following key functionalities:

3.1 Attendance Registration

Users provide their name and NRIC (National Registration Identity Card number) via a web form.

Upon submission, the system validates the input and stores the attendance record in the SQLite database with a timestamp.

A success message is displayed upon successful registration.

The system checks the user's location to verify they are within the camp radius before allowing attendance submission.

3.2 Attendance Retrieval

Authorized users can retrieve all attendance records from the database.

The records include name, NRIC, timestamp, and unique ID.

The system displays records in reverse chronological order to show the most recent attendance first.

3.3 Database Management

The system automatically creates an SQLite database (attendance.db) upon deployment if it does not exist.

The attendance table is structured to store ID, name, NRIC, and timestamp.

All records are securely stored and can be accessed via API endpoints.

4. Technical Implementation

The system is implemented using the following technologies:

Backend: Flask framework (Python)

Database: SQLite (Relational Database Management System)

Frontend: HTML and JavaScript (for web-based interaction)

APIs: RESTful APIs for data communication

Hosting: Can be deployed on a local server or cloud-based infrastructure

Location Services: Geolocation API to validate if users log in within the camp's predefined radius

4.1 Key Code Implementation

Flask App Setup: The application initializes the database and provides routes for attendance marking and retrieval.

Database Operations: The SQLite database is managed using SQL queries within Flask.

API Endpoints:

/mark_attendance (POST) - Records attendance

/get_attendance (GET) - Retrieves attendance records

Location validation feature to verify user check-in within the camp boundary

5. Use Case Scenarios

The system is particularly useful in scenarios such as:

5.1 Camp Management

Organizers can track participant attendance during multi-day camps.

Ensures every attendee is accounted for in real time.

Verifies user check-in location to prevent fraudulent attendance submissions.

5.2 Corporate Training Programs

Companies can maintain digital records of employee training attendance.

Facilitates reporting and compliance tracking.

5.3 Educational Institutions

Schools and universities can use the system for student attendance tracking during events and lectures.

Reduces the chances of proxy attendance.

5.4 Community Events

Community organizers can keep attendance logs for public events.

Enables efficient crowd management.

6. Benefits of the System

The implementation of this system provides the following benefits:

Accuracy: Eliminates human errors in manual attendance tracking.

Security: Uses NRIC for unique identification to prevent duplication.

Efficiency: Reduces the time required for manual attendance marking.

Accessibility: Attendance records can be accessed from anywhere.

Scalability: Can be extended with additional features like facial recognition or QR code scanning.

Location Verification: Prevents false attendance entries by ensuring users are within the camp premises.

7. Future Enhancements

The system can be further improved with the following features:

QR Code Integration: Attendees scan QR codes to mark attendance.

Facial Recognition: AI-based attendance marking using facial recognition.

Data Visualization: Dashboards for real-time attendance insights.

Mobile App Version: A mobile-friendly version for easier accessibility.

Role-based Access Control: Differentiated user roles for organizers and attendees.

Enhanced Geofencing: Advanced location-based authentication methods to improve security.

8. Conclusion

The Camp Attendance System provides an efficient, reliable, and secure method for managing attendance records. By automating the process, it significantly reduces administrative efforts and ensures accuracy in attendance tracking. The integration of location radius verification further enhances security by preventing false attendance submissions. Future improvements can further enhance usability, making it a robust solution for various organizational needs.

