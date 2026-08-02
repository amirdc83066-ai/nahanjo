<p align="center">
  <img src="./ui/resources/icons/nahanjo.png" width="132" alt="Nahanjo logo">
</p>

<h1 align="center">ناهنجو | Nahanjo</h1>

<p dir="rtl" align="center">
  <strong>سامانه دسکتاپ فارسی برای تحلیل، تشخیص و اولویت‌بندی ناهنجاری در داده‌های جدولی</strong>
</p>

<p dir="rtl" align="center">
  از فایل خام و داده‌های نامنظم تا ردیف‌هایی که باید زودتر و دقیق‌تر بررسی شوند
</p>

<p align="center">
  <img alt="Version 2.0.3" src="https://img.shields.io/badge/version-2.0.3-2563EB">
  <img alt="Python 3.11" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img alt="PyQt6" src="https://img.shields.io/badge/PyQt6-6.11-41CD52?logo=qt&logoColor=white">
  <img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-0078D4?logo=windows&logoColor=white">
  <img alt="Persian UI" src="https://img.shields.io/badge/UI-Persian-7C3AED">
</p>

<p align="center">
  <img alt="Data workflow" src="https://img.shields.io/badge/Data%20Workflow-0F766E">
  <img alt="Six Detectors" src="https://img.shields.io/badge/6%20Detectors-1D4ED8">
  <img alt="Autoencoder" src="https://img.shields.io/badge/Autoencoder-7C3AED">
  <img alt="Optional AI" src="https://img.shields.io/badge/AI-Optional-C2410C">
  <img alt="Persian PDF" src="https://img.shields.io/badge/Persian%20PDF-B91C1C">
</p>

<p dir="rtl" align="right">
  <strong>مرز استفاده:</strong>
  ناهنجو ابزار تحلیل و تصمیم‌یار است، نه سامانه صدور حکم خودکار. هر ردیف یا مقداری که برای بررسی نشان داده می‌شود باید در زمینه واقعی داده ارزیابی شود و به‌تنهایی اثبات خطا، تقلب، خرابی یا علت یک رویداد نیست.
</p>

---

<a id="quick-start"></a>
<h2 dir="rtl" align="right">شروع سریع</h2>

<h3 dir="rtl" align="right">نسخه آماده ویندوز</h3>

<ol dir="rtl" align="right">
  <li>فایل نسخه آماده یا Installer ناهنجو را از کنار Release دریافت کنید.</li>
  <li>اگر Installer دارید، آن را اجرا کنید؛ اگر پوشه آماده دارید، فایل <code>Nahanjo.exe</code> را باز کنید.</li>
  <li>فایل داده را وارد کنید و تحلیل را شروع کنید.</li>
</ol>

<h3 dir="rtl" align="right">اجرای سورس</h3>

<p dir="rtl" align="right">
  برای اجرای ساده سورس، Python 3.11 نسخه 64 بیتی را نصب کنید، یک PowerShell را در ریشه پروژه باز کنید و فقط این دو فرمان را اجرا کنید:
</p>

~~~powershell
py -3.11 -m pip install -r requirements.txt
py -3.11 main.py
~~~

<p dir="rtl" align="right">
  ساختن <code>venv</code> اجباری نیست. برای استفاده معمول، همین روش کافی است.
</p>

<details>
  <summary dir="rtl">روش اختیاری با محیط مجازی</summary>

~~~powershell
py -3.11 -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe main.py
~~~

</details>

<p dir="rtl" align="right">
  تحلیل اصلی، نمودارها و گزارش PDF بدون هوش مصنوعی اجرا می‌شوند. فقط تفسیر AI، بررسی Update و همگام‌سازی بخش AI به اتصال شبکه نیاز دارند.
</p>

<a id="at-a-glance"></a>
<h3 dir="rtl" align="right">در یک نگاه</h3>

<table dir="rtl">
  <tr>
    <td align="right"><strong>ورودی</strong><br>CSV، Excel، JSON، TXT و Parquet</td>
    <td align="right"><strong>تحلیل</strong><br>شش Detector کلاسیک و Autoencoder</td>
    <td align="right"><strong>خروجی</strong><br>نتیجه، نمودار، PDF و تفسیر اختیاری AI</td>
  </tr>
  <tr>
    <td align="right"><strong>رابط</strong><br>دسکتاپ فارسی با PyQt6</td>
    <td align="right"><strong>ردیابی</strong><br>اتصال نتیجه به ردیف فایل اصلی</td>
    <td align="right"><strong>پلتفرم رسمی</strong><br>Windows x64</td>
  </tr>
</table>

<blockquote>
  <strong>نکته انتشار:</strong>
  <span dir="rtl">تصاویر README از فایل‌های واقعی داخل پوشه <code>docs/assets/architecture_dossier</code> خوانده می‌شوند. این پوشه باید همراه خود README در Repository قرار بگیرد.</span>
</blockquote>

---

<a id="contents"></a>
<h2 dir="rtl" align="right">فهرست</h2>

