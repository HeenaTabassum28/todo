# Flask Todo App

A simple Todo web application built with Flask and SQLAlchemy.

## Features

- Add, update, delete, and edit todo items
- Mark todos as complete/incomplete
- Inline editing of todos on the main page
- SQLite database for persistent storage
- Responsive and clean UI

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo/src
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```sh
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
src/
├── app.py
├── requirements.txt
├── templates/
│   └── base.html
├── static/
│   └── style.css
```

## License

This project is licensed under the MIT License.