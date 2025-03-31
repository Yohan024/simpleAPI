# Faculty API (Flask + MySQL)

This is a REST API built using Flask and MySQL to fetch faculty details.

## 🚀 Setup Instructions

1. **Clone the repository**  
   ```sh
   git clone <your-repo-link>
   cd <your-project-folder>
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**  
   - Create a MySQL database  
   - Import `schema.sql` file  

4. **Configure the database connection** in `config.py`  
   ```python
   DB_HOST = "localhost"
   DB_USER = "your_username"
   DB_PASSWORD = "your_password"
   DB_NAME = "your_database"
   ```

5. **Run the API**  
   ```sh
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

## 🤝 Contribution
Feel free to contribute! Fork the repo and submit a pull request.