<ul dir="rtl" align="right">
  <li><a href="#quick-start">شروع سریع</a></li>
  <li><a href="#about">معرفی ناهنجو</a></li>
  <li><a href="#problem">مسئله‌ای که ناهنجو حل می‌کند</a></li>
  <li><a href="#solution">راه‌حل و ارزش محصول</a></li>
  <li><a href="#use-cases">حوزه‌های استفاده</a></li>
  <li><a href="#english">English Overview</a></li>
  <li><a href="#screenshots">نمای برنامه</a></li>
  <li><a href="#features">قابلیت‌ها و روند استفاده</a></li>
  <li><a href="#analysis">موتور تشخیص و Detectorها</a></li>
  <li><a href="#autoencoder">تحلیل Autoencoder</a></li>
  <li><a href="#ai">هوش مصنوعی و حریم خصوصی</a></li>
  <li><a href="#architecture">معماری سطح‌بالا</a></li>
  <li><a href="#development">توسعه و تست</a></li>
  <li><a href="#status">وضعیت، محدودیت‌ها و مسیر توسعه</a></li>
  <li><a href="#security">امنیت و مجوز</a></li>
</ul>

---

<a id="about"></a>
<h2 dir="rtl" align="right">معرفی ناهنجو</h2>

<p dir="rtl" align="right">
  ناهنجو یک نرم‌افزار دسکتاپ فارسی برای بررسی ناهنجاری در داده‌های جدولی است. هدف آن ایجاد یک مسیر منظم میان «فایل خام» و «تصمیم انسانی» است. کاربر داده را وارد می‌کند، بخش مورد نظر را انتخاب می‌کند و برنامه با چند روش تحلیلی مستقل، رفتارهای غیرمعمول را پیدا و براساس شواهد موجود مرتب می‌کند.
</p>

<p dir="rtl" align="right">
  خروجی ناهنجو فقط چند عدد قرمز یا یک پیام کلی نیست. برنامه نشان می‌دهد کدام ردیف یا مقدار نیازمند بررسی است، چه Detectorهایی آن را متفاوت دیده‌اند، قدرت نسبی این تفاوت چقدر است، داده ورودی برای تحلیل چه وضعیتی داشته و نتیجه دقیقاً به کدام موقعیت فایل اصلی برمی‌گردد. همان نتیجه در صفحه نتایج، نمودارها، گزارش PDF و تفسیر اختیاری هوش مصنوعی استفاده می‌شود.
</p>

<p dir="rtl" align="right">
  ناهنجاری همیشه به معنی «بزرگ‌ترین عدد» یا «کم‌ترین عدد» نیست. یک جهش ناگهانی، افت غیرمنتظره، فاصله از رفتار محلی، قرارگرفتن بیرون از محدوده معمول، ناسازگاری با الگوی غالب یا خطای بازسازی می‌تواند یک مورد را برای بررسی مهم کند. به همین دلیل ناهنجو به یک فرمول واحد وابسته نیست و مسئله را از چند زاویه بررسی می‌کند.
</p>

<p dir="rtl" align="right">
  این محصول برای جایگزین‌کردن تحلیل‌گر، حسابرس، متخصص داده یا کارشناس حوزه ساخته نشده است. نقش آن کاهش فضای جست‌وجو است: به‌جای بررسی دستی هزاران ردیف، کاربر می‌تواند ابتدا روی بخش‌هایی تمرکز کند که شواهد بیشتری از رفتار غیرمعمول دارند.
</p>

<a id="problem"></a>
<h2 dir="rtl" align="right">مسئله‌ای که ناهنجو حل می‌کند</h2>

<p dir="rtl" align="right">
  تشخیص ناهنجاری در یک پروژه واقعی فقط اجرای یک الگوریتم روی یک ستون تمیز نیست. پیش از تحلیل، داده باید وارد شود، ساختار جدول فهمیده شود، مقدارهای عددی از متن و قالب‌های مختلف جدا شوند، ردیف‌های نامعتبر مشخص شوند و ارتباط نتیجه با فایل اصلی از بین نرود. پس از تحلیل نیز خروجی باید برای انسان قابل‌خواندن، قابل‌مقایسه و قابل‌گزارش باشد.
</p>

<p dir="rtl" align="right">
  وقتی این مراحل میان چند ابزار، فایل موقت، Notebook و عملیات دستی پخش می‌شوند، مشکلات مهمی به وجود می‌آید:
</p>

<ul dir="rtl" align="right">
  <li>ساختار فایل، Header یا نوع ستون درست تشخیص داده نمی‌شود؛</li>
  <li>صفر، مقدار تکراری، سلول خالی و متن عددی به‌اشتباه با هم مخلوط می‌شوند؛</li>
  <li>پس از پاک‌سازی یا حذف ردیف‌ها، مشخص نیست نتیجه به کدام ردیف فایل اصلی مربوط است؛</li>
  <li>یک روش تشخیص بعضی الگوها را می‌بیند و بعضی الگوها را از دست می‌دهد؛</li>
  <li>خروجی خام الگوریتم برای کاربر روشن نمی‌کند از کجا باید بررسی را شروع کند؛</li>
  <li>نمودار، گزارش و تفسیر متنی از نتیجه علمی جدا می‌شوند و روایت متفاوتی می‌سازند؛</li>
  <li>هوش مصنوعی بدون مرز مشخص ممکن است متنی فراتر از شواهد واقعی موتور تولید کند.</li>
</ul>

