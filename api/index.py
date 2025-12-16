"""
Vercel serverless function entry point for Flask application
"""
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import app

# Export the Flask app for Vercel
# Vercel will automatically handle the WSGI interface
def handler(request):
    """Vercel serverless function handler"""
    return app(request.environ, request.start_response)

# For Vercel Python runtime
if __name__ == "__main__":
    app.run()

