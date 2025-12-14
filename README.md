# الفا تريد (Alfa Trade)

مشروع ويب لإدارة التوريدات، المخزون والحسابات — واجهة احترافية ومتجاوبة.

مواصفات مبدئية:
- Backend: Django + Django REST Framework
- Database: PostgreSQL (configurable عبر متغيرات البيئة) أو SQLite للتطوير المحلي
- Frontend: Bootstrap 5 (قالب بسيط متجاوب)

تشغيل محلي (بدون Docker):

1. إنشاء بيئة افتراضية وتثبيت المتطلبات:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. تطبيق المهاجرات وإنشاء مستخدم مشرف:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

تشغيل مع Docker (يوجد ملف `docker-compose.yml` لقاعدة بيانات PostgreSQL):

```bash
docker-compose up --build
```

المسارات الأساسية:
- لوحة الإدارة: `/admin`
- واجهة المستخدم: `/`
- API: `/api/`

المراحل التالية المقترحة:
- إضافة صلاحيات وأدوار مستخدمين
  - إنشاء مجموعات افتراضية (Admin, Manager, Staff) عبر أمر إدارة
- صفحة إدارة مخزون مفصلة وعمليات جرد
- تقارير مالية (تصدير PDF/CSV)
- اختبارات ووضع CI

