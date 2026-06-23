from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import base64
import tempfile
import os
from pathlib import Path

try:
    import markitdown
except ImportError:
    print("MarkItDown not installed. Install with: pip install markitdown")
    exit(1)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/api/convert', methods=['POST'])
def convert():
    try:
        data = request.json
        filename = data.get('filename', 'document')
        content_base64 = data.get('content', '')
        
        # Decode base64 content
        file_content = base64.b64decode(content_base64)
        
        # Create temporary file with original extension
        file_ext = Path(filename).suffix or '.bin'
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(file_content)
            tmp_path = tmp.name
        
        try:
            # Convert using MarkItDown
            md = markitdown.MarkItDown()
            result = md.convert(tmp_path)
            markdown_content = result.text_content
            
            return jsonify({
                'success': True,
                'markdown': markdown_content,
                'filename': filename
            })
        finally:
            # Clean up temporary file
            os.unlink(tmp_path)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'MarkItDown Converter'})

if __name__ == '__main__':
    print("MarkItDown Converter Server")
    print("Starting server on http://localhost:5000")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
