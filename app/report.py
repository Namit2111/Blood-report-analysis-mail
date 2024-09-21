from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os
import threading
from werkzeug.utils import secure_filename
from crewai import Crew, Process
from agents.agents import gemini_agent, google_query_agent, query_review, best_article_agent, answer_agent, email_agent
from tasks.task import extract_patient_data_task, create_google_query_task, review_google_query, find_related_articles, find_cure, send_email_task 
from tools.extract import extract_pdf
from config.config import a_user, a_password


report = Blueprint('report', __name__, url_prefix='/report')

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def run_crew_in_background(extracted_data, email):
    myCrew = Crew(
        agents=[gemini_agent, google_query_agent, query_review, best_article_agent, answer_agent, email_agent],
        tasks=[extract_patient_data_task, create_google_query_task, review_google_query, find_related_articles, find_cure, send_email_task],
        verbose=True,
        process=Process.sequential,
    )
    myCrew.kickoff(inputs={"data": extracted_data, 'email': email})

@report.route('/email', methods=['POST'])
@jwt_required()  # Protect the endpoint with JWT authentication
def email_report():
    pdf_file = request.files['pdf']
    email = request.form['email']

    # Check for PDF file type
    if not pdf_file.filename.endswith('.pdf'):
        return jsonify({'error': 'Invalid file type. Please upload a PDF.'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, secure_filename(pdf_file.filename))
    pdf_file.save(file_path)

    # Extract data from PDF
    try:
        extracted_data = extract_pdf(file_path)
    except Exception as e:
        return jsonify({'error': 'Failed to extract data from PDF.'}), 500

    # Run the crew process in a separate thread
    thread = threading.Thread(target=run_crew_in_background, args=(extracted_data, email))
    thread.start()

    return jsonify({'message': 'You will receive an email soon'}), 200

@report.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Placeholder validation for the assignment
    if username == a_user and password == a_password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
