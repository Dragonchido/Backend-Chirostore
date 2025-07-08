# 🔧 Setup Instructions untuk Auto-Deploy

## 1. GitHub Repository Secrets

Untuk mengaktifkan auto-deploy ke Hugging Face, tambahkan secret berikut:

### Langkah-langkah:
1. Buka repository GitHub: https://github.com/Dragonchido/Backend-Chirostore
2. Klik **Settings** tab
3. Di sidebar kiri, klik **Secrets and variables** → **Actions**
4. Klik **New repository secret**
5. Tambahkan secret:
   - **Name**: `HF_TOKEN`
   - **Value**: `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`
6. Klik **Add secret**

## 2. Hugging Face Space Secrets

Setelah PR di-merge dan auto-deploy berjalan, set secrets di HF Space:

### Langkah-langkah:
1. Buka HF Space: https://huggingface.co/spaces/Minatoz997/Chirostore
2. Klik **Settings** tab
3. Scroll ke **Repository secrets**
4. Tambahkan secrets berikut:

| Secret Name | Value | Required |
|-------------|-------|----------|
| `VIRTUSIM_API_KEY` | API key VirtuSIM Anda | ✅ Required |
| `MARKUP_PERCENTAGE` | `30` | ❌ Optional (default: 30) |
| `FIXED_MARKUP` | `500` | ❌ Optional (default: 0) |
| `MIN_PRICE` | `1000` | ❌ Optional (default: 1000) |

## 3. Workflow Deployment

Setelah setup secrets:

1. **Merge PR** → Auto-deploy akan berjalan
2. **Check workflow** di GitHub Actions tab
3. **Verify deployment** di https://minatoz997-chirostore.hf.space/health
4. **Test API** di https://minatoz997-chirostore.hf.space/docs

## 4. Troubleshooting

### Jika deployment gagal:
1. Check GitHub Actions logs untuk error details
2. Pastikan HF_TOKEN valid dan memiliki write access
3. Pastikan HF Space `Minatoz997/Chirostore` exists

### Jika API tidak berfungsi:
1. Check HF Space logs
2. Pastikan `VIRTUSIM_API_KEY` sudah di-set di HF Space secrets
3. Test health endpoint: https://minatoz997-chirostore.hf.space/health

## 5. Success Indicators

✅ **GitHub Actions workflow** completed successfully  
✅ **HF Space** shows "Running" status  
✅ **Health endpoint** returns 200 OK  
✅ **API docs** accessible di `/docs`  
✅ **Services endpoint** returns pricing data  

## 🚀 Ready to Launch!

Setelah semua setup selesai, backend VirtuSIM Anda siap untuk:
- Handle orders dari frontend
- Calculate pricing dengan profit margin
- Auto-deploy setiap ada update code
- Scale untuk business growth

Happy coding! 💰