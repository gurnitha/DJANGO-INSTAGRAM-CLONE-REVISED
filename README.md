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