<p dir="rtl" align="right">
  ناهنجو این مسئله را به‌صورت یک زنجیره کامل حل می‌کند: ورود کنترل‌شده داده، آماده‌سازی و سنجش کیفیت، اجرای چند روش، ترکیب شواهد، حفظ موقعیت منبع، اولویت‌بندی، نمایش بصری و تولید خروجی قابل‌استفاده.
</p>

<a id="solution"></a>
<h2 dir="rtl" align="right">راه‌حل و ارزش محصول</h2>

<h3 dir="rtl" align="right">۱. تبدیل فایل خام به داده قابل تحلیل</h3>

<p dir="rtl" align="right">
  ناهنجو فایل‌های رایج جدولی را می‌خواند، ساختار آن‌ها را اعتبارسنجی می‌کند، در Excel ردیف مناسب Header را تشخیص می‌دهد و یک فضای کاری مستقل برای مشاهده و ویرایش داده می‌سازد. پیش‌نمایش رابط ممکن است برای سرعت محدود باشد، اما تحلیل روی داده کامل انتخاب‌شده انجام می‌شود.
</p>

<h3 dir="rtl" align="right">۲. حفظ کیفیت و معنای داده</h3>

<p dir="rtl" align="right">
  موتور آماده‌سازی میان مقدار خالی، متن غیرعددی، مقدار نامتناهی، ورودی مبهم و عدد معتبر تفاوت می‌گذارد. صفر به‌عنوان عدد معتبر حفظ می‌شود و مقدارهای تکراری نیز بخشی از رفتار واقعی داده باقی می‌مانند. نتیجه پاک‌سازی به شکل خاموش داده را تغییر نمی‌دهد؛ وضعیت ورودی و موارد ردشده قابل بررسی‌اند.
</p>

<h3 dir="rtl" align="right">۳. ردیابی نتیجه تا فایل اصلی</h3>

<p dir="rtl" align="right">
  هنگام انتخاب، ویرایش یا آماده‌سازی داده، موقعیت منبع نگهداری می‌شود. بنابراین نتیجه فقط نمی‌گوید «مقدار ۱۲۵ غیرعادی است»؛ می‌تواند آن را دوباره به ردیف مربوط در داده اصلی متصل کند. این موضوع برای بازبینی، گزارش، حسابرسی و اصلاح داده ضروری است.
</p>

<h3 dir="rtl" align="right">۴. بررسی یک مسئله از چند زاویه</h3>

<p dir="rtl" align="right">
  شش Detector کلاسیک با فرض‌های متفاوت اجرا می‌شوند: بعضی فاصله از مرکز را بررسی می‌کنند، بعضی در برابر مقدارهای دور مقاوم‌ترند، بعضی محدوده چارکی را می‌سنجند، بعضی به چگالی محلی توجه دارند و بعضی مرز رفتار غالب یا قابلیت جداسازی مشاهده را بررسی می‌کنند. اختلاف نتیجه Detectorها پنهان نمی‌شود؛ برنامه آن‌ها را کنار هم قرار می‌دهد تا کاربر شواهد را ببیند.
</p>

<h3 dir="rtl" align="right">۵. تبدیل خروجی علمی به اولویت بررسی</h3>

<p dir="rtl" align="right">
  ناهنجو هشدارهای روش‌ها را با تعداد ردیف‌های یکتای نیازمند بررسی قاطی نمی‌کند. نتیجه‌ها براساس موقعیت داده یکپارچه می‌شوند، میزان پشتیبانی روش‌ها و قدرت نسبی هر مورد محاسبه می‌شود و یک ترتیب پیشنهادی برای بازبینی ساخته می‌شود. این ترتیب احتمال قطعی یا ریسک مالی کالیبره‌شده نیست؛ ابزاری برای مدیریت بهتر زمان بررسی است.
</p>

<h3 dir="rtl" align="right">۶. یک نتیجه مشترک برای تمام خروجی‌ها</h3>

<p dir="rtl" align="right">
  رابط نتایج، نمودارها، گزارش PDF و قابلیت‌های هوش مصنوعی از یک نتیجه ساختاریافته مشترک استفاده می‌کنند. این طراحی باعث می‌شود نمودار یا متن گزارش، نتیجه‌ای متفاوت از موتور تحلیل نسازد و هر بخش فقط همان شواهد واقعی را با شکل مناسب خود نمایش دهد.
</p>

<h3 dir="rtl" align="right">۷. جداسازی تحلیل اصلی از Autoencoder و هوش مصنوعی</h3>

<p dir="rtl" align="right">
  تحلیل Autoencoder یک مسیر بازسازی مستقل است و خروجی آن با نتیجه شش Detector کلاسیک مخلوط نمی‌شود. هوش مصنوعی نیز بعد از پایان محاسبات برای تفسیر و گزارش وارد می‌شود و اجازه ندارد موارد علامت‌گذاری‌شده موتور را اضافه، حذف یا جابه‌جا کند.
</p>

<a id="use-cases"></a>
<h2 dir="rtl" align="right">حوزه‌های استفاده</h2>

<p dir="rtl" align="right">
  ناهنجو یک موتور عمومی برای تحلیل اکتشافی داده جدولی است و می‌تواند در هر حوزه‌ای که ردیف‌ها یا مقدارهای غیرمعمول نیازمند بازبینی‌اند استفاده شود.
