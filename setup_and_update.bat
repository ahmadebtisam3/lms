if not exist .env ( python -m venv .env )

.\.env\Scripts\pip.exe install -r .\lms\requirements.txt
.\.env\Scripts\python.exe .\lms\manage.py migrate
npm install
