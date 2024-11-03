# Daily Expenses Sharing Application

A backend application for managing daily expenses between users, allowing them to split expenses equally, by exact amounts, or by percentages. Users can track and download balance sheets for expenses.

## Features

- **User Management**: Add and retrieve user details.
- **Expense Management**: Add expenses, retrieve individual and overall expenses, and download balance sheets.
- **Splitting Methods**: Supports equal, exact, and percentage-based splits.
- **Balance Sheet Download**: Generate and download a balance sheet with each user’s total expenses.

## Prerequisites

- Python 3.6+
- Django 3.2+
- Django REST Framework

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mehtachandrashekhar/Daily-Expense-Sharing-Application.git
   cd daily_expenses_app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

4. **Database Setup**:
   - **Run Migrations** to set up the database.
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Create a Superuser (Optional)**:
   - This step allows you to access the Django Admin interface.
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

   The application should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

### User Endpoints
- **Create a User**: `POST /api/users/`
- **Retrieve User Details**: `GET /api/users/{id}/`

### Expense Endpoints
- **Add an Expense**: `POST /api/expenses/`
- **Retrieve Overall Expenses**: `GET /api/expenses/overall_expenses/`
- **Download Balance Sheet**: `GET /api/expenses/download_balance_sheet/`

## Sample Request Payloads

### Create a User
```json
POST /api/users/
{
  "email": "john@example.com",
  "name": "John Doe",
  "mobile_number": "1234567890"
}
```

### Add an Expense
```json
POST /api/expenses/
{
  "amount": 500.0,
  "method": "equal",
  "user": 1,  // ID of the user creating the expense
  "description": "Dinner expense",
  "participants": [1, 2, 3],  // IDs of participating users
  "exact_amounts": null,  // Required for "exact" split method
  "percentage_amounts": null  // Required for "percentage" split method
}
```

## Running Tests

1. To run the tests, execute:
   ```bash
   python manage.py test
   ```

## Additional Information

- **Admin Access**: Access the Django Admin interface at `/admin/`.
- **Error Handling**: Basic validation and error responses are provided for required fields and validation rules.
