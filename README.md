# my_prictice
File Upload and Plotting
Это пример приложения Flask для загрузки файлов и построения графиков.

Описание
Данное приложение разработано с использованием фреймворка Flask и позволяет пользователям загружать файлы, сохранять информацию о файлах в базе данных SQLite и строить графики на основе загруженных данных.

Приложение состоит из следующих модулей:

main_app.py: основной сервер Flask, отвечающий за обработку запросов загрузки файлов и отображение страницы загрузки.
upload_service.py: модуль, содержащий функции для обработки загрузки файлов, проверки расширений файлов и сохранения файлов на сервере.
database_service.py: модуль, содержащий функции для работы с базой данных SQLite, включая сохранение информации о файлах и создание таблицы файлов.
plot_service.py: модуль, отвечающий за построение графиков на основе загруженных данных.
Требования
Перед запуском приложения, убедитесь, что у вас установлен Conda и выполните следующие шаги:

Создайте новое виртуальное окружение с помощью Conda:

conda create -n flask-app python=3.9
Активируйте виртуальное окружение:

conda activate flask-app
Установите необходимые зависимости:

conda install -c conda-forge --file requirements.txt
Установка и запуск
Склонируйте репозиторий с помощью команды:

git clone https://github.com/GeX38/my_prictice
Перейдите в каталог проекта:

cd flask-file-upload-plotting
Установите зависимости:

conda install -c conda-forge --file requirements.txt
Запустите приложение:

python main_app.py
Откройте браузер и перейдите по адресу http://localhost:5000 для доступа к приложению.

Использование
На главной странице вы можете загрузить файл, указав свой адрес электронной почты и выбрав файл для загрузки.

После загрузки файла и успешного сохранения его на сервере, вы увидите сообщение об успешной загрузке или сообщение об ошибке, если что-то пошло не так.

Вы можете нажать кнопку "Построить график", чтобы построить график на основе загруженных данных. График будет отображен на экране.

Чтобы загрузить новый файл или построить другой график, вернитесь на главную страницу.

Лицензия
Этот проект распространяется под лицензией MIT.
