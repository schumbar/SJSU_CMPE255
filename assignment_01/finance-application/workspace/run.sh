# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the Django server
python manage.py runserver

# Navigate to the frontend directory
cd frontend

# Install the dependencies
npm install

# Run the React app
npm start
