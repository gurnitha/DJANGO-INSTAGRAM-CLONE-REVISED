# DJANGO-INSTAGRAM-CLONE-REVISED
REVISI Belajar membuat aplikasi INSTAGRAM berdasarkan tutorial Desphixs di Youtube


## 1. SETUP 

        :: Aktivitas


#### 1.1 SETUP - Membuat local environment

        :: Aktivitas

        1. Membuat virtual environment (venv3942)

        ~ python --version
        ~ pip --version
        ~ virtualenv --version
        ~ python -m venv venv3942

        modified:   README.md


#### 1.2 SETUP - Menginstal Django versi 4.2

        :: Aktivitas

        1. Mengaktifkan venv3942
        ~ venv3942\Scripts\activate

        2. Menginstal Django versi 4.2
        ~ pip install django==4.2.*

        modified:   README.md


## 2. MEMBUAT APLIKASI


#### 2.1 MEMBUAT APLIKASI - Membuat Proyek Django 'Config'

        :: Aktivitas

        1. Memastikan django sudah terinstal
        ~ pip list

        2. Membuat proyek django
        ~ django-admin startproject Config .

        3. Memeriksa hasil
        ~ tree Config /f

        :: File baru / modifikasi

        new file:   Config/__init__.py
        new file:   Config/asgi.py
        new file:   Config/settings.py
        new file:   Config/urls.py
        new file:   Config/wsgi.py
        modified:   README.md
        new file:   manage.py


#### 2.2 MEMBUAT APLIKASI - Membuat App Django 'App/Post'

        :: Aktivitas

        1. Membuat direktori
        ~ mkdir App\Post

        2. Membuat App Django
        ~ django-admin startapp Post App\Post

        :: File baru / modifikasi

        new file:   App/Post/__init__.py
        new file:   App/Post/admin.py
        new file:   App/Post/apps.py
        new file:   App/Post/migrations/__init__.py
        new file:   App/Post/models.py
        new file:   App/Post/tests.py
        new file:   App/Post/views.py
        modified:   README.md


#### 2.3 MEMBUAT APLIKASI - Register app Post pada Config/settings.py

        :: Aktivitas

        1. Modifikasi name pada apps.py
        2. Register app Post pada Config/settings.py

        :: File baru / modifikasi

        modified:   App/Post/apps.py
        modified:   Config/settings.py
        modified:   README.md


#### 2.4 MEMBUAT APLIKASI - Menjalankan server lokal

        :: Aktivitas

        1. Tesing dengan menjalankan server lokal
        ~ python manage.py runserver

        2. Buka browser
        http://127.0.0.1:8000/

        :: File baru / modifikasi

        modified:   README.md

        NOTE:

        Sukses menjalankan server dan display hasil.


## 3. HOMEPAGE


#### 3.1 HOMEPAGE - Membuat 'Hello World!' dari HttpResponse

        :: Aktivitas

        1. Mengimport HttpResponse
        from django.http import HttpResponse
        2. Membuat index views dgn HttpResponse 'Hello World'
        3. Membuat path untuk laman home
        4. Register home path pada Config/urls.py

        :: File baru / modifikasi

        new file:   App/Post/urls.py
        modified:   App/Post/views.py
        modified:   Config/urls.py
        modified:   README.md

        NOTE:

        Sukses display 'Hello World!'
        :)


#### 3.2 HOMEPAGE - Membuat laman Home menggunakan templates, views, dan urls

        :: Aktivitas

        1. Mengimport os pada Config/settings.py 
        2. Mengaktifkan django templates pada Config/settings.py
        3. Membuat laman home 
        4. Memodifikasi index views

        :: File baru / modifikasi
        
        new file:   App/Post/templates/Post/index.html
        modified:   App/Post/views.py
        modified:   Config/settings.py
        modified:   README.md
        :)


#### 3.3 HOMEPAGE - Menambahkan html template pada laman home

        :: Aktivitas

        1. Menambahkan html template pada laman home

        :: File baru / modifikasi

        modified:   App/Post/templates/Post/index.html
        modified:   README.md

        NOTE:

        Home page belum berisi css, js dan images
        sehingga laman home terlihat kurang menarik.


#### 3.4 HOMEPAGE - Menambahkan static files

        :: Aktivitas

        1. Membuat folder static
        2. Mengisi assets pada static folder
        3. Membuat path pada settings.py untuk statid files
        4. Loading static files
        5. Testing: jalankan server dan refresh browser

        :: File baru / modifikasi

        modified:   App/Post/templates/Post/index.html
        modified:   Config/settings.py
        modified:   README.md
        new file:   static/ads-manage.JPG
        new file:   static/assets1/default-user.png
        ...
        new file:   static/default.jpg
        new file:   static/house.jpg
        new file:   static/logo-ombak.PNG

        NOTE:

        Sukses :)


#### 3.5 HOMEPAGE - Membuat base template

        :: Aktivitas

        1. Membuat file baru dengan nama base.html
        new file:   App/Post/templates/base.html
        2. Memindahkan html template pada laman home ke base.html
        3. Extends base.html pada laman home (index.html)
        modified:   App/Post/templates/Post/index.html
        4. Testing: jalankan server dan refresh browser

        :: File baru / modifikasi

        modified:   App/Post/templates/Post/index.html
        new file:   App/Post/templates/base.html
        modified:   README.md

        NOTE:

        Sukses :)