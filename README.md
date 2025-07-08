# VirtuSIM API Backend

Backend API untuk layanan virtual phone number VirtuSIM yang di-deploy di Hugging Face Spaces.

## 🚀 Fitur

- ✅ RESTful API dengan FastAPI
- ✅ API Key dari Hugging Face Secrets (VIRTUSIM_API_KEY)
- ✅ CORS support untuk frontend Vercel
- ✅ Dokumentasi API otomatis (Swagger UI)
- ✅ Error handling yang komprehensif
- ✅ Ready untuk production

## 📋 Setup di Hugging Face

### 1. Buat Space Baru
1. Buka [Hugging Face Spaces](https://huggingface.co/spaces)
2. Klik "Create new Space"
3. Pilih **Docker** sebagai SDK
4. Beri nama space (contoh: `username/virtusim-backend`)

### 2. Upload Files
Upload semua file dari repository ini ke Hugging Face Space:
- `app.py` (main application)
- `requirements.txt`
- `Dockerfile`
- `README.md`

### 3. Set API Key & Pricing di Secrets
1. Di Hugging Face Space, buka tab **Settings**
2. Scroll ke bagian **Repository secrets**
3. Tambahkan secrets berikut:
   - **Name**: `VIRTUSIM_API_KEY` | **Value**: API key VirtuSIM Anda
   - **Name**: `MARKUP_PERCENTAGE` | **Value**: `30` (markup 30%, opsional)
   - **Name**: `FIXED_MARKUP` | **Value**: `0` (markup tetap dalam IDR, opsional)
   - **Name**: `MIN_PRICE` | **Value**: `1000` (harga minimum dalam IDR, opsional)

### 4. Deploy
Hugging Face akan otomatis build dan deploy aplikasi Anda.

## 🔗 API Endpoints

Base URL: `https://your-username-virtusim-backend.hf.space`

### Authentication
API key diambil otomatis dari environment variable `VIRTUSIM_API_KEY`.
Jika tidak ada, bisa menggunakan Authorization header:
```
Authorization: Bearer YOUR_VIRTUSIM_API_KEY
```

### Available Endpoints

#### 1. Create Order
```http
POST /order
Content-Type: application/json

{
    "service": "26",
    "operator": "indosat"
}
```

#### 2. Get Active Orders
```http
GET /active-orders
```

#### 3. Check Order Status
```http
GET /status/{order_id}
```

#### 4. Update Order Status
```http
PUT /status
Content-Type: application/json

{
    "order_id": "9323",
    "status": 1
}
```

#### 5. Get Services
```http
GET /services
```

#### 6. Get Services (dengan harga jual)
```http
GET /services
```

#### 7. Calculate Pricing
```http
GET /pricing/{original_price}
```

#### 8. Health Check
```http
GET /health
```

### Operator Types
- `telkomsel`
- `axis`
- `indosat`
- `any` (random)

### Status Codes
- `1` = Ready
- `2` = Cancel
- `3` = Resend
- `4` = Complete

## 💰 Sistem Pricing & Markup

Backend ini mendukung sistem markup otomatis untuk menambahkan profit pada harga VirtuSIM.

### Konfigurasi Pricing

Set environment variables berikut di Hugging Face Secrets:

| Variable | Default | Deskripsi |
|----------|---------|-----------|
| `MARKUP_PERCENTAGE` | `30` | Markup persentase (%) |
| `FIXED_MARKUP` | `0` | Markup tetap (IDR) |
| `MIN_PRICE` | `1000` | Harga minimum (IDR) |

### Cara Kerja Markup

1. **Harga Asli**: Dari VirtuSIM API
2. **Markup Persentase**: `harga_asli * (1 + markup_percentage/100)`
3. **Markup Tetap**: `+ fixed_markup`
4. **Minimum Price**: `max(hasil, min_price)`
5. **Pembulatan**: Dibulatkan ke kelipatan 100

### Contoh Perhitungan

Harga asli: Rp 5.000
- Markup 30%: Rp 5.000 × 1.30 = Rp 6.500
- Fixed markup: Rp 6.500 + Rp 0 = Rp 6.500
- Minimum price: max(Rp 6.500, Rp 1.000) = Rp 6.500
- Pembulatan: Rp 6.500
- **Profit**: Rp 1.500

### Response Format Services

```json
{
  "success": true,
  "data": {
    "data": [
      {
        "id": "26",
        "name": "WhatsApp",
        "price": "5000",
        "display_price": 6500,
        "pricing": {
          "original_price": 5000,
          "markup_percentage": 30,
          "fixed_markup": 0,
          "selling_price": 6500,
          "profit": 1500
        }
      }
    ]
  }
}

## 📖 API Documentation

Setelah deploy, akses dokumentasi API di:
- **Swagger UI**: `https://your-space.hf.space/docs`
- **ReDoc**: `https://your-space.hf.space/redoc`

## 💻 Contoh Penggunaan untuk Frontend Vercel

### JavaScript/Fetch
```javascript
const baseUrl = 'https://your-username-virtusim-backend.hf.space';

// Create order (API key sudah di-set di backend)
const response = await fetch(`${baseUrl}/order`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        service: '26',
        operator: 'indosat'
    })
});

const result = await response.json();
console.log(result);
```

### Next.js API Route
```javascript
// pages/api/virtusim/order.js
export default async function handler(req, res) {
    const baseUrl = 'https://your-username-virtusim-backend.hf.space';
    
    try {
        const response = await fetch(`${baseUrl}/order`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(req.body)
        });
        
        const data = await response.json();
        res.status(200).json(data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to create order' });
    }
}
```

### React Hook
```javascript
// hooks/useVirtuSIM.js
import { useState } from 'react';

const useVirtuSIM = () => {
    const [loading, setLoading] = useState(false);
    const baseUrl = 'https://your-username-virtusim-backend.hf.space';
    
    const createOrder = async (service, operator) => {
        setLoading(true);
        try {
            const response = await fetch(`${baseUrl}/order`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ service, operator })
            });
            
            const data = await response.json();
            return data;
        } catch (error) {
            throw error;
        } finally {
            setLoading(false);
        }
    };
    
    return { createOrder, loading };
};

export default useVirtuSIM;
```

## 🔧 Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variable:
```bash
export VIRTUSIM_API_KEY=your_api_key_here
```

3. Run the server:
```bash
python app.py
```

Server akan berjalan di `http://localhost:7860`

## 📝 Response Format

Semua endpoint mengembalikan response dalam format:
```json
{
    "success": true/false,
    "data": {...},
    "message": "Success/Error message"
}
```

## 🛠️ Troubleshooting

### API Key Issues
- Pastikan `VIRTUSIM_API_KEY` sudah di-set di Hugging Face Secrets
- Cek di endpoint `/health` untuk memastikan API key terkonfigurasi

### CORS Issues
- Backend sudah dikonfigurasi untuk menerima request dari semua origin
- Untuk production, update `allow_origins` di `app.py` dengan domain Vercel Anda

### Deployment Issues
- Pastikan semua file sudah ter-upload ke Hugging Face Space
- Cek logs di Hugging Face Space untuk error details

## 📞 Support

Jika ada masalah, cek:
1. Logs di Hugging Face Space
2. API documentation di `/docs`
3. Health check di `/health`

## 📄 License

MIT License