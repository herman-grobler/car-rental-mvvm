# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a car rental application demonstrating a FastAPI backend with plans for a React TypeScript frontend following MVVM architecture. Currently, the project contains a fully functional backend API with comprehensive testing.

## Architecture

### Backend Architecture (Implemented)
FastAPI application with:
- **Single-file structure** in `backend/main.py` - all API logic in one file
- **SQLite database** with direct SQL queries (no ORM) stored in `cars.db`
- **Pydantic models** for request/response validation (`Car` model)
- **CORS middleware** configured for frontend communication on localhost:3000
- **Automatic database initialization** with sample data on startup
- **OpenAPI documentation** automatically generated at `/docs`

### Planned Frontend Architecture (MVVM Pattern)
When implemented, the frontend will follow MVVM pattern:
- **Model**: Type definitions for data structures
- **View**: React components (presentation layer)
- **ViewModel**: Custom React hooks (business logic and state management)
- **Service Layer**: API communication with backend

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

### Frontend (Not Yet Implemented)
Frontend directory exists but is empty. When implemented, typical commands will be:
```bash
# Create React app with TypeScript
npx create-react-app frontend --template typescript
cd frontend

# Start development server
npm start

# Run tests
npm test

# Build for production
npm run build
```

## Database

The backend uses SQLite with a file-based database (`cars.db`) that is automatically created and seeded with sample data on startup. The database contains a single `cars` table with fields: id, make, model, year, daily_rate, available.

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /cars` - Returns all available cars (only those with available=true)
- `GET /docs` - OpenAPI/Swagger documentation (auto-generated)
- Backend serves on `http://localhost:8000`
- Planned frontend will serve on `http://localhost:3000`

## Testing Strategy

### Backend Testing (Implemented)
- **Integration Tests**: Uses FastAPI TestClient in `test_main.py`
- **Database Isolation**: Tests use separate `test_cars.db` with fixtures
- **Test Coverage**: All API endpoints, data validation, and error scenarios
- **Pytest Fixtures**: Database setup/teardown for isolated testing
- **Test Categories**: Root endpoint, empty database, data retrieval, availability filtering

### Frontend Testing (Planned)
When implemented, will use:
- **Unit Tests**: Each layer (Service, ViewModel, Component) tested in isolation
- **Mocking**: Jest mocks for API calls and external dependencies
- **React Testing Library**: Component testing with user interaction simulation

## Code Organization

### Current Structure
```
backend/
├── main.py              # Complete FastAPI application
├── test_main.py         # Comprehensive test suite
├── requirements.txt     # Python dependencies
├── cars.db             # SQLite database (auto-generated)
└── .gitignore          # Python-specific ignores

frontend/               # Empty directory for future React app
```

### Key Files
- `backend/main.py` - Complete FastAPI application with database initialization
- `backend/test_main.py` - Comprehensive test suite with fixtures
- `backend/requirements.txt` - Python dependencies (FastAPI, Uvicorn, Pydantic, Pytest)

## Development Workflow

### Current Workflow (Backend Only)
1. **Setup**: Create virtual environment and install dependencies
2. **Development**: Run backend server with `python3 main.py`
3. **Testing**: Execute `python3 -m pytest test_main.py -v` before changes
4. **API Exploration**: Use auto-generated docs at `http://localhost:8000/docs`

### Future Full-Stack Workflow
1. **Backend First**: Ensure API endpoints are working
2. **Frontend Setup**: Create React app in `frontend/` directory
3. **Development**: Run both servers simultaneously (backend:8000, frontend:3000)
4. **Testing**: Run tests for both backend and frontend independently

## Common Development Patterns

### Adding Backend Features
1. **Define Pydantic Models**: Add data validation models in `main.py`
2. **Create API Endpoints**: Add FastAPI route handlers
3. **Update Database Schema**: Modify table creation in `init_db()`
4. **Write Tests**: Add corresponding test cases in `test_main.py`

### Current Error Handling
- **FastAPI**: Built-in HTTP exception handling and validation
- **Database**: Basic SQLite error handling with connection management
- **Testing**: Comprehensive error scenario coverage

## Dependencies

### Backend (Current)
- **FastAPI 0.104.1**: Modern web framework for building APIs
- **Uvicorn 0.24.0**: ASGI server for running FastAPI
- **Pydantic 2.5.0**: Data validation using Python type annotations
- **Pytest 7.4.3**: Testing framework
- **HTTPX 0.25.2**: HTTP client for testing API endpoints

### Frontend (Planned)
When implemented, will use:
- **React 18+**: Frontend framework with TypeScript
- **Axios or Fetch**: HTTP client for API requests
- **React Testing Library**: Component testing utilities
- **Jest or Vitest**: JavaScript testing framework

## Development Environment

### Current Setup
- **Backend**: `http://localhost:8000` (API and auto-docs at `/docs`)
- **Database**: SQLite file (`cars.db`) in backend directory
- **CORS**: Pre-configured for `http://localhost:3000` frontend

### Virtual Environment Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Quality
A task is not complete unless:
- All tests pass
- Linting is clean
- No build errors exist

## Using Playwright
Use Playwright to verify designs by default when building front-ends based off Figma designs.

## Advanced planning workflow
When I ask you to use advanced planning, use three different agents. The first two should come up with different implementation plans, the third is the decision maker that chooses the best option and presents it to me for approval before implementation is allowed to start.

## TDD ping-pong workflow
When I ask you to use TDD ping-pong, run two agents. AgentOne writes the unit tests that fail. AgentTwo writes the implementation code. AgentOne then refactors the code according to Clean Code principles and writes the next unit test again. For collaboration, AgentOne can create and write to the file "AgentOneScratchPad" as a scratchpad. AgentTwo can create and write to the file "AgentTwoScratchPad" as a scratchpad. AgentOne reads from AgentTwoScratchPad. AgentTwo reads from AgentOneScratchPad.