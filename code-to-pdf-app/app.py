from flask import Flask, render_template, request, send_file
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max limit

ALLOWED_EXTENSIONS = {'txt', 'py', 'js', 'ts', 'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'go', 'rs', 'rb', 'php', 'sh', 'bash', 'html', 'css', 'json', 'xml', 'md', 'sql'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file_content(filepath):
    """Read file content with various encodings"""
    encodings = ['utf-8', 'latin-1', 'cp1251', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
    # If all encodings fail, read as binary and decode with errors='ignore'
    with open(filepath, 'rb') as f:
        return f.read().decode('utf-8', errors='ignore')

def create_pdf(content, filename):
    """Create PDF from text content"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Create custom style for code
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=10,
        leading=12,
        alignment=TA_LEFT,
        wordWrap='OFF'
    )
    
    story = []
    
    # Split content into lines and add to PDF
    lines = content.split('\n')
    for line in lines:
        # Escape special characters for ReportLab
        escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        if escaped_line.strip():
            story.append(Paragraph(escaped_line, code_style))
        else:
            story.append(Spacer(1, 12))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file', 400
    
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Read file content
            content = read_file_content(filepath)
            
            # Create PDF
            pdf_buffer = create_pdf(content, filename)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            # Send PDF
            pdf_filename = os.path.splitext(filename)[0] + '.pdf'
            return send_file(
                pdf_buffer,
                mimetype='application/pdf',
                as_attachment=True,
                download_name=pdf_filename
            )
        except Exception as e:
            # Clean up on error
            if os.path.exists(filepath):
                os.remove(filepath)
            return f'Error processing file: {str(e)}', 500
    
    return 'File type not allowed', 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
