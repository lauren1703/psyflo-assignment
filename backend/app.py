from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_PATH = "database.db"
USER_ID = 1  # Simulate single persistent user

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS moods (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        mood TEXT,
        date TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS modules (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        module_name TEXT,
        date_completed TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/mood', methods=['POST'])
def add_mood():
    data = request.json
    mood = data['mood']
    date = datetime.now().date().isoformat()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO moods (user_id, mood, date) VALUES (?, ?, ?)",
                 (USER_ID, mood, date))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/mood', methods=['GET'])
def get_moods():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT mood, date FROM moods WHERE user_id = ? ORDER BY date DESC", (USER_ID,))
    data = cursor.fetchall()
    conn.close()
    return jsonify([{'mood': mood, 'date': date} for mood, date in data])

@app.route('/module', methods=['POST'])
def complete_module():
    data = request.json
    module_name = data['module_name']
    date_completed = datetime.now().date().isoformat()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO modules (user_id, module_name, date_completed) VALUES (?, ?, ?)",
                 (USER_ID, module_name, date_completed))
    conn.commit()
    conn.close()
    return jsonify({'status': 'completed'})

@app.route('/module', methods=['GET'])
def get_completed_modules():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT module_name, date_completed FROM modules WHERE user_id = ?", (USER_ID,))
    data = cursor.fetchall()
    conn.close()
    return jsonify([{'module': name, 'date': date} for name, date in data])

@app.route('/module/<module_name>', methods=['DELETE'])
def delete_module(module_name):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("DELETE FROM modules WHERE user_id = ? AND module_name = ?",
                    (USER_ID, module_name))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
