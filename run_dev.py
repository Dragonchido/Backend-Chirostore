#!/usr/bin/env python3
"""
Development server runner dengan konfigurasi pricing yang mudah diubah
"""

import os
import sys
import uvicorn
from pathlib import Path

def load_env_file(env_file: str = ".env"):
    """Load environment variables from file"""
    env_path = Path(env_file)
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value
        print(f"✅ Loaded environment from {env_file}")
    else:
        print(f"⚠️  {env_file} not found, using default values")

def set_development_config():
    """Set development configuration"""
    # Default development settings
    dev_config = {
        'MARKUP_PERCENTAGE': '30',
        'FIXED_MARKUP': '500',
        'MIN_PRICE': '2000',
        'VIRTUSIM_API_KEY': 'demo_key_for_testing'  # Demo key
    }
    
    for key, default_value in dev_config.items():
        if key not in os.environ:
            os.environ[key] = default_value
    
    print("🔧 Development configuration:")
    print(f"   Markup Percentage: {os.environ.get('MARKUP_PERCENTAGE')}%")
    print(f"   Fixed Markup: Rp {os.environ.get('FIXED_MARKUP')}")
    print(f"   Minimum Price: Rp {os.environ.get('MIN_PRICE')}")
    print(f"   API Key: {'✅ Set' if os.environ.get('VIRTUSIM_API_KEY') else '❌ Not set'}")

def main():
    """Main function"""
    print("🚀 VirtuSIM Backend - Development Server")
    print("=" * 50)
    
    # Load environment file if exists
    load_env_file()
    
    # Set development configuration
    set_development_config()
    
    print("\n📡 Starting server...")
    print("   URL: http://localhost:7860")
    print("   Docs: http://localhost:7860/docs")
    print("   Health: http://localhost:7860/health")
    print("\n💡 Tips:")
    print("   - Edit .env file to change pricing configuration")
    print("   - Run test_pricing.py to test pricing calculations")
    print("   - Press Ctrl+C to stop server")
    print("\n" + "=" * 50)
    
    try:
        # Import and run the app
        from app import app
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=7860,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()