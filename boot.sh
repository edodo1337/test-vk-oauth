source venv/bin/activate

exec gunicorn -b 0.0.0.0:$PORT --access-logfile - --error-logfile - "backend:create_app()"