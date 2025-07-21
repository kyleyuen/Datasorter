from flask import Flask, render_template, request
import cohere

app = Flask(__name__)

co = cohere.Client("YOUR_API_KEY")

data_sorter_personality = """You are a highly skilled and efficient Data Sorting Assistant. Your expertise lies in:

1. ANALYZING raw data from various sources (Google Sheets, CSV files, text files, spreadsheets)
2. IDENTIFYING patterns, inconsistencies, and data quality issues
3. ORGANIZING and STRUCTURING data into logical, usable formats
4. CLEANING data by removing duplicates, fixing formatting issues, and standardizing entries
5. CATEGORIZING and SORTING data based on relevant criteria
6. SUGGESTING optimal data structures and formats for specific use cases
7. PROVIDING clear explanations of your sorting logic and recommendations

You are methodical, detail-oriented, and always aim to transform messy data into clean, organized, and actionable information. You ask clarifying questions when data requirements are unclear and provide step-by-step guidance for data processing tasks."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort_file', methods=['POST'])
def sort_file():
    uploaded_file = request.files.get('file')
    sort_instructions = request.form.get('sort_instructions', '').strip()

    if not uploaded_file:
        return "No file uploaded", 400

    file_content = uploaded_file.read().decode('utf-8')

    prompt = f"{data_sorter_personality}\n\n{file_content}\n\nInstructions: {sort_instructions if sort_instructions else 'No extra instructions.'}\n\nHow should I organize and clean this data to make it more usable?"

    response = co.chat(
        message=prompt,
        model="command-r-plus",
        temperature=0.7,
    )

    return render_template('index.html', response=response.text)

@app.route('/sort_text', methods=['POST'])
def sort_text():
    data = request.form.get('data', '').strip()
    sort_instructions = request.form.get('sort_instructions', '').strip()

    if not data:
        return "No data provided", 400

    prompt = f"{data_sorter_personality}\n\n{data}\n\nInstructions: {sort_instructions if sort_instructions else 'No extra instructions.'}\n\nHow should I organize and clean this data to make it more usable?"

    response = co.chat(
        message=prompt,
        model="command-r-plus",
        temperature=0.7,
    )

    return render_template('index.html', text_response=response.text)

if __name__ == '__main__':
    app.run(debug=True)
