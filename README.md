# SE_lab_6

## گزارش
---
پلیکیشن Flask CRUD (ایجاد، خواندن، به‌روزرسانی، حذف) ارائه شده یک برنامه وب است که با استفاده از Flask و کتابخانه SQLAlchemy ساخته شده است. این اپلیکیشن به ما امکان انجام عملیات CRUD روی یک منبع را می‌دهد.

در ادامه به شرح مختصری از اجزای کلیدی این برنامه می‌پردازیم:

فایل `app.py` حاوی کد اصلی برنامه Flask است. <br/>
تابع `create_app()` برنامه Flask را مقداردهی اولیه و پیکربندی می‌کند. <br/>
کلاس `Resource` یک مدل است که یک منبع را در این برنامه نمایش می‌دهد. این کلاس شامل فیلد `id` و فیلد `name` است. <br/>
این برنامه به یک پایگاه داده متصل می‌شود که با استفاده از متغیر محیطی `DATABASE_URL` تعیین می‌شود. <br/>
برنامه چندین مسیر را تعریف می‌کند تا عملیات‌های مختلف را انجام دهد: <br/>
- **GET** /resources تمام منابع را از پایگاه داده بازیابی کرده و آن‌ها را به صورت JSON برمی‌گرداند. <br/>
- **POST** /resources با استخراج نام از بارگیری JSON در درخواست، یک منبع جدید ایجاد می‌کند. <br/>
- **PUT** /resources/<int:resource_id> یک منبع موجود با شناسه مشخص را به‌روزرسانی می‌کند. <br/>
- **DELETE** /resources/<int:resource_id> منبع مشخص با شناسه داده شده را حذف می‌کند. <br/> <br/>

برنامه برای مواقعی که فیلدهای ضروری وجود ندارند یا منبع یافت نشد، بررسی خطا انجام می‌دهد و پیام خطای مناسب را به صورت JSON برمی‌گرداند. <br/>
برنامه را می‌توان با اجرای `python app.py` در ترمینال اجرا کرد. این برنامه روی `localhost (0.0.0.0)` و در حالت اشکال‌زدایی اجرا می‌شود. <br/>
این اپلیکیشن Flask CRUD یک رابط برنامه‌نویسی برای مدیریت منابع به صورت پایه‌ای فراهم می‌کند و امکان ایجاد، خواندن، به‌روزرسانی و حذف منابع را با استفاده از مسیرهای ارائه شده فراهم می‌کند. <br/>

### نمودار UML
![photo_2023-08-28_22-14-29](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/2650a53f-eb20-4698-89b0-06d527ba18af)

### بالا آمدن Docker Compose
در این بخش، نحوه‌ی اجرای مجموعه‌ی Docker Compose را مشاهده می‌کنید. این مجموعه شامل دو نمونه از برنامه‌ی وب، یک سرور Nginx، و یک پایگاه داده می‌باشد.
![photo_2023-08-28_22-02-33](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/b2476c65-2bf3-484c-bc82-3eb40a249d64)

### بررسی اجرا در Postman

این تصویر نمایانگر یک درخواست GET به برنامه‌ی (webapp1) است که روی پورت 8000 اجرا شده و بدون داده است.

![photo_2023-08-28_22-07-34](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/613e0902-10b6-4686-8f22-e28670ed29f1)

در این قسمت، یک درخواست POST به برنامه‌ی (webapp1) را مشاهده می‌کنید.


![photo_2023-08-28_22-07-52](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/08617431-dbcc-49e1-8719-5a9e265d4cb3)

این تصویر یک درخواست GET به برنامه‌ی دوم (webapp2) را نشان می‌دهد که روی پورت 8080 اجرا شده است. این برنامه به یک پایگاه داده متصل است و بنابراین داده‌ها را نیز بارگذاری می‌کند.

![photo_2023-08-28_22-08-05](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/7a83ecf1-0804-4282-baf7-b2592424b91d)

در این بخش، یک درخواست GET به پورت 80 را مشاهده می‌کنید، که Nginx روی آن اجرا شده و وظایف مرتبط با توزیع بار (Load Balancing) را انجام می‌دهد.

![photo_2023-08-28_22-10-05](https://github.com/bardia-mhd/SE_lab_6/assets/22092861/ac3e1deb-018d-4c16-8817-53339edd50dc)


## پرسش‌ها
---
1. در معماری میکروسرویس، از چندین نوع نمودار UML می‌توان استفاده کرد. نمودار Component برای نمایش ساختار و ارتباطات بین میکروسرویس‌ها و نمودار Deployment برای توضیح نحوه‌ی مستقر شدن آن‌ها در زیرساخت فیزیکی یا مجازی استفاده می‌شود. نمودار Sequence نیز برای توصیف جریان تراکنش‌ها و تعاملات بین میکروسرویس‌ها مفید است.
2. مفهوم Domain-Driven Design یک رویکرد مدل‌سازی است که به توسعه‌دهندگان این امکان را می‌دهد تا مدل‌های دامنه‌ای را به طور دقیق و با تمرکز بر منطق کسب و کار تعریف کنند. در معماری میکروسرویس، این مدل‌سازی به این معنا است که هر میکروسرویس یک یا چند دامنه یا زیردامنه (Subdomain) کسب و کار را پیاده‌سازی می‌کند، که در ایجاد سرویس‌های مستقل و قابل مدیریت کمک می‌کند.
3. Docker Compose یک ابزار orchestration است که ایجاد برنامه‌های توزیع‌شده چند‌کانتینری با Docker را بسیار آسان می‌کند. با استفاده از یک فایل، می‌توان برنامه‌ای چند‌کانتینری و خدمات همراه آن را تعریف کرد و با یک دستور واحد، کل برنامه را راه‌اندازی و اجرا کرد.
