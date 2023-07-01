import os

def allowed_file(filename, allowed_extensions):
    """Проверяет, соответствует ли расширение файла разрешенным расширениям."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def create_user_directory(upload_folder, email):
    """Создает директорию пользователя с указанным email."""
    user_directory = os.path.join(upload_folder, email)
    if not os.path.exists(user_directory):
        os.makedirs(user_directory)
    return user_directory

def save_file(file, email, upload_folder):
    """Сохраняет загруженный файл в директорию пользователя и возвращает путь к сохраненному файлу."""
    filename = file.filename
    user_directory = create_user_directory(upload_folder, email)
    file_path = os.path.join(user_directory, filename)
    file.save(file_path)
    return file_path
