import requests


base_url = 'http://127.0.0.1:5000'  # Replace with the correct URL if needed


def login(username, password):
    login_url = f'{base_url}/report/login'
    response = requests.post(login_url, json={'username': username, 'password': password})
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print('Login failed:', response.status_code, response.text)
        return None


def send_email_with_pdf(token, email, pdf_file_path):
    url = f'{base_url}/report/email'
    
    with open(pdf_file_path, 'rb') as pdf_file:
        files = {
            'pdf': (pdf_file_path, pdf_file, 'application/pdf')
        }
        data = {
            'email': email
        }
        
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.post(url, files=files, data=data, headers=headers)
        
        if response.status_code == 200:
            print('Success:', response.json())
        else:
            print('Failed:', response.status_code, response.text)

# Main execution
if __name__ == '__main__':
    username = 'user'  # Replace with the actual username
    password = 'password'  # Replace with the actual password
    email = ''  # Replace with the email address you want to send to
    pdf_file_path = ''  # Path to your test PDF file

    token = login(username, password)

    if token:
        
        send_email_with_pdf(token, email, pdf_file_path)