</p>

<table dir="rtl">
  <tr>
    <th align="right">حوزه</th>
    <th align="right">نمونه داده</th>
    <th align="right">پرسش عملی</th>
  </tr>
  <tr>
    <td align="right">مالی و حسابداری</td>
    <td align="right">مبلغ، تعداد تراکنش، مانده، فاصله زمانی</td>
    <td align="right">کدام ردیف‌ها با الگوی غالب فاصله دارند و باید زودتر بررسی شوند؟</td>
  </tr>
  <tr>
    <td align="right">عملیات و پایش</td>
    <td align="right">زمان پاسخ، نرخ خطا، حجم کار، مصرف منابع</td>
    <td align="right">کدام تغییر ممکن است نشانه اختلال یا رفتار غیرعادی باشد؟</td>
  </tr>
  <tr>
    <td align="right">انرژی و زیرساخت</td>
    <td align="right">مصرف، بار، فشار، دما، جریان</td>
    <td align="right">کدام جهش، افت یا فاصله از روند معمول نیازمند بررسی است؟</td>
  </tr>
  <tr>
    <td align="right">صنعت و کنترل کیفیت</td>
    <td align="right">اندازه‌گیری فرایند، زمان چرخه، سنسور، خروجی تولید</td>
    <td align="right">کدام مشاهده با رفتار رایج خط تولید یا دستگاه سازگار نیست؟</td>
  </tr>
  <tr>
    <td align="right">کیفیت داده</td>
    <td align="right">مقدار خالی، متن نامعتبر، قالب ناسازگار، مقدار نامتناهی</td>
    <td align="right">کدام بخش ورودی برای تحلیل قابل اتکا نیست یا نیاز به اصلاح دارد؟</td>
  </tr>
  <tr>
    <td align="right">پژوهش و تحلیل اکتشافی</td>
    <td align="right">خروجی آزمایش، سری عددی، داده مشاهده‌ای</td>
    <td align="right">روش‌های مختلف روی کدام موارد توافق یا اختلاف دارند؟</td>
  </tr>
</table>

<p dir="rtl" align="right">
  این موارد نمونه استفاده‌اند، نه ادعای دقت تضمین‌شده یا استقرار تأییدشده در هر صنعت. ارزیابی معتبر هر حوزه به داده واقعی، معیار پذیرش و در صورت امکان داده مرجع نیاز دارد.
</p>

<a id="english"></a>
<div dir="ltr" align="left">
  <h2>English Overview</h2>
  <p>
    <strong>Nahanjo</strong> is a Persian-first Windows desktop application for exploratory anomaly analysis on tabular data. It turns raw files into a traceable review workflow: controlled ingestion, numeric preparation, input-quality assessment, six independent classical detection methods, evidence aggregation, source-row mapping, interactive charts, optional AI interpretation, Autoencoder/reconstruction analysis, and Persian PDF reporting.
  </p>
  <p>
    The product addresses a practical gap between running an algorithm and completing a real investigation. It preserves the relationship between an analytical result and the original row, keeps disagreements between methods visible, distinguishes input quality from model output, and ranks unusual observations without presenting them as confirmed errors or calibrated risk probabilities.
  </p>
  <ul>
    <li>Persian desktop interface built with PyQt6</li>
    <li>CSV, Excel, JSON, TXT, and Parquet input</li>
    <li>Z-Score, MAD, IQR, LOF, Isolation Forest, and One-Class SVM</li>
    <li>Source-row traceability and evidence-based result aggregation</li>
    <li>Independent Autoencoder/reconstruction workspace using PCA and Gaussian Random Projection by default</li>
    <li>Interactive charts, optional AI interpretation, and RTL PDF reports</li>
    <li>Windows packaged release and a simple source-run path</li>
  </ul>
</div>

---

<a id="screenshots"></a>
<h2 dir="rtl" align="right">نمای برنامه</h2>

<p dir="rtl" align="right">
  تصاویر زیر مستقیماً از فایل‌های واقعی رابط برنامه نمایش داده می‌شوند و هیچ لینک کلیک‌پذیری دور آن‌ها قرار نگرفته است.
</p>

| ورود فایل یا ساخت جدول | پیش‌نمایش، انتخاب و ویرایش داده |
| :---: | :---: |
| ![ورود داده در ناهنجو](./docs/assets/architecture_dossier/01-data-entry.png) | ![پیش‌نمایش داده در ناهنجو](./docs/assets/architecture_dossier/02-data-preview.png) |

| نمودارهای تعاملی | تحلیل اختیاری هوش مصنوعی |
| :---: | :---: |
| ![نمودارهای ناهنجو](./docs/assets/architecture_dossier/04-charts.png) | ![تحلیل هوش مصنوعی ناهنجو](./docs/assets/architecture_dossier/05-ai-analysis.png) |

| تحلیل Autoencoder | تنظیمات برنامه |
| :---: | :---: |
| ![تحلیل Autoencoder ناهنجو](./docs/assets/architecture_dossier/06-hidden-patterns.png) | ![تنظیمات ناهنجو](./docs/assets/architecture_dossier/07-settings.png) |

