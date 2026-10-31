# راهنمای دیپلوی پروفایل گیت‌هاب

## 1) شخصی‌سازی
1. در `data/profile.json` مقدار `YOUR_GITHUB_USERNAME` را با یوزرنیم دقیق GitHub عوض کن.
2. نام نمایشی، عنوان شغلی، مهارت‌ها، تمرکز و گواهینامه‌ها را بازبینی کن؛ هر چیزی که نمی‌خواهی عمومی باشد حذف کن.
3. تصویر فعلی به ASCII تک‌رنگ تبدیل شده و فایل `assets/ascii-portrait.svg` است. برای تغییر عکس، `scripts/make_ascii_svg.py` را می‌توانی بعداً اضافه/اجرا کنی یا همین SVG را جایگزین کنی.

## 2) ساخت Repository مخصوص پروفایل
1. وارد https://github.com/new شو.
2. نام Repository باید دقیقاً برابر username باشد (مثلاً اگر username برابر `daniel-dev` است، نام repo هم `daniel-dev`).
3. حتماً **Public** را انتخاب کن و گزینه Add a README را خاموش بگذار (چون README آماده در این پروژه هست).
4. Create repository را بزن.

## 3) آپلود فایل‌ها با Git (ویندوز / macOS / لینوکس)
Git را نصب کن و ترمینال را در پوشه `github-profile-kit` باز کن. سپس: 

```bash
git init
git branch -M main
git add .
git commit -m "Build animated GitHub profile README"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME.git
git push -u origin main
```

هر دو `YOUR_GITHUB_USERNAME` را با یوزرنیم خودت جایگزین کن. اگر Git نام و ایمیل خواست، با اطلاعاتی که می‌خواهی در commitها نمایش داده شود تنظیم کن:

```bash
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_NOREPLY_OR_PUBLIC_EMAIL"
```

اگر هنگام push احراز هویت خواست، از Git Credential Manager یا ورود مرورگری GitHub استفاده کن؛ رمز حساب را به‌عنوان پسورد Git وارد نکن.

## 4) فعال کردن به‌روزرسانی روزانه نمودار
1. در repo به Settings → Actions → General برو.
2. در بخش Workflow permissions، گزینه **Read and write permissions** را انتخاب و Save کن. (Workflow هم `contents: write` درخواست می‌کند.)
3. وارد Actions شو، workflow با نام **Update profile art** را باز کن و Run workflow را بزن.
4. بعد از پایان موفق، فایل `contrib-heatmap.svg` و `data/contributions.json` باید به‌روزرسانی شده باشند.

## 5) بررسی
به `https://github.com/YOUR_GITHUB_USERNAME` برو و صفحه را Refresh کن. README باید بالای پروفایل دیده شود.

## نکات
- پروفایل README فقط وقتی خودکار روی پروفایل نمایش داده می‌شود که repo عمومی و نامش دقیقاً برابر username باشد و README.md در ریشه داشته باشد.
- عکس به شکل ASCII در repo قرار می‌گیرد؛ فایل اصلی عکس در بسته نیست. با این حال ASCII هم می‌تواند قابل بازشناسی باشد، پس قبل از public کردن تصمیم بگیر.
- GitHub ممکن است ساختار HTML تقویم مشارکت‌ها را تغییر دهد؛ اگر fetch script خطای `No contribution cells found` داد، باید parser به markup جدید به‌روزرسانی شود.
- GitHub Actions زمان‌بندی‌شده ممکن است با تأخیر اجرا شود؛ برای تست از Run workflow استفاده کن.
- این پروژه برای اجرای روزانه به Personal Access Token نیاز ندارد؛ فقط از صفحه عمومی contribution calendar استفاده می‌کند.
