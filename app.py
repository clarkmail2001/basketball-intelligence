from flask import Flask, render_template, jsonify
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('PGHOST'),
        database=os.environ.get('PGDATABASE'),
        user=os.environ.get('PGUSER'),
        password=os.environ.get('PGPASSWORD'),
        port=os.environ.get('PGPORT')
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/teams')
def get_teams():
    # Placeholder - will fetch from database
    teams = [
        {'name': 'Cleveland Cavaliers', 'abbr': 'CLE', 'league': 'NBA'},
        {'name': 'Oklahoma City Thunder', 'abbr': 'OKC', 'league': 'NBA'},
        {'name': 'Boston Celtics', 'abbr': 'BOS', 'league': 'NBA'}
    ]
    return jsonify(teams)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
