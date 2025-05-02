# Psyflo - Mood Tracking and Therapeutic Learning Platform

## Project Overview

Psyflo is a web-based application designed to help users track their emotional well-being and engage with therapeutic learning modules. The platform addresses the need for accessible mental health tools by providing:

- Daily mood tracking with intuitive emoji-based selection
- Structured therapeutic learning modules
- Historical tracking of both mood states and learning progress

### Problem Statement

Many individuals struggle to maintain awareness of their emotional states and lack easy access to therapeutic techniques. Psyflo bridges this gap by offering a simple, user-friendly interface for both mood tracking and therapeutic learning.

## Technical Stack

### Frontend
- **React.js**: Chosen for its component-based architecture and efficient state management
- **Axios**: For handling HTTP requests
- **CSS3**: Custom styling with modern features like gradients and transitions

### Backend
- **Flask**: Lightweight Python web framework, perfect for rapid development
- **SQLite**: Simple, file-based database ideal for the project scope
- **Flask-CORS**: Handling Cross-Origin Resource Sharing

### Rationale for Technical Choices
- **React**: Enables rapid development of interactive UIs with reusable components
- **Flask**: Minimalist framework that's quick to set up and easy to extend
- **SQLite**: File-based database that requires no separate server, simplifying deployment

## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js and npm
- Git

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```
   The server will start on http://localhost:5000

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```
   The application will open in your browser at http://localhost:3000

## Data Persistence

### Implementation
- SQLite database with two main tables:
  - `moods`: Stores user mood entries with timestamps
  - `modules`: Tracks completed learning modules
- File-based storage requiring no additional configuration
- Automatic database initialization on first run

### Schema
```sql
CREATE TABLE moods (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    mood TEXT,
    date TEXT
);

CREATE TABLE modules (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    module_name TEXT,
    date_completed TEXT
);
```

## Assumptions and Trade-offs

### Assumptions
- Single user system (no authentication implemented)
- Local deployment environment
- Modern browser support (CSS3 features)

### Trade-offs
1. **Simplicity vs. Features**
   - Focused on core functionality over additional features
   - Limited to basic mood options and fixed learning modules

2. **Database Choice**
   - Used SQLite for simplicity over scalable alternatives
   - Sacrificed multi-user support for easier deployment

3. **UI/UX**
   - Prioritized usability over complex visualizations
   - Limited historical data analysis features

## Development Time

Total development time: Approximately 2 hours

## AI Tool Usage

This project was developed with assistance from:
- GitHub Copilot: Code suggestions and completion
- Claude AI: Project structure guidance and documentation help

The AI tools were primarily used for:
- Boilerplate code generation
- Documentation writing
- CSS styling suggestions
- Debugging assistance