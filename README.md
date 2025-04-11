# RPGen Backend

RPGen Backend is the server-side application for the RPGen project. It provides the core functionality, APIs, and services that support the RPGen Frontend for generating role-playing game content.

## Features

- **RESTful APIs:** Provides endpoints for managing RPG content generation and other backend services.
- **Built with Python (100%):** A robust and efficient backend leveraging Python's flexibility and power.
- **Scalable Architecture:** Designed to handle growing demands and additional features as the project evolves.
- **Secure and Reliable:** Implements best practices for security and error handling.

## Tech Stack

This project is entirely built using **Python**, ensuring a clean and efficient backend implementation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Gustavo-Cruzz/RPGen-back.git
   cd RPGen-back

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the application:
   ```bash
   python app.py

5. The backend will start, and you can access it at http://localhost:5000 (default port).


## API Endpoints
The backend provides the following key endpoints:

POST /api/gerar-texto: Receives a JSON to call the Gemini API and generate a Character's backstory
POST /api/gerar-imagem: Receives a JSON to call the Gemini API and generate a Character's image

## License
This project is licensed under the MIT License.
