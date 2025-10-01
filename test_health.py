#!/usr/bin/env python3
"""
Quick health check test for the Zeno AI API
"""

import os
import sys
import time
import requests
from subprocess import Popen, PIPE
import signal

def test_health_endpoint():
    """Test the /healthz endpoint"""
    print("Testing Zeno AI Health Check Endpoint...")
    print("-" * 60)
    
    # Set dummy environment variables
    env = os.environ.copy()
    env["DATABASE_URL"] = "postgresql://dummy:dummy@localhost/dummy"
    env["GOOGLE_API_KEY"] = "dummy_key"
    
    # Start the server
    print("Starting server...")
    server_process = Popen(
        ["uvicorn", "zeno_agent.agent:app", "--host", "127.0.0.1", "--port", "8081"],
        env=env,
        stdout=PIPE,
        stderr=PIPE,
        text=True
    )
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        # Test the health endpoint
        print("Testing health endpoint at http://127.0.0.1:8081/healthz")
        response = requests.get("http://127.0.0.1:8081/healthz", timeout=5)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200 and response.json().get("status") == "ok":
            print("\n✓ Health check endpoint is working correctly!")
            return True
        else:
            print("\n✗ Health check endpoint returned unexpected response")
            return False
            
    except Exception as e:
        print(f"\n✗ Error testing endpoint: {e}")
        return False
        
    finally:
        # Stop the server
        print("\nStopping server...")
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except:
            server_process.kill()

if __name__ == "__main__":
    success = test_health_endpoint()
    sys.exit(0 if success else 1)
