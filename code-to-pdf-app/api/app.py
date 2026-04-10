from flask import Flask, request, send_file, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from io import BytesIO
import os

app = Flask(__name__)

# Поддерживаемые расширения файлов
SUPPORTED_EXTENSIONS = {
    'py', 'js', 'ts', 'jsx', 'tsx', 'html', 'css', 'json', 'xml', 'yaml', 'yml',
    'md', 'txt', 'sh', 'bash', 'zsh', 'rb', 'php', 'go', 'rs', 'swift', 'kt',
    'java', 'c', 'cpp', 'h', 'hpp', 'cs', 'sql', 'r', 'm', 'lua', 'pl', 'pm'
}

@app.route('/api/convert', methods=['POST'])
def convert_to_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'Файл не найден'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Имя файла пустое'}), 400
    
    # Проверка расширения
    ext = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else ''
    if ext not in SUPPORTED_EXTENSIONS:
        return jsonify({'error': f'Формат .{ext} не поддерживается'}), 400
    
    try:
        # Чтение содержимого файла
        content = file.read().decode('utf-8', errors='replace')
        
        # Создание PDF в памяти
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        
        # Настройки шрифта
        c.setFont("Courier", 10)
        
        # Параметры для текста
        left_margin = 0.5 * inch
        top_margin = height - 0.5 * inch
        line_height = 12
        max_width = width - left_margin - 0.5 * inch
        
        y_position = top_margin
        
        # Разбивка на строки и перенос длинных строк
        lines = content.split('\n')
        
        for line in lines:
            # Если строка слишком длинная, разбиваем её
            while len(line) > 0:
                # Проверяем длину строки в пунктах (примерно)
                test_string = line
                while len(test_string) > 0:
                    string_width = c.stringWidth(test_string, "Courier", 10)
                    if string_width <= max_width:
                        break
                    test_string = test_string[:-1]
                
                if len(test_string) == 0:
                    test_string = line[:80]  # fallback
                
                # Проверка на переполнение страницы
                if y_position < 0.5 * inch:
                    c.showPage()
                    c.setFont("Courier", 10)
                    y_position = top_margin
                
                c.drawString(left_margin, y_position, test_string)
                y_position -= line_height
                
                line = line[len(test_string):]
        
        c.save()
        buffer.seek(0)
        
        # Формирование имени выходного файла
        output_filename = os.path.splitext(file.filename)[0] + '.pdf'
        
        return send_file(
            buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=output_filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/supported-formats', methods=['GET'])
def get_supported_formats():
    return jsonify({'formats': sorted(list(SUPPORTED_EXTENSIONS))})

if __name__ == '__main__':
    app.run(debug=True)
