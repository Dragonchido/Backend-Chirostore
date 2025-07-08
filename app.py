from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, Dict, Any
import httpx
import os
from enum import Enum

# Initialize FastAPI app
app = FastAPI(
    title="VirtuSIM API Backend",
    description="Backend API untuk layanan virtual phone number VirtuSIM",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware untuk akses dari frontend Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Untuk production, ganti dengan domain Vercel Anda
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer(auto_error=False)

# Constants
VIRTUSIM_API_URL = "https://virtusim.com/api/json.php"
VIRTUSIM_API_KEY = os.getenv("VIRTUSIM_API_KEY")  # API key dari Hugging Face secrets

# Enums
class OperatorType(str, Enum):
    telkomsel = "telkomsel"
    axis = "axis"
    indosat = "indosat"
    any = "any"

class OrderStatus(int, Enum):
    ready = 1
    cancel = 2
    resend = 3
    complete = 4

# Pydantic models
class OrderRequest(BaseModel):
    service: str
    operator: OperatorType

class StatusRequest(BaseModel):
    order_id: str

class SetStatusRequest(BaseModel):
    order_id: str
    status: OrderStatus

class ApiResponse(BaseModel):
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None

# Helper functions
async def get_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Extract API key dari environment variable atau Authorization header"""
    # Prioritas: Environment variable (Hugging Face secrets)
    if VIRTUSIM_API_KEY:
        return VIRTUSIM_API_KEY
    
    # Fallback: Authorization header
    if credentials:
        return credentials.credentials
    
    # Error jika tidak ada keduanya
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API key required. Set VIRTUSIM_API_KEY di Hugging Face secrets atau gunakan Authorization header"
    )

async def call_virtusim_api(post_data: Dict[str, Any]) -> Dict[str, Any]:
    """Make API call ke VirtuSIM"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                VIRTUSIM_API_URL,
                data=post_data,
                headers={
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                timeout=30.0
            )
            response.raise_for_status()
            
            # Handle response
            try:
                return response.json()
            except:
                # Jika response bukan JSON, return sebagai text
                return {"response": response.text}
                
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"VirtuSIM API error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )

# API Endpoints
@app.get("/")
async def root():
    """Root endpoint dengan informasi API"""
    return {
        "message": "VirtuSIM API Backend",
        "version": "1.0.0",
        "status": "running",
        "api_key_configured": bool(VIRTUSIM_API_KEY),
        "documentation": "/docs",
        "endpoints": {
            "POST /order": "Buat pesanan baru",
            "GET /active-orders": "Dapatkan pesanan aktif",
            "GET /status/{order_id}": "Cek status pesanan",
            "PUT /status": "Update status pesanan",
            "GET /services": "Dapatkan layanan tersedia"
        }
    }

@app.post("/order", response_model=ApiResponse)
async def create_order(
    order_request: OrderRequest,
    api_key: str = Depends(get_api_key)
):
    """Buat pesanan baru untuk virtual phone number"""
    post_data = {
        'api_key': api_key,
        'action': 'order',
        'service': order_request.service,
        'operator': order_request.operator.value
    }
    
    result = await call_virtusim_api(post_data)
    
    return ApiResponse(
        success=True,
        data=result,
        message="Pesanan berhasil dibuat"
    )

@app.get("/active-orders", response_model=ApiResponse)
async def get_active_orders(api_key: str = Depends(get_api_key)):
    """Dapatkan pesanan aktif/SMS OTP"""
    post_data = {
        'api_key': api_key,
        'action': 'active_order'
    }
    
    result = await call_virtusim_api(post_data)
    
    return ApiResponse(
        success=True,
        data=result,
        message="Pesanan aktif berhasil diambil"
    )

@app.get("/status/{order_id}", response_model=ApiResponse)
async def check_order_status(
    order_id: str,
    api_key: str = Depends(get_api_key)
):
    """Cek status pesanan tertentu"""
    post_data = {
        'api_key': api_key,
        'action': 'status',
        'id': order_id
    }
    
    result = await call_virtusim_api(post_data)
    
    return ApiResponse(
        success=True,
        data=result,
        message="Status pesanan berhasil diambil"
    )

@app.put("/status", response_model=ApiResponse)
async def update_order_status(
    status_request: SetStatusRequest,
    api_key: str = Depends(get_api_key)
):
    """Update status pesanan"""
    post_data = {
        'api_key': api_key,
        'action': 'set_status',
        'id': status_request.order_id,
        'status': str(status_request.status.value)
    }
    
    result = await call_virtusim_api(post_data)
    
    return ApiResponse(
        success=True,
        data=result,
        message="Status pesanan berhasil diupdate"
    )

@app.get("/services", response_model=ApiResponse)
async def get_services(api_key: str = Depends(get_api_key)):
    """Dapatkan layanan yang tersedia"""
    post_data = {
        'api_key': api_key,
        'action': 'services'
    }
    
    result = await call_virtusim_api(post_data)
    
    return ApiResponse(
        success=True,
        data=result,
        message="Layanan berhasil diambil"
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check untuk monitoring"""
    return {
        "status": "healthy",
        "service": "VirtuSIM API Backend",
        "api_key_configured": bool(VIRTUSIM_API_KEY)
    }

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "success": False,
        "message": exc.detail,
        "status_code": exc.status_code
    }

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return {
        "success": False,
        "message": "Internal server error",
        "error": str(exc)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 7860)),
        reload=False
    )