#!/usr/bin/env python3
"""
Simple script to verify repository access and basic functionality.
This demonstrates that the repository is accessible and functional.
"""

import os
import sys

def verify_repo_structure():
    """Verify that key repository files and directories exist."""
    required_paths = [
        "zeno_agent",
        "zeno_agent/agent.py",
        "zeno_agent/requirements.txt",
        "Dockerfile",
        "README.md",
    ]
    
    print("Verifying repository structure...")
    all_exist = True
    for path in required_paths:
        exists = os.path.exists(path)
        status = "✓" if exists else "✗"
        print(f"  {status} {path}")
        if not exists:
            all_exist = False
    
    return all_exist

def verify_imports():
    """Verify that key modules can be imported."""
    print("\nVerifying Python imports...")
    try:
        # Test basic imports
        import fastapi
        print("  ✓ fastapi")
        
        import uvicorn
        print("  ✓ uvicorn")
        
        # Set dummy environment variables to allow imports
        os.environ.setdefault("DATABASE_URL", "postgresql://dummy:dummy@localhost/dummy")
        os.environ.setdefault("GOOGLE_API_KEY", "dummy_api_key")
        
        # Try importing the agent module
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from zeno_agent import agent
        print("  ✓ zeno_agent.agent")
        
        return True
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_app_structure():
    """Verify the FastAPI app structure."""
    print("\nVerifying application structure...")
    try:
        # Ensure environment variables are set
        os.environ.setdefault("DATABASE_URL", "postgresql://dummy:dummy@localhost/dummy")
        os.environ.setdefault("GOOGLE_API_KEY", "dummy_api_key")
        
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from zeno_agent.agent import app, health
        
        # Check that the app has required routes
        routes = [route.path for route in app.routes]
        print(f"  ✓ FastAPI app created with {len(routes)} routes")
        
        # Check health endpoint
        if "/healthz" in routes:
            print("  ✓ Health check endpoint exists at /healthz")
        
        # Test health function
        health_result = health()
        if health_result.get("status") == "ok":
            print("  ✓ Health check returns correct status")
        
        return True
    except Exception as e:
        print(f"  ✗ App verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main verification function."""
    print("=" * 60)
    print("Repository Access Verification")
    print("=" * 60)
    
    results = []
    
    # Run verifications
    results.append(("Repository Structure", verify_repo_structure()))
    results.append(("Python Imports", verify_imports()))
    results.append(("Application Structure", verify_app_structure()))
    
    # Summary
    print("\n" + "=" * 60)
    print("Verification Summary")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"  {symbol} {name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ Repository is accessible and functional!")
        print("=" * 60)
        return 0
    else:
        print("✗ Some verifications failed. Check output above.")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
