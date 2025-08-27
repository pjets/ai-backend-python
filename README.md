<<<<<<< HEAD
# Hello World Backend API

A simple Python backend API built with FastAPI that provides a Hello World endpoint and user authentication functionality.

## Features

- GET / - Hello World endpoint
- GET /health - Health check endpoint
- POST /register - User registration
- POST /login - User authentication with JWT tokens
- GET /profile - Protected user profile endpoint
- CORS enabled for cross-origin requests
- Auto-generated API documentation
- JWT-based authentication
- Password hashing with bcrypt

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The application uses environment variables for configuration. Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-change-this-in-production-make-it-very-long-and-random
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

### Option 1: Using Python directly
```bash
python main.py
```

### Option 2: Using Uvicorn
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- Main endpoint: http://localhost:8000/
- Health check: http://localhost:8000/health
- API Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## API Endpoints

### GET /
Returns a Hello World message.

**Response:**
```json
{
  "message": "Hello World!",
  "status": "success"
}
```

### GET /health
Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

### POST /register
Register a new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "fullname": "John Doe",
  "phone_number": "0812345678",
  "birthday": "1990-01-01"
}
```

**Response:**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "fullname": "John Doe",
  "phone_number": "0812345678",
  "birthday": "1990-01-01",
  "created_at": "2025-08-27T10:30:00"
}
```

### POST /login
Authenticate user and get JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "jwt-token-string",
  "token_type": "bearer"
}
```

### GET /profile
Get user profile (requires authentication).

**Headers:**
```
Authorization: Bearer your-jwt-token
```

**Response:**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "fullname": "John Doe",
  "phone_number": "0812345678",
  "birthday": "1990-01-01",
  "created_at": "2025-08-27T10:30:00"
}
```

## Testing

You can test the authentication endpoints using the provided test script:

```bash
python test_auth.py
```

Or use curl commands:

```bash
# Register a user
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpassword",
    "fullname": "Test User",
    "phone_number": "0812345678",
    "birthday": "1990-01-01"
  }'

# Login
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "testpassword"
  }'

# Get profile (replace TOKEN with actual token from login)
curl -X GET "http://localhost:8000/profile" \
  -H "Authorization: Bearer TOKEN"
```

## Development

The application uses FastAPI with automatic reload enabled for development. Any changes to the code will automatically restart the server.

## Security Features

- Passwords are hashed using bcrypt
- JWT tokens for stateless authentication
- Protected endpoints require valid JWT tokens
- Configurable token expiration time
- Email validation for user registration
=======
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      ...tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      ...tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      ...tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default tseslint.config([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
>>>>>>> bb60185a6213a803cf9c417a19995cbf1ae39c20
