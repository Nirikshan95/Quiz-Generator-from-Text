# Quiz-Generator-from-Text

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red.svg)](https://streamlit.io/)
[![AI Powered](https://img.shields.io/badge/AI-Powered-brightgreen.svg)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/yourusername/Quiz-Generator-from-Text)

## 🎯 Overview

Quiz-Generator-from-Text is an intelligent application that transforms any text content into comprehensive quiz questions automatically. Powered by advanced language models, this tool can generate multiple-choice questions from educational content, articles, or any textual material.

Perfect for educators, students, content creators, and anyone looking to create engaging assessments from existing text materials.

## 🌟 Key Features

- **Smart Question Generation**: Automatically creates diverse question types from input text

- **Intelligent Parsing**: Advanced text analysis to identify key concepts and facts

- **Web Interface**: User-friendly Streamlit frontend (coming soon!)

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- HuggingFace API tokens for language model services

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nirikshan95/Quiz-Generator-from-Text.git
   cd Quiz-Generator-from-Text
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with your Hugging Face API token:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   HF_TOKEN=your_token_here
   ```

## 🚀 Usage

### Command Line Interface

Generate quizzes directly from the command line:

```bash
python quiz_generation/quiz_gen.py
```

### Web Interface (Coming Soon!)

We're working on a beautiful Streamlit web interface! Contributors are welcome to help complete the frontend integration.

```bash
# Once completed, you'll be able to run:
streamlit run app.py
```

## 📊 Example Output

**Input Text:**
```
The photosynthesis process allows plants to convert sunlight, carbon dioxide, and water into glucose and oxygen. This process occurs primarily in the chloroplasts of plant cells, specifically in the chlorophyll molecules. The equation for photosynthesis is: 6CO2 + 6H2O + light energy → C6H12O6 + 6O2.
```


## 🏗️ Project Architecture

```
Quiz-Generator-from-Text/
├── configs/
│   └── settings.py              # Configuration management
├── models/
│   └── load_chat_model.py       # Model loading and initialization
├── output_parser/
│   └── quiz_parser.py           # Question parsing and formatting
├── prompts/
│   └── quiz_prompt.txt          # Prompt templates for question generation
├── quiz_generation/
│   └── quiz_gen.py              # Core quiz generation logic
├── venv/                        # Virtual environment
├── .env                         # Environment variables
├── app.py                       # Streamlit frontend (in development)
├── LICENSE                      # MIT License
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## 🛠️ Core Components

### Quiz Generator (`quiz_generation/quiz_gen.py`)
The heart of the application that processes input text and generates intelligent questions using advanced NLP techniques.

### Output Parser (`output_parser/quiz_parser.py`)
Formats and structures the generated questions into clean, usable formats with proper schema.

### Model Interface (`models/load_chat_model.py`)
Handles communication with language models and manages model initialization and configuration.

### Prompt Engineering (`prompts/quiz_prompt.txt`)
Contains carefully crafted prompt that guide the AI to generate high-quality, educational questions.

## 📋 Dependencies

Core libraries used in this project:

- **langchain**: For LLM integration and chain operations
- **streamlit**: Web interface framework (frontend)
- **pydantic**: Data validation and parsing

See `requirements.txt` for the complete dependency list.

## 🤝 Contributing

We welcome contributions! Especially for:

- **Frontend Development**: Help complete the Streamlit web interface
- **Question Types**: Add support for more question formats
- **Model Integration**: Support for additional language models
- **Export Features**: Multiple output formats (PDF, Word, etc.)
- **UI/UX Improvements**: Make the interface more intuitive

### How to Contribute

1. **Fork the repository**
   ```bash
   git fork https://github.com/yourusername/Quiz-Generator-from-Text.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-new-feature
   ```

3. **Make your changes and commit**
   ```bash
   git commit -m "Add amazing new feature"
   ```

4. **Push to your fork and submit a pull request**
   ```bash
   git push origin feature/amazing-new-feature
   ```

### Current Priority Areas

- 🎨 **Frontend Integration**: Complete the Streamlit app integration
- 📊 **Question Analytics**: Add difficulty scoring and question quality metrics
- 🔄 **Batch Processing**: Support for multiple document processing
- 📤 **Export Functionality**: PDF, Word, and other format exports

## 🐛 Known Issues & Roadmap

### Current Limitations
- Streamlit frontend integration is incomplete
- Limited to text input (no file upload yet)
- Basic question formatting

### Upcoming Features
- [ ] Complete Streamlit web interface
- [ ] File upload support (PDF, DOCX, TXT)
- [ ] Question difficulty adjustment
- [ ] Batch quiz generation
- [ ] Export to multiple formats
- [ ] Question bank management
- [ ] User authentication and quiz history

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Hugging Face community for providing excellent language models
- Streamlit team for the amazing web app framework
- All contributors who help make this project better

## 📞 Support & Contact

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and community support
- **Email**: [nirikshan987654321@gmail.com] for direct contact

---

⭐ **Star this repository if you find it helpful!** ⭐

*Made with ❤️ for educators and learners everywhere*