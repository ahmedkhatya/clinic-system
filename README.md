# Clinic System — Docker Setup

## الملفات المهمة
```
├── Dockerfile          → صورة الـ App
├── Dockerfile.db       → صورة الـ PostgreSQL
├── docker-compose.yml  → بيربطهم مع بعض
├── .env.example        → نموذج المتغيرات
├── start.sh            → سكريبت التشغيل
└── .github/
    └── workflows/
        └── deploy.yml  → GitHub Actions
```

## خطوات الإعداد

### 1. اعمل .env
```bash
cp .env.example .env
# عدّل القيم جوا .env
```

### 2. ارفع على GitHub
```bash
git add .
git commit -m "initial commit"
git push origin main
```
GitHub Actions هيبني ويبعت الـ images تلقائياً لـ GHCR

### 3. على أي سيرفر عنده Docker
```bash
# نزّل الكود
git clone https://github.com/YOUR_USERNAME/clinic-system
cd clinic-system

# اعمل .env
cp .env.example .env
nano .env   # عدّل القيم

# شغّل
./start.sh
```

## الـ Images على GHCR
- `ghcr.io/YOUR_USERNAME/clinic-app:latest`
- `ghcr.io/YOUR_USERNAME/clinic-db:latest`
