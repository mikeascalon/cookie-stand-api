# LAB - Class 34

## Project: “Vanilla” Django and Django REST Framework

### Author: Michelangelo Ascalon

## Overview
This project demonstrates the use of Django alongside Django REST Framework to create a robust API for managing cookie stands. It utilizes Docker for easy setup and deployment, providing a seamless development experience.

## Setup

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Basic understanding of Docker, Django, and Django REST Framework.

### Installation
1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Build and start the containers with Docker Compose:
   ```
   docker-compose up --build
   ```

## Access and Testing
The API is accessible at: `http://127.0.0.1:8000/api/v1/cookieStands`

## Notes
- Ensure Docker is running on your machine before starting the application.
- Adjust `docker-compose.yml` according to your database preference (SQLite or PostgreSQL).
- Static files are served using Whitenoise; ensure your static file paths are correctly set in settings for production.

## Database Hosting
- The database is hosted at ElephantSQL.

## Superuser for Testing
- To test as a superuser, use the username `admin` and the password `admin`.