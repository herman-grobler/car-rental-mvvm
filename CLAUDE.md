# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a car rental application demonstrating MVVM architecture with a React TypeScript frontend and FastAPI backend. The project is structured as two independent applications that communicate via REST API.

## Architecture

### MVVM Pattern Implementation
The frontend follows a strict MVVM pattern:
- **Model**: Type definitions in `src/types/index.ts`
- **View**: React components in `src/components/` (presentation layer)
- **ViewModel**: Custom React hooks in `src/viewmodels/` (business logic and state management)
- **Service Layer**: API communication in `src/services/`

### Backend Architecture
Simple FastAPI application with:
- Single-file structure in `main.py`
- SQLite database with direct queries (no ORM)
- Pydantic models for validation
- CORS configured for frontend communication

## Development Commands

### Backend
```bash
# Start development server
cd backend
python3 main.py

# Run tests
python3 -m pytest test_main.py -v

# Install dependencies (requires virtual environment)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend
```bash
# Start development server (port 3000)
cd frontend
npm start

# Run tests
npm test

# Run specific test file
npm test -- --testPathPattern="CarService"

# Run tests without watch mode
npm test -- --watchAll=false

# Build for production
npm run build

# Install dependencies
npm install
```

## Database

The backend uses SQLite with a file-based database (`cars.db`) that is automatically created and seeded with sample data on startup. The database contains a single `cars` table with fields: id, make, model, year, daily_rate, available.

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /cars` - Returns all available cars
- Backend serves on `http://localhost:8000`
- Frontend serves on `http://localhost:3000`

## Testing Strategy

### Frontend Testing
- **Unit Tests**: Each layer (Service, ViewModel, Component) has isolated unit tests
- **Mocking**: Uses Jest mocks for external dependencies (axios, API calls)
- **Test Structure**: Tests are co-located with source files in `__tests__/` directories
- **Coverage**: Tests loading states, error handling, and successful data flow

### Backend Testing
- **Integration Tests**: Uses FastAPI TestClient for endpoint testing
- **Database Isolation**: Tests use separate test database with fixtures
- **Test Coverage**: API endpoints, data validation, error scenarios

## Code Organization

### Frontend Structure
```
src/
├── components/          # React components (View layer)
├── viewmodels/         # Custom hooks (ViewModel layer)
├── services/           # API communication (Service layer)
├── types/              # TypeScript definitions (Model layer)
└── __tests__/          # Test files co-located with source
```

### Key Files
- `src/viewmodels/CarViewModel.ts` - Manages car data state and API calls
- `src/services/CarService.ts` - Handles API requests to backend
- `src/components/CarList.tsx` - Displays car data in grid layout
- `backend/main.py` - Complete FastAPI application with database

## Development Workflow

1. **Backend First**: Start backend server to provide API endpoints
2. **Frontend Development**: Frontend fetches data from backend API
3. **Testing**: Run tests for both frontend and backend independently
4. **Type Safety**: Shared Car interface ensures consistent data structure

## Common Development Patterns

### Adding New Features
1. Define types in `src/types/index.ts`
2. Create service methods in `src/services/`
3. Implement ViewModel hooks in `src/viewmodels/`
4. Build View components in `src/components/`
5. Add corresponding tests for each layer

### Error Handling
- ViewModels handle API errors and provide error states to components
- Components display loading and error states appropriately
- Backend uses FastAPI's built-in error handling

## Dependencies

### Backend
- FastAPI for web framework
- Uvicorn for ASGI server
- Pydantic for data validation
- pytest + httpx for testing

### Frontend
- React 19 with TypeScript
- Axios for HTTP requests
- React Testing Library for testing
- Jest for test runner

## Development Environment

Both servers run simultaneously during development:
- Backend: `http://localhost:8000` (API and auto-docs)
- Frontend: `http://localhost:3000` (React dev server)

CORS is configured to allow frontend-backend communication in development.