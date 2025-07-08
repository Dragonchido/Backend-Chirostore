#!/usr/bin/env python3
"""
Test script untuk sistem pricing VirtuSIM Backend
"""

import requests
import json
import os
from typing import List, Dict

# Configuration
BASE_URL = "http://localhost:7860"
TEST_PRICES = [1000, 2500, 5000, 7500, 10000, 15000, 20000, 25000]

def test_pricing_endpoint(prices: List[int]) -> None:
    """Test pricing endpoint dengan berbagai harga"""
    print("🧪 Testing Pricing Endpoint")
    print("=" * 50)
    
    for price in prices:
        try:
            response = requests.get(f"{BASE_URL}/pricing/{price}")
            if response.status_code == 200:
                data = response.json()
                pricing = data['data']
                print(f"Rp {price:,} → Rp {pricing['selling_price']:,} (Profit: Rp {pricing['profit']:,})")
            else:
                print(f"❌ Error for price {price}: {response.status_code}")
        except Exception as e:
            print(f"❌ Exception for price {price}: {e}")
    
    print()

def test_root_endpoint() -> None:
    """Test root endpoint untuk melihat konfigurasi"""
    print("🏠 Testing Root Endpoint")
    print("=" * 50)
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"Status: {data['status']}")
            print(f"API Key Configured: {data['api_key_configured']}")
            print("Pricing Config:")
            for key, value in data['pricing_config'].items():
                print(f"  - {key}: {value}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()

def calculate_profit_scenarios() -> None:
    """Hitung profit untuk berbagai skenario markup"""
    print("📊 Profit Analysis for Different Markup Scenarios")
    print("=" * 60)
    
    scenarios = [
        {"name": "Conservative", "markup_pct": 20, "fixed": 300, "min_price": 1500},
        {"name": "Balanced", "markup_pct": 30, "fixed": 500, "min_price": 2000},
        {"name": "Aggressive", "markup_pct": 40, "fixed": 1000, "min_price": 2500},
        {"name": "Premium", "markup_pct": 50, "fixed": 1500, "min_price": 3000},
    ]
    
    test_prices = [2000, 5000, 10000, 15000, 20000]
    
    # Header
    print(f"{'Price':<10}", end="")
    for scenario in scenarios:
        print(f"{scenario['name']:<12}", end="")
    print()
    print("-" * 60)
    
    # Calculate for each price
    for price in test_prices:
        print(f"Rp {price:,}".ljust(10), end="")
        
        for scenario in scenarios:
            # Simulate markup calculation
            markup_pct = scenario['markup_pct']
            fixed = scenario['fixed']
            min_price = scenario['min_price']
            
            # Calculate selling price
            price_with_pct = price * (1 + markup_pct / 100)
            final_price = price_with_pct + fixed
            final_price = max(final_price, min_price)
            final_price = round(final_price / 100) * 100
            
            profit = final_price - price
            print(f"Rp {profit:,}".ljust(12), end="")
        
        print()
    
    print()

def test_health_endpoint() -> None:
    """Test health endpoint"""
    print("❤️  Testing Health Endpoint")
    print("=" * 50)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Status: {data['status']}")
            print(f"Timestamp: {data['timestamp']}")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print()

def main():
    """Main test function"""
    print("🚀 VirtuSIM Backend Pricing Test")
    print("=" * 60)
    print()
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code != 200:
            print("❌ Server tidak berjalan atau tidak dapat diakses")
            print(f"Pastikan server berjalan di {BASE_URL}")
            return
    except:
        print("❌ Server tidak berjalan atau tidak dapat diakses")
        print(f"Pastikan server berjalan di {BASE_URL}")
        print("\nUntuk menjalankan server:")
        print("python app.py")
        return
    
    # Run tests
    test_health_endpoint()
    test_root_endpoint()
    test_pricing_endpoint(TEST_PRICES)
    calculate_profit_scenarios()
    
    print("✅ Testing completed!")

if __name__ == "__main__":
    main()