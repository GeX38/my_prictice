from flask import Flask, request, render_template
from upload_service import allowed_file, save_file
from database_service import save_file_info, create_files_table
from map_service import generate_plot

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'
app.config['DATABASE'] = 'data.db'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','h5'}
file_path = ''
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global file_path
    if request.method == 'POST':
        email = request.form.get('email')
        file = request.files['file']

        if email and file and allowed_file(file.filename, app.config['ALLOWED_EXTENSIONS']):
            file_path = save_file(file, email, app.config['UPLOAD_FOLDER'])
            save_file_info(email, file_path, app.config['DATABASE'])
            return render_template('upload.html', message='File uploaded successfully.')
        else:
            return render_template('upload.html', message='Invalid email or file format.')

    return render_template('upload.html')
@app.route('/plot', methods=['POST'])  # Новый маршрут для построения графика
def plot_graph():
    if request.method == 'POST':
        generate_plot(file_path)  # Вызов нового микросервиса
        return render_template('upload.html', message='Plot generated.')  # Возврат сообщения об успешном построении графика

    return render_template('upload.html')

if __name__ == '__main__':
    create_files_table(app.config['DATABASE'])
    app.run()