---

<a id="features"></a>
<h2 dir="rtl" align="right">قابلیت‌ها و روند استفاده</h2>

<table dir="rtl">
  <tr>
    <th align="right">بخش</th>
    <th align="right">قابلیت‌ها</th>
  </tr>
  <tr>
    <td align="right"><strong>ورود و مدیریت داده</strong></td>
    <td align="right">انتخاب فایل، Drag &amp; Drop، ساخت جدول تازه، پیش‌نمایش، انتخاب سلول و ردیف، ویرایش، افزودن یا حذف ردیف و ستون و ذخیره خروجی</td>
  </tr>
  <tr>
    <td align="right"><strong>آماده‌سازی</strong></td>
    <td align="right">تشخیص Header، استخراج عدد از ورودی فارسی و لاتین، تفکیک مقدار خالی و نامعتبر، حفظ صفر و تکرارها و ردیابی موقعیت منبع</td>
  </tr>
  <tr>
    <td align="right"><strong>تحلیل ناهنجاری</strong></td>
    <td align="right">اجرای شش روش، بررسی آمادگی داده، ترکیب شواهد، تفکیک نتیجه هر روش و اولویت‌بندی ردیف‌های نیازمند بررسی</td>
  </tr>
  <tr>
    <td align="right"><strong>نمایش نتیجه</strong></td>
    <td align="right">صفحه نتایج، جزئیات روش‌ها، نمودارهای قابل Zoom و Pan، نمایش ردیف فایل اصلی و تم روشن یا تیره</td>
  </tr>
  <tr>
    <td align="right"><strong>تفسیر و خروجی</strong></td>
    <td align="right">تحلیل اختیاری هوش مصنوعی، گزارش PDF فارسی، ذخیره نمودار و تحلیل مستقل Autoencoder</td>
  </tr>
  <tr>
    <td align="right"><strong>نگهداری محصول</strong></td>
    <td align="right">پردازش‌های پس‌زمینه برای حفظ پاسخ‌گویی رابط، بررسی نسخه جدید، دانلود بسته برنامه و همگام‌سازی کنترل‌شده بخش هوش مصنوعی</td>
  </tr>
</table>

<h3 dir="rtl" align="right">روند معمول کار</h3>

<ol dir="rtl" align="right">
  <li>فایل را وارد کنید یا یک جدول تازه بسازید.</li>
  <li>پیش‌نمایش داده و وضعیت ستون‌ها را بررسی کنید.</li>
  <li>در صورت نیاز داده را ویرایش، مرتب یا تکمیل کنید.</li>
  <li>ستون، ردیف‌ها یا سلول‌های مورد نظر را انتخاب کنید.</li>
  <li>تحلیل را اجرا کنید تا داده آماده و روش‌های مناسب اجرا شوند.</li>
  <li>ردیف‌های غیرمعمول، شواهد روش‌ها و اولویت بررسی را ببینید.</li>
  <li>با نمودارها نتیجه را از زاویه‌های مختلف بررسی کنید.</li>
  <li>در صورت نیاز از Autoencoder، تفسیر هوش مصنوعی یا گزارش PDF استفاده کنید.</li>
</ol>

<h3 dir="rtl" align="right">فرمت‌های پشتیبانی‌شده</h3>

<table dir="rtl">
  <tr>
    <th align="right">عملیات</th>
    <th dir="ltr" align="left">فرمت‌ها</th>
  </tr>
  <tr>
    <td align="right">ورود داده</td>
    <td dir="ltr" align="left"><code>.csv</code>, <code>.xlsx</code>, <code>.xls</code>, <code>.json</code>, <code>.txt</code>, <code>.parquet</code></td>
  </tr>
  <tr>
    <td align="right">ذخیره از رابط</td>
    <td dir="ltr" align="left"><code>.csv</code>, <code>.xlsx</code>, <code>.json</code>, <code>.parquet</code>, <code>.txt</code></td>
  </tr>
</table>

---

<a id="analysis"></a>
<h2 dir="rtl" align="right">موتور تشخیص و Detectorها</h2>

<p dir="rtl" align="right">
  مسیر اصلی تحلیل از شش Detector کلاسیک استفاده می‌کند. این Detectorها یک سؤال را با فرض‌های متفاوت می‌بینند و به همین دلیل ممکن است روی بعضی ردیف‌ها توافق و روی بعضی ردیف‌ها اختلاف داشته باشند. ناهنجو این اختلاف را حذف نمی‌کند؛ نتیجه هر Detector و شواهد ترکیبی را جداگانه نگه می‌دارد.
</p>

<table dir="rtl">
  <tr>
    <th dir="ltr" align="left">Detector</th>
    <th align="right">چیزی که بررسی می‌کند</th>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>Z-Score</strong></td>
    <td align="right">فاصله استانداردشده مقدارها از میانگین</td>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>MAD</strong></td>
    <td align="right">فاصله مقاوم از میانه، با حساسیت کمتر به مقدارهای بسیار دور</td>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>IQR</strong></td>
    <td align="right">قرارگرفتن مقدار بیرون از محدوده چارکی</td>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>LOF</strong></td>
    <td align="right">تفاوت چگالی محلی هر ردیف با همسایه‌های آن</td>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>Isolation Forest</strong></td>
    <td align="right">میزان آسان‌بودن جداسازی مشاهده در ساختارهای تصادفی</td>
  </tr>
  <tr>
    <td dir="ltr" align="left"><strong>One-Class SVM</strong></td>
    <td align="right">فاصله مشاهده از مرز یادگرفته‌شده رفتار غالب</td>
  </tr>
