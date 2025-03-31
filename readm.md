# Faculty API (Flask + MySQL)

This is a REST API built using Flask and MySQL to fetch faculty details.

## 🚀 Setup Instructions

1. **Clone the repository**  
    

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**  
   - Create a MySQL database  
   - 
    CREATE DATABASE srm_faculty_db;
    USE srm_faculty_db;

    CREATE TABLE faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department VARCHAR(255),
    designation VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    profile_link TEXT
);

    INSERT INTO faculty (name, department, designation, email, phone, profile_link)
    VALUES 
    ('Dr. John Doe', 'Computer Science', 'Professor', 'johndoe@srmist.edu.in', '9876543210', 'https://srmist.irins.org/faculty/123'),
    ('Dr. Jane Smith', 'Artificial Intelligence', 'Associate Professor', 'janesmith@srmist.edu.in', '9876543211', 'https://srmist.irins.org/faculty/124');


4. **Configure the database connection** in `config.py`  
   ```python
   DB_HOST = "localhost"
   DB_USER = "your_username"
   DB_PASSWORD = "your_password"
   DB_NAME = "your_database"
   ```

5. **Run the API**  
   ```
   IN VS CODE
   python app.py
   ```
   The server will start at: `http://127.0.0.1:5000/`

## 📌 API Endpoints

| Method | Endpoint         | Description               |
|--------|-----------------|---------------------------|
| GET    | `/faculty`      | Get all faculty data      |
| GET    | `/faculty/<id>` | Get a faculty by ID       |

## 🛠 Technologies Used
- Flask
- MySQL
- MySQL Connector
- RESTful API



