from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_code():
    try:
        data = request.json
        description = data.get('description', '')
        language = data.get('language', 'python')
        
        if not description:
            return jsonify({'error': 'Description is required'}), 400
        
        prompt = f"""Generate clean, well-documented {language} code based on this description:
        
{description}

Requirements:
- Include docstrings/comments
- Follow best practices
- Handle errors appropriately
- Make the code production-ready
- Include type hints if applicable

Generate only the code, no explanations."""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert code generator. Generate clean, efficient, and well-documented code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        generated_code = response['choices'][0]['message']['content'].strip()
        
        return jsonify({
            'code': generated_code,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/explain', methods=['POST'])
def explain_code():
    try:
        data = request.json
        code = data.get('code', '')
        
        if not code:
            return jsonify({'error': 'Code is required'}), 400
        
        prompt = f"""Explain what this code does in a clear, concise way:

{code}

Provide:
1. Overall purpose
2. Key functions/classes
3. How it works
4. Potential improvements"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert code explainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        explanation = response['choices'][0]['message']['content'].strip()
        
        return jsonify({
            'explanation': explanation,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)