# Password Strength Meter

A Streamlit web application that analyzes and rates the strength of passwords based on various criteria.

## Features

- Real-time password strength analysis
- Detailed feedback on password components
- Visual strength indicator
- Tips for creating strong passwords
- User-friendly interface

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Enter a password in the input field to see its strength analysis

## Password Strength Criteria

The application checks for:
- Password length (minimum 8 characters, recommended 12+)
- Presence of uppercase and lowercase letters
- Presence of numbers
- Presence of special characters
- Common patterns and sequences
- Overall complexity

## Deployment

This application can be deployed on Streamlit Cloud or any other platform that supports Streamlit applications.

## License

MIT License 