</table>

<p dir="rtl" align="right">
  پیاده‌سازی فعال LOF از
  <code>sklearn.neighbors.LocalOutlierFactor</code>
  در سطح ردیف استفاده می‌کند. مقدارهای تکراری حذف یا دست‌کاری نمی‌شوند،
  <code>contamination="auto"</code>
  است و برنامه سهمیه اجباری برای تعداد خروجی‌ها تعیین نمی‌کند.
</p>

<h3 dir="rtl" align="right">ترکیب شواهد</h3>

<p dir="rtl" align="right">
  پس از اجرای Detectorهای قابل‌استفاده، نتیجه‌ها براساس موقعیت ردیف کنار هم قرار می‌گیرند. اگر چند Detector یک ردیف را علامت بزنند، این توافق به‌عنوان شواهد بیشتر ثبت می‌شود؛ بااین‌حال توافق چند Detector به معنی احتمال کالیبره‌شده صحت نیست.
</p>

<h3 dir="rtl" align="right">شاخص‌های نتیجه</h3>

<ul dir="rtl" align="right">
  <li><strong>مورد نیازمند بررسی:</strong> ردیف یا مقداری که دست‌کم یک Detector معتبر آن را غیرمعمول دیده است.</li>
  <li><strong>شدت نسبی:</strong> قدرت سیگنال در همان اجرای تحلیل، نه میزان خسارت واقعی.</li>
  <li><strong>اطمینان تحلیل:</strong> جمع‌بندی مهندسی از کیفیت اجرا و سازگاری شواهد، نه احتمال درست‌بودن تشخیص.</li>
  <li><strong>سلامت داده:</strong> وضعیت کیفیت و آمادگی ورودی برای تحلیل، نه سنجه دقت روش‌ها.</li>
  <li><strong>اولویت بررسی:</strong> ترتیب پیشنهادی برای بازبینی، نه ریسک مالی یا عملیاتی کالیبره‌شده.</li>
</ul>

<p dir="rtl" align="right">
  ممکن است تحلیل با موفقیت کامل شود و هیچ ردیفی علامت نخورد. این حالت خطا نیست؛ فقط یعنی Detectorهای اجراشده با تنظیمات فعلی موردی برای بررسی پیدا نکرده‌اند.
</p>

<a id="autoencoder"></a>
<h2 dir="rtl" align="right">تحلیل <bdi dir="ltr">Autoencoder</bdi></h2>

<p dir="rtl" align="right">
  بخش Autoencoder یک مسیر بازسازی مستقل از شش Detector کلاسیک است. این بخش تلاش می‌کند رفتار رایج داده را بازسازی کند و سپس فاصله میان داده واقعی و بازسازی‌شده را بسنجد. خطای بازسازی بزرگ‌تر یعنی آن بخش برای مدل‌های همان اجرا ناآشناتر بوده است و باید همراه با زمینه واقعی داده بررسی شود.
</p>

<p dir="rtl" align="right">
  تنظیم پیش‌فرض فعلی از ترکیب
  <code>PCA</code>
  و
  <code>Gaussian Random Projection</code>
  استفاده می‌کند. خروجی شامل خلاصه مدل‌ها، خطای بازسازی، آستانه همان اجرا، ردیف‌های نیازمند بررسی و نمودارهای مقایسه داده واقعی و بازسازی‌شده است.
</p>

<p dir="rtl" align="right">
  نتیجه Autoencoder با نتیجه شش Detector کلاسیک یکی فرض نمی‌شود. یک ردیف ممکن است فقط در تحلیل کلاسیک، فقط در بازسازی، در هر دو مسیر یا در هیچ‌کدام دیده شود.
</p>

---

<a id="ai"></a>
<h2 dir="rtl" align="right">هوش مصنوعی و حریم خصوصی</h2>

<p dir="rtl" align="right">
  هوش مصنوعی در ناهنجو یک لایه اختیاری برای توضیح و گزارش است. محاسبات اصلی، اجرای Detectorها، ترکیب شواهد، نمودارها و ساخت نتیجه بدون هوش مصنوعی انجام می‌شوند. پس از آماده‌شدن نتیجه، کاربر می‌تواند برای جمع‌بندی، توضیح نمودار یا تفسیر Autoencoder از AI استفاده کند.
</p>

<p dir="rtl" align="right">
  هوش مصنوعی اجازه ندارد ردیف جدیدی به نتیجه موتور اضافه کند، موردی را حذف کند یا تصمیم Detectorها را بازنویسی کند. متن تولیدشده باید براساس داده و خلاصه ساختاریافته‌ای باشد که برنامه در اختیار آن قرار می‌دهد.
</p>

