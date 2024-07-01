# Subscription API

This application provides a simple Subscription API built with Flask. It includes endpoints for creating and extending user subscriptions, ensuring proper data validation and handling through the use of Pydantic and other utilities.

## Getting Started

### Prerequisites

- Python 3.6 or later
- `virtualenv` or `venv` for creating virtual environments

### Installing and Running

Clone the repository:

   ```bash
   git@github.com:hitesharora1997/Feelme_ai_subsciption.git
   cd Feelme_ai_subsciption
   ```

Create a virtual environment and install dependencies:
   ```bash
   make setup
   ```

Run the application:
   ```bash
   make run
   ```

To run the test:
   ```bash
   make test
   ```
To see the test coverage:
   ```bash
   make coverage
   ```

Building Docker Image
   ```bash
   make docker
   ```

Cleaning up the virtual environment and other generated files:
   ```bash
   make clean
   ```

### Application Overview
The application provides a RESTful API for managing subscriptions. It includes endpoints for creating new subscriptions and extending existing ones, with proper authentication and validation.

> **Note:** For demo purposes, the authorized key for authentication are currently hardcoded in the code. In a production environment, these should be securely managed and stored.

### API Endpoints

#### Create Subscription
* URL: `/api/v1/subscription`
* Method: `POST`
* Headers: `Authorization: personalkey`
* Request Body: 
   ```bash
   {
    "user_external_id": "123",
    "user_email": "user@example.com",
    "duration": 1,
    "start_date": "2024-06-29"
   }
   ```
* Response:
   * `201 Created`:
   ```bash
   {
    "message": "Subscription created",
    "subscription_id": "123"
   }
   ```
   * `422 Unprocessable Entity`: Validation errors
   * `400 Bad Request`: Unexpected errors

#### Extend Subscription
* URL: `/api/v1/subscription`
* Method: `PUT`
* Headers: `Authorization: personalkey`
* Request Body: 
   ```bash
   {
    "user_external_id": "123",
    "duration": 1
   }
   ```
* Response:
   * `200 OK`:
   ```bash
   {
    "message": "Subscription extended",
    "new_end_date": "2024-07-29"
   }
   ```
   * `404 Not Found`: Subscription not found
   * `422 Unprocessable Entity`: Validation errors
   * `400 Bad Request`: Unexpected errors

### Project Structure
* `app/`: Contains the main application code.
* `tests/`: Contains the unit tests.
* `Makefile`: Automates setup, installation, running, testing, and cleaning tasks.


### Caveats and Limitations
* Concurrency Handling: Currently handles basic concurrency. Future versions could aim to improve this for high-load scenarios with benchmark tests.
* Error Handling: Basic error handling implemented; can be improved with more contextual errors.
* Testing Coverage: Good coverage for major functionalities. Edge cases and stress conditions can be further improved.
* Code Maintainability: The code is structured for maintainability, with ongoing efforts to improve documentation and code clarity.
* Data Persistence: Currently, data is stored in memory during runtime and is not persisted after the application stops.