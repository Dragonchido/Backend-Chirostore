# 💰 Contoh Konfigurasi Pricing

Panduan konfigurasi pricing untuk berbagai model bisnis reseller VirtuSIM.

## 🎯 Skenario Bisnis

### 1. Markup Persentase Sederhana (30%)
**Target**: Profit konsisten 30% dari harga asli
```env
MARKUP_PERCENTAGE=30
FIXED_MARKUP=0
MIN_PRICE=1000
```

**Contoh**:
- Harga asli: Rp 5.000 → Harga jual: Rp 6.500 → Profit: Rp 1.500
- Harga asli: Rp 10.000 → Harga jual: Rp 13.000 → Profit: Rp 3.000

### 2. Markup Tetap untuk Layanan Murah
**Target**: Profit minimum Rp 1.000 untuk semua layanan
```env
MARKUP_PERCENTAGE=0
FIXED_MARKUP=1000
MIN_PRICE=2000
```

**Contoh**:
- Harga asli: Rp 3.000 → Harga jual: Rp 4.000 → Profit: Rp 1.000
- Harga asli: Rp 8.000 → Harga jual: Rp 9.000 → Profit: Rp 1.000

### 3. Kombinasi Persentase + Tetap
**Target**: Profit minimum + persentase untuk layanan mahal
```env
MARKUP_PERCENTAGE=20
FIXED_MARKUP=500
MIN_PRICE=2000
```

**Contoh**:
- Harga asli: Rp 5.000 → Harga jual: Rp 6.500 → Profit: Rp 1.500
- Harga asli: Rp 15.000 → Harga jual: Rp 18.500 → Profit: Rp 3.500

### 4. Premium Pricing (Markup Tinggi)
**Target**: Profit maksimal untuk target market premium
```env
MARKUP_PERCENTAGE=50
FIXED_MARKUP=1000
MIN_PRICE=3000
```

**Contoh**:
- Harga asli: Rp 4.000 → Harga jual: Rp 7.000 → Profit: Rp 3.000
- Harga asli: Rp 10.000 → Harga jual: Rp 16.000 → Profit: Rp 6.000

### 5. Volume Discount (Markup Rendah)
**Target**: Harga kompetitif untuk volume tinggi
```env
MARKUP_PERCENTAGE=15
FIXED_MARKUP=200
MIN_PRICE=1500
```

**Contoh**:
- Harga asli: Rp 5.000 → Harga jual: Rp 6.000 → Profit: Rp 1.000
- Harga asli: Rp 20.000 → Harga jual: Rp 23.200 → Profit: Rp 3.200

## 📊 Analisis Profit

### Tabel Perbandingan Skenario

| Harga Asli | Sederhana (30%) | Tetap (Rp1k) | Kombinasi | Premium (50%+1k) | Volume (15%+200) |
|------------|-----------------|---------------|-----------|-------------------|------------------|
| Rp 2.000   | Rp 2.600        | Rp 3.000      | Rp 2.900  | Rp 4.000          | Rp 2.500         |
| Rp 5.000   | Rp 6.500        | Rp 6.000      | Rp 6.500  | Rp 8.500          | Rp 6.000         |
| Rp 10.000  | Rp 13.000       | Rp 11.000     | Rp 12.500 | Rp 16.000         | Rp 11.700        |
| Rp 20.000  | Rp 26.000       | Rp 21.000     | Rp 24.500 | Rp 31.000         | Rp 23.200        |

### Profit per Transaksi

| Harga Asli | Sederhana | Tetap | Kombinasi | Premium | Volume |
|------------|-----------|-------|-----------|---------|--------|
| Rp 2.000   | Rp 600    | Rp 1.000 | Rp 900 | Rp 2.000 | Rp 500 |
| Rp 5.000   | Rp 1.500  | Rp 1.000 | Rp 1.500 | Rp 3.500 | Rp 1.000 |
| Rp 10.000  | Rp 3.000  | Rp 1.000 | Rp 2.500 | Rp 6.000 | Rp 1.700 |
| Rp 20.000  | Rp 6.000  | Rp 1.000 | Rp 4.500 | Rp 11.000 | Rp 3.200 |

## 🎯 Rekomendasi Berdasarkan Target Market

### Pemula/Mahasiswa (Budget Terbatas)
```env
MARKUP_PERCENTAGE=20
FIXED_MARKUP=300
MIN_PRICE=1500
```
- Harga kompetitif
- Profit wajar
- Volume tinggi

### Bisnis Menengah (Balanced)
```env
MARKUP_PERCENTAGE=30
FIXED_MARKUP=500
MIN_PRICE=2000
```
- Profit optimal
- Harga masih terjangkau
- Sustainable

### Enterprise/Premium
```env
MARKUP_PERCENTAGE=40
FIXED_MARKUP=1000
MIN_PRICE=3000
```
- Profit maksimal
- Target customer premium
- Service quality tinggi

## 🔧 Tips Optimasi Pricing

### 1. Monitor Kompetitor
- Cek harga kompetitor secara berkala
- Adjust markup sesuai market
- Pertahankan competitive advantage

### 2. A/B Testing
- Test berbagai markup percentage
- Monitor conversion rate
- Optimize berdasarkan data

### 3. Dynamic Pricing
- Markup berbeda per layanan
- Seasonal adjustment
- Volume-based pricing

### 4. Customer Segmentation
- Pricing tier berbeda
- Loyalty program
- Bulk discount

## 📈 Strategi Scaling

### Phase 1: Market Entry
```env
MARKUP_PERCENTAGE=25
FIXED_MARKUP=300
MIN_PRICE=1500
```

### Phase 2: Growth
```env
MARKUP_PERCENTAGE=30
FIXED_MARKUP=500
MIN_PRICE=2000
```

### Phase 3: Mature
```env
MARKUP_PERCENTAGE=35
FIXED_MARKUP=700
MIN_PRICE=2500
```

## 🛠️ Tools untuk Monitoring

### 1. Profit Calculator
```bash
curl https://your-space.hf.space/pricing/5000
```

### 2. Batch Price Check
```javascript
const prices = [2000, 5000, 10000, 15000, 20000];
prices.forEach(async (price) => {
    const response = await fetch(`/pricing/${price}`);
    const data = await response.json();
    console.log(`Rp ${price} → Rp ${data.data.selling_price} (Profit: Rp ${data.data.profit})`);
});
```

### 3. Profit Analysis
```javascript
// Calculate total profit from sales data
const calculateTotalProfit = (sales) => {
    return sales.reduce((total, sale) => {
        return total + (sale.selling_price - sale.original_price);
    }, 0);
};
```

## 💡 Best Practices

1. **Start Conservative**: Mulai dengan markup rendah, naikkan bertahap
2. **Monitor Metrics**: Track conversion rate, customer satisfaction
3. **Flexible Pricing**: Siap adjust berdasarkan market feedback
4. **Transparent Communication**: Jelaskan value proposition ke customer
5. **Regular Review**: Review pricing strategy setiap bulan

## 🚨 Warning

- Jangan set markup terlalu tinggi di awal
- Monitor customer feedback tentang pricing
- Pastikan tetap kompetitif dengan market
- Backup pricing strategy jika ada perubahan market

---

**Happy Selling! 💰**