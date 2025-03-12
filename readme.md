# Inside.Io 3D Model Manager  

A Django REST API backend for uploading, storing, and managing 3D model files. This application enables developers to integrate 3D model capabilities into their applications through a simple REST API.  

## Features  

- Upload and validate 3D model files (.obj, .gltf, .glb)  
- Retrieve 3D models with download URLs  
- RESTful API with full CRUD operations  
- File format validation and automatic metadata extraction  
- Cross-Origin Resource Sharing (CORS) enabled for frontend integration  

## Installation  

### Prerequisites  

- Python 3.8 or higher  
- pip (Python package manager)  
- Git (optional, for cloning the repository)  

### Step 1: Get the Code  

Clone the repository or download the source code:  

```bash
git clone https://github.com/your-username/Inside.Io.git
cd Inside.Io/BackEnd
```  

### Step 2: Set Up a Virtual Environment  

Create and activate a virtual environment:  

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```  

### Step 3: Install Dependencies  

Install all required packages:  

```bash
pip install -r requirements.txt
```  

### Step 4: Initialize the Database  

Run migrations to set up the database:  

```bash
python manage.py migrate
```  

### Step 5: Start the Development Server  

Launch the application:  

```bash
python manage.py runserver
```  

The API will be available at http://localhost:8000/api/  
The admin interface will be at http://localhost:8000/admin/  

## API Endpoints  

- `GET /api/models/` - List all 3D models  
- `POST /api/models/` - Upload a new 3D model  
- `GET /api/models/<id>/` - Retrieve a specific 3D model  
 

## Project Structure  

```
BackEnd/
├── backend/             # Django project settings
├── threeDapp/           # Django app for 3D model handling
├── media/               # Uploaded files storage
│   └── models/          # 3D model files
├── templates/           # HTML templates
└── manage.py            # Django management script
```  

## Technologies Used  

- Django  
- Django REST Framework  
- Python  
- SQLite (development) / PostgreSQL (production)  

## License  

MIT  