<ul dir="rtl" align="right">
  <li><strong>حالت خودکار:</strong> استفاده از تنظیمات سرویس مدیریت‌شده برنامه؛</li>
  <li><strong>حالت دستی:</strong> استفاده از نشانی سرویس، مدل و API Key واردشده توسط کاربر؛</li>
  <li><strong>اطلاعات احتمالی درخواست:</strong> نام فایل یا ستون، خلاصه وضعیت داده، نمونه محدود از داده انتخاب‌شده، خلاصه نتیجه و ردیف‌های علامت‌گذاری‌شده؛</li>
  <li><strong>تحلیل محلی:</strong> استفاده نکردن از AI مانع اجرای موتور اصلی یا تولید PDF علمی نمی‌شود.</li>
</ul>

<p dir="rtl" align="right">
  برای داده حساس، سیاست نگهداری و پردازش اطلاعات سرویس‌دهنده را پیش از ارسال بررسی کنید. API Key نباید در سورس، فایل عمومی، Screenshot، Log یا Commit قرار بگیرد.
</p>

---

<a id="architecture"></a>
<h2 dir="rtl" align="right">معماری سطح‌بالا</h2>

<p dir="rtl" align="right">
  معماری ناهنجو مسیر داده، منطق تحلیل و لایه نمایش را از یکدیگر جدا نگه می‌دارد. نمودار زیر فقط جریان اصلی محصول را نشان می‌دهد و عمداً از اتصال‌های فرعی و فلش‌های متقاطع دوری می‌کند.
</p>

~~~mermaid
flowchart TD
    A["ورود فایل یا ساخت جدول"] --> B["خواندن، تشخیص ساختار و اعتبارسنجی"]
    B --> C["فضای کاری داده و ردیابی ردیف منبع"]
    C --> D["انتخاب داده، استخراج عدد و سنجش کیفیت"]

    D --> E["مسیر تشخیص ناهنجاری"]
    E --> F["اجرای شش Detector کلاسیک"]
    F --> G["ترکیب شواهد و اولویت‌بندی"]
    G --> H["نتایج، نمودارها، هوش مصنوعی و PDF"]

    D --> I["مسیر Autoencoder"]
    I --> J["PCA و Gaussian Random Projection"]
    J --> K["خطای بازسازی و ردیف‌های نیازمند بررسی"]
    K --> L["نمای Autoencoder، هوش مصنوعی و PDF"]
~~~

<h3 dir="rtl" align="right">مرز مسئولیت بخش‌ها</h3>

<table dir="rtl">
  <tr>
    <th align="right">لایه</th>
    <th align="right">مسئولیت</th>
    <th dir="ltr" align="left">مسیر اصلی</th>
  </tr>
  <tr>
    <td align="right">رابط کاربری</td>
    <td align="right">ساخت صفحه‌ها، نمایش وضعیت و دریافت تعامل کاربر</td>
    <td dir="ltr" align="left"><code>ui/</code></td>
  </tr>
  <tr>
    <td align="right">هماهنگی رابط</td>
    <td align="right">اتصال دکمه‌ها، مدیریت صفحه‌ها، Workerها و انتقال نتیجه</td>
    <td dir="ltr" align="left"><code>controllers/</code></td>
  </tr>
  <tr>
    <td align="right">داده</td>
    <td align="right">خواندن فایل، فضای کاری، انتخاب، ردیابی منبع، استخراج عدد و پروفایل</td>
    <td dir="ltr" align="left"><code>data/</code></td>
  </tr>
  <tr>
    <td align="right">تحلیل</td>
    <td align="right">Detectorها، راهبرد اجرا، ترکیب شواهد، رتبه‌بندی و Autoencoder</td>
    <td dir="ltr" align="left"><code>analysis/</code></td>
  </tr>
  <tr>
    <td align="right">تفسیر و خروجی</td>
    <td align="right">هوش مصنوعی، نمودار، صفحه نتایج و گزارش فارسی</td>
    <td dir="ltr" align="left"><code>ai/</code>, <code>reports/</code></td>
  </tr>
  <tr>
    <td align="right">عملیات محصول</td>
    <td align="right">نسخه، منابع، Updater و همگام‌سازی بخش هوش مصنوعی</td>
    <td dir="ltr" align="left"><code>core/</code>, <code>updater/</code></td>
  </tr>
</table>

<p dir="rtl" align="right">
  قرارداد مهم معماری این است که صفحه نتایج، نمودار، PDF و هوش مصنوعی مصرف‌کننده نتیجه موتور هستند. تغییر ظاهر یا متن نباید تصمیم علمی، آستانه یا تعداد ردیف‌های علامت‌گذاری‌شده را تغییر دهد.
</p>

<h3 dir="rtl" align="right">ساختار مخزن</h3>

~~~text
Nahanjo_v2/
|-- main.py                 # Application startup
|-- analysis/               # Detection engines and Autoencoder
|-- data/                   # Loaders, workspace, extraction, profiling
|-- controllers/            # UI coordination, workers, charts
|-- ui/                     # Forms, pages, themes, resources
|-- ai/                     # AI clients and prompt construction
|-- reports/                # Persian PDF generation
|-- updater/                # Update validation and installation
|-- tests/                  # Regression and contract tests
|-- benchmarks/             # Synthetic analysis benchmark
|-- docs/                   # Technical and release documentation
|-- installer/              # Windows installer definition
|-- core/                   # Version, resources, sync, shared services
|-- storage/                # Default local settings
|-- requirements.txt
~~~

