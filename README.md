# Data Sorting Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)
![AI](https://img.shields.io/badge/AI-Cohere-purple.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> Transform chaotic data into clean, organized, and actionable information with AI-powered intelligence.

---

## 📋 Project Overview

The **Data Sorting Assistant** is a Flask-powered web application that leverages the Cohere AI API to intelligently organize, clean, and structure messy data from various sources. This full-stack application provides an intuitive interface for users to upload files or paste text directly, receiving AI-driven recommendations for data organization and cleaning.

---

## 🎯 Purpose

This project was developed to:
- Learn full-stack web development fundamentals with Flask
- Explore AI API integration and prompt engineering techniques
- Master file upload handling in web applications
- Practice secure environment configuration and API key management
- Build a practical tool that addresses real-world data organization challenges

The Data Sorting Assistant serves as both a learning project and a functional utility for anyone dealing with unstructured or messy data that needs intelligent organization.

---

## ✨ Features

### Core Functionality
- **Dual Input Methods**: Upload files (CSV, TXT, etc.) or paste text directly into the interface
- **AI-Powered Analysis**: Leverages Cohere's language model for intelligent pattern recognition and data sorting
- **Smart Recommendations**: Receives structured suggestions for organizing and cleaning data
- **Custom Instructions**: Provide specific sorting requirements to tailor AI recommendations
- **Flexible Processing**: Handles various data formats and structures seamlessly

### User Experience
- **Clean, Modern UI**: Responsive design with intuitive navigation
- **Real-time Processing**: Fast AI analysis and response generation
- **Error Handling**: Comprehensive validation and user-friendly error messages
- **Multipart Form Support**: Robust file upload handling with proper encoding

---

## 🛠️ Tech Stack

### Backend
- **Flask**: Python web framework for routing and server-side logic
- **Cohere AI API**: Advanced language model for intelligent data analysis
- **Python-dotenv**: Secure environment variable management

### Frontend
- **HTML5**: Semantic markup for structured content
- **CSS3**: Modern styling with responsive design principles
- **Vanilla JavaScript**: Client-side interactivity and form handling

### Development Tools
- **Virtual Environment (venv)**: Isolated Python dependency management
- **Git**: Version control and project tracking
- **.env Configuration**: Secure API key storage and environment management

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Cohere API key (sign up at [cohere.ai](https://cohere.ai))
- Git (optional, for cloning)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kyleyuen/Datasorter.git
   cd Datasorter
   ```

2. **Create and activate virtual environment**
   
   On macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask cohere python-dotenv
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```
   COHERE_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   
   Open your browser and navigate to: `http://localhost:5000`

---

## 📖 Usage Guide

### Option 1: File Upload
1. Navigate to the application homepage
2. Click the file upload button or drag-and-drop a file (CSV, TXT, etc.)
3. Optionally provide custom sorting instructions
4. Click "Analyze" to process your data
5. Review AI-generated recommendations and organized output

### Option 2: Direct Text Input
1. Navigate to the application homepage
2. Paste your unorganized data directly into the text area
3. Optionally provide custom sorting instructions
4. Click "Analyze" to process your data
5. Review AI-generated recommendations and organized output

### Sample Test Data
The repository includes `test.txt` with sample data for testing the application's capabilities.

---

## 📚 Learning Outcomes

### Core Concepts Mastered
1. **Flask Web Development**
   - Building routes and handling HTTP requests (GET/POST)
   - Rendering Jinja2 templates with dynamic content
   - Form data processing and validation

2. **AI Integration**
   - Working with external APIs and authentication
   - Prompt engineering for consistent AI responses
   - Response handling and display formatting

3. **File Upload Handling**
   - Understanding Flask's `request.files` for multipart form data
   - File reading and encoding (`.decode('utf-8')`)
   - Validating uploads and providing error feedback

4. **Environment Security**
   - Managing API keys with `.env` files
   - Implementing secure configuration practices
   - Protecting sensitive information

5. **Full-Stack Development**
   - Connecting frontend forms with backend processing
   - Managing both user interface and server logic
   - Creating seamless user experiences

### Technical Skills Developed
- HTTP protocol understanding (GET vs POST methods)
- Form data extraction and validation
- Template rendering with Jinja2
- Error handling and user feedback mechanisms
- Project structure and file organization
- Multipart form processing
- Client-server communication patterns

### Key Challenges Overcome
- **File Upload Implementation**: Learning Flask's file handling mechanisms from scratch
- **AI Prompt Engineering**: Crafting prompts for consistent, useful responses
- **Frontend-Backend Communication**: Ensuring smooth data flow between layers
- **Error Handling**: Building robust validation and user-friendly error messages

---

## 🔮 Future Enhancements

- [ ] **Expanded File Format Support**: Add Excel (.xlsx), JSON, and XML parsing
- [ ] **Data Visualization**: Implement charts and graphs for cleaned data
- [ ] **User Authentication**: Add login system for personalized experiences
- [ ] **Data Persistence**: Store user uploads and analysis history
- [ ] **Downloadable Output**: Generate formatted files (CSV, Excel) from cleaned data
- [ ] **Batch Processing**: Support multiple file uploads simultaneously
- [ ] **Advanced AI Features**: Add data validation, anomaly detection, and predictive insights
- [ ] **API Endpoint**: Create RESTful API for programmatic access
- [ ] **Improved Error Handling**: Enhanced validation and detailed error reporting
- [ ] **Dark Mode**: Theme toggle for user preference

---

## 📊 Technical Specifications

| Category | Details |
|----------|--------|
| **Language** | Python 3.x |
| **Framework** | Flask 2.x |
| **AI Service** | Cohere API |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Template Engine** | Jinja2 |
| **Environment** | Python-dotenv |
| **Supported Formats** | CSV, TXT, plain text |
| **Server** | Flask Development Server |
| **Port** | 5000 (default) |
| **Architecture** | Client-Server (Monolithic) |
| **Deployment** | Local (can be deployed to cloud platforms) |

### Project Structure
```
Datasorter/
├── main.py              # Flask application and routes
├── templates/
│   └── index.html       # Frontend interface
├── .env                 # Environment variables (API keys)
├── .gitignore          # Git ignore rules
├── test.txt            # Sample data for testing
├── README.md           # Project documentation
└── venv/               # Virtual environment
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! This project is primarily a learning exercise, but improvements and suggestions are always appreciated.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational purposes. Feel free to use, modify, and distribute as needed.

---

## 👤 Author

**Kyle Yuen**
- GitHub: [@kyleyuen](https://github.com/kyleyuen)

---

## 🙏 Acknowledgments

- **Cohere AI**: For providing the powerful language model API
- **Flask Community**: For excellent documentation and resources
- **Open Source Contributors**: For inspiration and learning materials
- **Stack Overflow Community**: For troubleshooting support during development

---

## ⭐ Show Your Support

If you found this project helpful or learned something from it, please consider giving it a star! ⭐

It helps others discover the project and motivates continued development.

---

**Built with ❤️ as a learning project to explore Flask, AI integration, and full-stack development**
