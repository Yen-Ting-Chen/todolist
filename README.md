# To-Do List (Django)

[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一個使用 **Django** 開發的簡單待辦清單應用，提供使用者新增、編輯、刪除與標記完成任務的功能，並可記錄完成狀態與到期時間。

---

## 功能特色
- 使用者可 **新增、編輯、刪除** 待辦事項  
<!-- - 可將待辦項目標記為 **完成/未完成**  
- 支援 **到期日** 與排序功能   -->
- 使用 **Django ORM** 操作資料庫  
- 使用 **Bootstrap 5** 美化介面  
<!-- - (選配) **使用者帳號系統**：支援註冊、登入、登出，每位使用者擁有自己的待辦列表 -->
---
## 環境需求
- Python 3.8+  
- Django 4.0.4 或更新版本  
- (選配) MySQL / SQLite 資料庫  
- pip 與虛擬環境 (venv)

---

## 安裝與設定

### 1. Clone 專案
```bash
git clone https://github.com/your-username/to_do_list.git
cd to_do_list
```

### 2. 建立虛擬環境並啟用
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. 安裝依賴套件
```bash
pip install -r requirements.txt
```
若沒有 `requirements.txt`，可手動安裝：
```bash
pip install django
```

### 4. 資料庫設定
預設使用 **SQLite**，若需使用 MySQL，請在 `settings.py` 中修改：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'to_do_list',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
並安裝驅動：
```bash
pip install mysqlclient
```

### 5. 建立資料表
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 建立管理員帳號 (選用)
```bash
python manage.py createsuperuser
```

### 7. 啟動開發伺服器
```bash
python manage.py runserver
```
打開瀏覽器訪問：
```
http://127.0.0.1:8000/show_list/first
```
---
## 使用方式
1. 新增待辦事項，設定標題與到期日  
2. 可編輯或刪除已存在的事項  
<!-- 3. 點擊勾選框標記完成狀態   -->
<!-- 5. (選用) 進入 `/admin` 後台管理資料 -->

---

## 專案結構
```
to_do_list/
│
├── manage.py
├── requirements.txt
├── to_do_list/       # 專案設定 (settings, urls, wsgi)
│
└── show_list/            # 主要應用 (models, views, templates)
    ├── migrations/
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── forms.py
│
└── templates
    │   └── show_list/
    │       └── index.html
```

---

## 技術棧
- **後端**：Django 4.0.4
- **前端**：Bootstrap 5
- **資料庫**：SQLite / MySQL
- **部署**：可部署至 AWS EC2 / Docker

---
<!-- ## 未來規劃
- 加入 API (Django REST Framework)  
- 支援行動裝置的 PWA  
- 提供到期提醒通知   -->
---

## 授權
歡迎自由修改與使用。
