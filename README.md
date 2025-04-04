# Healthcare Backend

A comprehensive healthcare management system backend built with Django and Django REST Framework. This system allows for secure user authentication, patient management, doctor directory, and patient-doctor relationship management.

## Project Overview

This Django-based REST API provides a backend system for healthcare applications with features including:
- JWT-based user authentication
- Patient record management
- Doctor directory
- Patient-doctor relationship mapping
- Role-based data access controls

## Technology Stack

- **Framework**: Django 5.1+, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Security**: Environment variables for sensitive configuration

## Project Structure

```
backend/
├── authentication/       # User authentication app
├── patients/            # Patient management app
├── doctors/             # Doctor management app
├── mappings/            # Patient-doctor relationship management
└── healthcare/          # Main project configuration
```

## Features

### Authentication
- User registration with secure password handling
- JWT-based login system
- Token refresh functionality

### Patient Management
- Create, read, update, and delete patient records
- Patients are associated with the user who created them
- Data validation for all patient fields

### Doctor Directory
- Complete doctor information management
- Searchable doctor database
- Validation for doctor contact information

### Patient-Doctor Mappings
- Assign doctors to patients
- View all doctors assigned to a specific patient
- Prevent duplicate assignments

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Authenticate and receive JWT tokens

### Patient Management
- `GET /api/patients/` - List all patients (filtered by authenticated user)
- `POST /api/patients/` - Create a new patient
- `GET /api/patients/<id>/` - Retrieve a specific patient
- `PUT /api/patients/<id>/` - Update a patient record
- `DELETE /api/patients/<id>/` - Delete a patient record

### Doctor Management
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create a new doctor
- `GET /api/doctors/<id>/` - Retrieve a specific doctor
- `PUT /api/doctors/<id>/` - Update a doctor record
- `DELETE /api/doctors/<id>/` - Delete a doctor record

### Mappings
- `GET /api/mappings/` - List all patient-doctor mappings
- `POST /api/mappings/` - Create a new patient-doctor mapping
- `GET /api/mappings/<id>/` - Retrieve a specific mapping
- `DELETE /api/mappings/<id>/` - Delete a mapping
- `GET /api/mappings/patient/<patient_id>/` - List all doctors for a specific patient

## Setup and Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/afnan006/HealthCare_006.git
   cd healthcare-backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

## Testing

The project includes comprehensive tests for all features:

```
python manage.py test
```

## Security Features

- Password hashing using Django's built-in security features
- JWT token-based authentication
- Database credentials stored as environment variables
- User-based data access restrictions

## Future Enhancements

- Appointment scheduling system
- Medical records management
- Prescription system
- Patient portal features
- Analytics dashboard

## License

MIT License

## Contributors

- [Afnan](https://github.com/afnan006)
