# Data Sorting Assistant

A Flask-powered web application that leverages AI to intelligently organize, clean, and structure messy data from various sources.

## What This Project Does

The Data Sorting Assistant helps transform chaotic data into clean, organized, and actionable information. Users can either upload files (CSV, TXT, etc.) or paste text directly, and the AI will analyze patterns, identify inconsistencies, and provide structured recommendations for data organization.

## Technologies Used

### Backend
- **Flask** - Python web framework for handling routes and server logic
- **Cohere AI API** - Advanced language model for intelligent data analysis and sorting recommendations
- **Python-dotenv** - Environment variable management for secure API key storage

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling with responsive design
- **Vanilla JavaScript** - Client-side interactivity and form handling

### Development Tools
- **Virtual Environment (venv)** - Isolated Python environment for dependency management
- **Git** - Version control
- **Environment Variables** - Secure configuration management

## What I Learned

### Core Concepts
1. **Flask Web Development** - Building routes, handling HTTP requests, and rendering templates
2. **AI Integration** - Working with external APIs and prompt engineering for specific tasks
3. **File Upload Handling** - Processing user-uploaded files in web applications
4. **Environment Configuration** - Secure API key management using `.env` files
5. **Full-Stack Development** - Connecting frontend forms with backend processing

### Technical Skills
- **HTTP Methods** - Understanding GET vs POST requests and when to use each
- **Form Data Processing** - Extracting and validating user input from web forms
- **Template Rendering** - Using Jinja2 templates to dynamically display content
- **Error Handling** - Implementing basic validation and user feedback
- **Project Structure** - Organizing a web application with proper file hierarchy

## Challenges Faced

### File Upload Implementation
The biggest challenge was implementing file upload functionality, as this was completely new territory for me. Key hurdles included:

- **Understanding `request.files`** - Learning how Flask handles multipart form data
- **File Reading and Encoding** - Converting uploaded files to readable text format using `.decode('utf-8')`
- **Error Handling** - Validating file uploads and providing meaningful error messages
- **Form Processing** - Managing both file uploads and text input in the same application

### AI Integration
- **Prompt Engineering** - Crafting effective prompts to get consistent, useful responses from the AI
- **API Configuration** - Setting up Cohere client with proper authentication
- **Response Handling** - Processing and displaying AI responses in a user-friendly format

### Frontend-Backend Communication
- **Form Submission** - Ensuring proper data flow between HTML forms and Flask routes
- **Dynamic Content** - Displaying AI responses without page refresh complexity
- **User Experience** - Creating an intuitive interface for both file upload and text input options

## Features

- **Dual Input Methods**: Upload files or paste text directly
- **AI-Powered Analysis**: Intelligent data sorting and cleaning recommendations
- **Clean UI**: Modern, responsive design with intuitive user experience
- **Flexible Processing**: Handles various data formats and structures
- **Custom Instructions**: Users can provide specific sorting requirements

## Project Structure

```
Datasorter/
├── main.py              # Flask application and routes
├── templates/
│   └── index.html       # Frontend interface
├── .env                 # Environment variables (API keys)
├── .gitignore          # Git ignore rules
├── test.txt            # Sample data for testing
└── venv/               # Virtual environment
```

## Setup and Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install flask cohere python-dotenv`
5. Create `.env` file with your Cohere API key: `COHERE_API_KEY=your_api_key_here`
6. Run the application: `python main.py`
7. Open `http://localhost:5000` in your browser

## Key Takeaways

This project was an excellent introduction to:
- **Web development fundamentals** with Flask
- **AI API integration** and prompt engineering
- **File handling** in web applications
- **Full-stack thinking** - considering both user experience and backend logic
- **Environment security** - protecting sensitive information like API keys

The file upload feature was particularly educational, teaching me about HTTP multipart forms, file processing, and the importance of proper error handling in web applications.

## Future Improvements

- Add support for more file formats (Excel, JSON)
- Implement data visualization features
- Add user authentication and data persistence
- Create downloadable output files
- Enhance error handling and user feedback

---

*This project represents my journey into web development and AI integration, with a focus on practical data management solutions.*
