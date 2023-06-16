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


#### 3.6 HOMEPAGE - Template inheritance

        :: Aktivitas

        1. Memecah laman home template menjadi beberap bagian
        2. Menggunakan include untuk menyertakan files yang dipecah
        3. Testing: jalankan server dan refresh browser

        :: File baru / modifikasi

        new file:   App/Post/templates/Post/components/content-posts.html
        new file:   App/Post/templates/Post/components/content-stories.html
        new file:   App/Post/templates/Post/components/content.html
        new file:   App/Post/templates/Post/components/side-menu.html
        modified:   App/Post/templates/Post/index.html
        modified:   App/Post/templates/base.html
        new file:   App/Post/templates/header.html
        new file:   App/Post/templates/navbar.html
        modified:   README.md

        NOTE:

        Sukses :)


## 4. DATABASE


#### 4.1 DATABASE - Membuat MySQL Database

        :: Aktivitas

        1. Mengaktifkan MySQL Server

        ~ mysql -u root -p
        Enter password: **** (root)
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        ...
        mysql>

        2. Membuat database

        mysql> CREATE DATABASE django_instagram_clone_revised;

        3. Memeriksa hasil

        mysql> SHOW DATABASES;
        +-----------------------------------------------------+
        | Database                                            |
        +-----------------------------------------------------+
        | information_schema                                  |
        | beginning_sql_queries                               |
        | brad_schiff_petfoodsreference                       |
        | ci_blog_and_magazine43                              |
        ...
        | django_instagram_clone_revised                      | <<----
        | django_job_portal                                   |
        ...
        | wp_ecommerce_porto621_58                            |
        +-----------------------------------------------------+
        134 rows in set (0.22 sec)

        :: File baru / modifikasi

        modified:   README.md

        NOTE:

        Suskses membuat database :)


#### 4.2 DATABASE - Menginstal mysqlclient

        :: Aktivitas

        1. Menginstal mysqlclient

        ~ pip install mysqlclient
        Collecting mysqlclient
          Using cached mysqlclient-2.1.1-cp39-cp39-win_amd64.whl (178 kB)
        Installing collected packages: mysqlclient
        Successfully installed mysqlclient-2.1.1
        
        2. Memeriksa hasilnya

        ~ pip list
        Package           Version
        ----------------- -------
        asgiref           3.7.2
        Django            4.2.2
        mysqlclient       2.1.1 << ---
        pip               23.1.2
        setuptools        56.0.0
        sqlparse          0.4.4
        typing_extensions 4.6.3
        tzdata            2023.3

        :: File baru / modifikasi

        modified:   README.md

        NOTE:

        Suskses menginstal mysqlclient :)


#### 4.3 DATABASE - Menghubungkan database dengan proyek

        :: Aktivitas

        1. Menghubungkan database dengan proyek

        # MYSQL DB
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_instagram_clone_revised',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        2. Testing: jalankan server

        ~ python manage.py runserver

        NotSupportedError(
        django.db.utils.NotSupportedError: MySQL 8 or later is required (found 5.7.24).

        3. Meng-upgrade MySQL dari versi 5.7 ke versi 8

        3.1 Install MySQL versi 8 di Laragon

        3.2 Backup database yg ada di MySQL versi 5.7

        C:\Users\hp>mysqldump -u root -p --all-databases > E:\workspace\laragon\tmp\alldb.sql
        Enter password: ****

        NOTE: berhasil

        3.3 Aktifkan MySQL versi 8

        Start server > pilih MySQL versi 8

        3.4 Membuat db pada MySQL versi 8
        dbname: django_instagram_clone_revised

        3.5 Testing: jalankan server

        (venv3942) hp@ING:DJANGO-IG-CLONE ~ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        ...
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        :: File baru / modifikasi

        modified:   Config/settings.py
        modified:   README.md
        
        NOTE:

        Suskses:

        1. Membackup db.
        2. Meng-upgrade MySQL.
        3. Membuat db baru.
        4. Menghubungkan db dengan proyek.