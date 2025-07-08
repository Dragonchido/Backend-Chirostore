# 🚀 Deployment Guide - Hugging Face Spaces

Panduan lengkap untuk deploy VirtuSIM API Backend ke Hugging Face Spaces.

## 📋 Prerequisites

1. Akun Hugging Face (gratis)
2. API Key VirtuSIM yang valid
3. File-file backend yang sudah siap

## 🔧 Step-by-Step Deployment

### 1. Buat Hugging Face Space

1. **Login ke Hugging Face**
   - Buka [huggingface.co](https://huggingface.co)
   - Login dengan akun Anda

2. **Create New Space**
   - Klik "Spaces" di menu atas
   - Klik "Create new Space"
   - Isi form:
     - **Space name**: `virtusim-backend` (atau nama lain)
     - **License**: MIT
     - **SDK**: Pilih **Docker** ⚠️ (Penting!)
     - **Hardware**: CPU basic (gratis)
     - **Visibility**: Public atau Private (sesuai kebutuhan)

3. **Clone Repository**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/virtusim-backend
   cd virtusim-backend
   ```

### 2. Upload Files

Copy semua file berikut ke folder space Anda:

```
virtusim-backend/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── README.md          # Documentation
├── DEPLOYMENT.md      # This file
└── .gitignore        # Git ignore rules
```

### 3. Set API Key di Secrets

1. **Buka Settings Space**
   - Di halaman space Anda, klik tab **Settings**
   - Scroll ke bagian **Repository secrets**

2. **Tambah Secret**
   - Klik **New secret**
   - **Name**: `VIRTUSIM_API_KEY`
   - **Value**: Masukkan API key VirtuSIM Anda
   - Klik **Add secret**

### 4. Commit & Push

```bash
git add .
git commit -m "Initial deployment"
git push
```

### 5. Monitor Deployment

1. **Build Logs**
   - Kembali ke halaman space
   - Lihat tab **Logs** untuk monitor proses build
   - Build biasanya memakan waktu 2-5 menit

2. **Status Check**
   - Setelah build selesai, space akan menampilkan status "Running"
   - URL space: `https://YOUR_USERNAME-virtusim-backend.hf.space`

## ✅ Verifikasi Deployment

### 1. Test Basic Endpoint
```bash
curl https://YOUR_USERNAME-virtusim-backend.hf.space/
```

Expected response:
```json
{
  "message": "VirtuSIM API Backend",
  "version": "1.0.0",
  "status": "running",
  "api_key_configured": true,
  "documentation": "/docs"
}
```

### 2. Test Health Check
```bash
curl https://YOUR_USERNAME-virtusim-backend.hf.space/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "VirtuSIM API Backend",
  "api_key_configured": true
}
```

### 3. Test API Documentation
Buka di browser:
- Swagger UI: `https://YOUR_USERNAME-virtusim-backend.hf.space/docs`
- ReDoc: `https://YOUR_USERNAME-virtusim-backend.hf.space/redoc`

## 🔧 Configuration untuk Frontend

Setelah backend berhasil di-deploy, gunakan URL berikut di frontend Vercel Anda:

```javascript
const API_BASE_URL = 'https://YOUR_USERNAME-virtusim-backend.hf.space';
```

## 🛠️ Troubleshooting

### Build Gagal

**Problem**: Build error atau timeout
**Solution**:
1. Cek logs di tab **Logs**
2. Pastikan `Dockerfile` dan `requirements.txt` benar
3. Coba push ulang

### API Key Tidak Terkonfigurasi

**Problem**: `api_key_configured: false` di response
**Solution**:
1. Pastikan secret `VIRTUSIM_API_KEY` sudah ditambahkan
2. Restart space: Settings → Restart this Space
3. Tunggu beberapa menit untuk reload

### CORS Error dari Frontend

**Problem**: Frontend tidak bisa akses API
**Solution**:
1. Pastikan CORS sudah dikonfigurasi di `app.py`
2. Untuk production, update `allow_origins` dengan domain Vercel

### Space Sleep/Inactive

**Problem**: Space menjadi inactive setelah tidak digunakan
**Solution**:
1. Hugging Face free tier akan sleep setelah tidak aktif
2. Space akan otomatis wake up saat ada request
3. Untuk always-on, upgrade ke paid tier

## 📊 Monitoring & Maintenance

### 1. Logs Monitoring
- Akses logs real-time di tab **Logs**
- Monitor error dan performance

### 2. Usage Statistics
- Lihat usage di dashboard Hugging Face
- Monitor request volume

### 3. Updates
Untuk update code:
```bash
git pull  # Get latest changes
# Make your changes
git add .
git commit -m "Update: description"
git push
```

## 🔒 Security Best Practices

1. **API Key Security**
   - Jangan commit API key ke git
   - Selalu gunakan Hugging Face secrets
   - Rotate API key secara berkala

2. **CORS Configuration**
   - Untuk production, set specific domains di `allow_origins`
   - Jangan gunakan `["*"]` di production

3. **Rate Limiting**
   - Implementasi rate limiting jika diperlukan
   - Monitor usage untuk detect abuse

## 📞 Support

Jika mengalami masalah:

1. **Check Logs**: Tab Logs di Hugging Face Space
2. **Health Check**: Test endpoint `/health`
3. **Documentation**: Akses `/docs` untuk API reference
4. **Community**: Hugging Face Discord/Forum

## 🎉 Next Steps

Setelah backend berhasil di-deploy:

1. **Frontend Integration**: Integrate dengan frontend Vercel
2. **Testing**: Test semua endpoint dengan data real
3. **Monitoring**: Setup monitoring dan alerting
4. **Documentation**: Update dokumentasi API sesuai kebutuhan

---

**Happy Deploying! 🚀**