---

<a id="development"></a>
<h2 dir="rtl" align="right">توسعه و تست</h2>

<p dir="rtl" align="right">
  کاربران عادی نیازی به اجرای تست یا ساخت برنامه ندارند و باید از نسخه آماده کنار Release استفاده کنند. این بخش فقط برای توسعه‌دهنده‌ای است که سورس را تغییر می‌دهد.
</p>

<h3 dir="rtl" align="right">اجرای تست‌ها</h3>

~~~powershell
$env:QT_QPA_PLATFORM = "offscreen"
py -3.11 -m unittest discover -s tests -v
~~~

<p dir="rtl" align="right">
  تست‌ها مسیر ورود داده، ردیابی منبع، Detectorها، موتورهای ترکیب نتیجه، رابط، نمودارها، Autoencoder، همگام‌سازی AI، Updater و گزارش را پوشش می‌دهند. Benchmark مصنوعی از مسیر
  <code>benchmarks/run_anomaly_benchmark.py</code>
  در دسترس است، اما جایگزین ارزیابی روی داده واقعی هر حوزه نیست.
</p>

<p dir="rtl" align="right">
  فرایند ساخت نسخه آماده و Installer در محیط توسعه انجام می‌شود و فرمان‌های آن عمداً در README کاربرمحور قرار نگرفته‌اند.
</p>

---

<a id="status"></a>
<h2 dir="rtl" align="right">وضعیت، محدودیت‌ها و مسیر توسعه</h2>

<h3 dir="rtl" align="right">وضعیت فعلی</h3>

<ul dir="rtl" align="right">
  <li>نسخه مرجع سورس <code>2.0.3</code> است.</li>
  <li>رابط اصلی فارسی و مبتنی بر PyQt6 است.</li>
  <li>نسخه آماده، Installer و Updater رسمی فعلاً برای Windows x64 هستند.</li>
  <li>مسیر کلاسیک روی توالی عددی انتخاب‌شده کار می‌کند و Autoencoder مسیر بازسازی مستقل دارد.</li>
  <li>گزارش فارسی PDF و نمودارهای تعاملی در خود برنامه تولید می‌شوند.</li>
</ul>

<h3 dir="rtl" align="right">محدودیت‌های مهم</h3>

<ul dir="rtl" align="right">
  <li>هیچ نرخ دقت عمومی برای همه حوزه‌ها ادعا نمی‌شود.</li>
  <li>نتیجه برنامه تشخیص قطعی یا توصیه حقوقی، پزشکی، مالی یا ایمنی نیست.</li>
  <li>کیفیت نتیجه به ساختار داده، اندازه نمونه، توزیع و مناسب‌بودن روش‌ها وابسته است.</li>
  <li>هوش مصنوعی ممکن است Context درخواست را به سرویس خارجی ارسال کند.</li>
  <li>پشتیبانی رسمی Linux و macOS هنوز در مسیر نسخه آماده و QA تثبیت نشده است.</li>
</ul>

<h3 dir="rtl" align="right">جهت توسعه</h3>

<ul dir="rtl" align="right">
  <li>گسترش تحلیل‌های چندمتغیره و چندوجهی در کنار مسیر فعلی؛</li>
  <li>افزودن نماهای تحلیلی مکمل برای کشف رابطه، روند و تغییر رفتار؛</li>
  <li>Benchmarkهای دامنه‌محور با داده مرجع و معیارهای قابل دفاع؛</li>
  <li>تقویت امنیت انتشار عمومی و زنجیره Update؛</li>
  <li>گسترش گزارش‌ها و اتصال کنترل‌شده‌تر هوش مصنوعی به جریان محصول؛</li>
  <li>آماده‌سازی تدریجی برای استفاده گسترده‌تر و سناریوهای سازمانی.</li>
</ul>

---

<a id="security"></a>
<h2 dir="rtl" align="right">امنیت و مجوز</h2>

<ul dir="rtl" align="right">
  <li>فایل‌های <code>.env</code>، API Key، Token، Credential و داده حساس نباید Commit شوند.</li>
  <li>Manifest و بسته Update باید فقط از منبع مورد اعتماد دریافت و با اندازه و SHA-256 معتبر بررسی شوند.</li>
  <li>پیش از عمومی‌کردن Repository، فایل‌های تولیدی، Cacheها، تنظیمات محلی و تاریخچه Git باید از نظر اطلاعات حساس بررسی شوند.</li>
</ul>

<p dir="rtl" align="right">
  توسعه‌دهنده محصول:
  <strong>امیرحسین عبدلی</strong>
  <br>
  نسخه:
  <code>2.0.3</code>
  <br>
  سال:
  <code>2026</code>
</p>

<p dir="rtl" align="right">
  در Snapshot فعلی فایل <code>LICENSE</code> عمومی وجود ندارد. تا زمان افزودن مجوز صریح، همه حقوق محفوظ است و انتشار سورس به معنی اجازه خودکار برای استفاده، بازتوزیع، فروش یا ساخت نسخه مشتق‌شده نیست.
</p>

<p align="center">
  <strong>Nahanjo 2.0.3</strong>
</p>
