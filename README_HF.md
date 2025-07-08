---
title: VirtuSIM Backend API
emoji: 📱
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
license: mit
---

# 📱 VirtuSIM Backend API

Backend API untuk virtual SIM card trading dengan sistem pricing otomatis.

## 🚀 Features

- ✅ VirtuSIM API integration
- ✅ Advanced pricing system dengan markup
- ✅ CORS support untuk frontend
- ✅ Auto-generated API documentation
- ✅ Health monitoring

## 📖 API Documentation

Akses dokumentasi lengkap di: `/docs`

## 🔧 Configuration

Set environment variables berikut di Space secrets:

- `VIRTUSIM_API_KEY` - API key VirtuSIM (required)
- `MARKUP_PERCENTAGE` - Persentase markup (default: 30)
- `FIXED_MARKUP` - Fixed markup dalam IDR (default: 0)
- `MIN_PRICE` - Minimum price dalam IDR (default: 1000)

## 💰 Business Model

Sistem pricing otomatis dengan profit calculation:
- Markup percentage configurable
- Fixed amount markup
- Smart price rounding
- Minimum price enforcement

## 🔗 Endpoints

- `POST /order` - Create order
- `GET /active-orders` - Get active orders
- `GET /status/{id}` - Check status
- `PUT /status` - Update status
- `GET /services` - Get services dengan pricing
- `GET /pricing/{price}` - Calculate markup
- `GET /health` - Health check

## 🏗️ Built With

- FastAPI
- Python 3.11
- Uvicorn
- httpx

## 📄 License

MIT License