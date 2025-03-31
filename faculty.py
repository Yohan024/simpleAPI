# faculty.py

from flask import Blueprint, jsonify
from db import get_db_connection

faculty_bp = Blueprint("faculty", __name__)

@faculty_bp.route("/faculty", methods=["GET"])
def get_faculty():
    """Fetch all faculty members from the database."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM faculty")
    faculty_list = cursor.fetchall()
    conn.close()
    
    if not faculty_list:
        return jsonify({"message": "No faculty found."}), 404
    
    return jsonify(faculty_list)
