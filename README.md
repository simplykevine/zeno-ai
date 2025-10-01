# Zeno AI - East African Agricultural Trade Advisor

## Repository Status
✅ **Repository is accessible and functional**

This repository contains the Zeno AI agent, a specialized AI assistant for East African agricultural trade analysis. The system provides scenario analysis, forecasting, and comparative analysis for agricultural commodities in the East African region.

## Overview

Zeno is an intelligent agent designed to help analyze agricultural trade patterns, forecast market trends, and simulate various economic scenarios for key commodities in East Africa.

### Supported Regions
- Kenya
- Rwanda
- Tanzania
- Uganda
- Ethiopia

### Supported Commodities
- Maize
- Coffee
- Tea

## Features

1. **Scenario Analysis**: Simulate "what-if" scenarios for price changes and market shocks
2. **Forecasting**: Predict future trends in export volume, prices, and revenue
3. **Comparative Analysis**: Compare trade patterns between different countries
4. **RAG-based Knowledge Base**: Query agricultural trade information using semantic search

## Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL database with trade data
- Google API key for Gemini AI

### Installation

1. Clone the repository:
```bash
git clone https://github.com/simplykevine/zeno-ai.git
cd zeno-ai
```

2. Install dependencies:
```bash
pip install -r zeno_agent/requirements.txt
pip install fastapi uvicorn
```

3. Set up environment variables:
```bash
export DATABASE_URL="postgresql://user:password@host:port/database"
export GOOGLE_API_KEY="your_google_api_key"
```

4. Run the application:
```bash
uvicorn zeno_agent.agent:app --host 0.0.0.0 --port 8080
```

### Verification

To verify the repository is accessible and functional, run:
```bash
python3 verify_repo_access.py
```

## API Endpoints

### Health Check
```
GET /healthz
```
Returns the health status of the application.

### Query
```
POST /query
```
Submit queries to the Zeno AI agent for analysis, forecasting, or comparative insights.

**Request body:**
```json
{
  "query": "What if maize prices in Kenya drop by 20%?"
}
```

## Docker Deployment

Build and run using Docker:
```bash
docker build -t zeno-ai .
docker run -p 8080:8080 \
  -e DATABASE_URL="your_database_url" \
  -e GOOGLE_API_KEY="your_api_key" \
  zeno-ai
```

## Project Structure

```
zeno-ai/
├── zeno_agent/           # Main application package
│   ├── agent.py          # FastAPI application and routing
│   ├── scenario.py       # Scenario analysis module
│   ├── forecasting.py    # Forecasting module
│   ├── comparative.py    # Comparative analysis module
│   ├── rag_tools.py      # RAG-based knowledge retrieval
│   ├── tools/            # Utility tools
│   │   ├── db.py         # Database operations
│   │   └── graphing.py   # Visualization tools
│   └── prompts/          # AI prompt templates
├── Dockerfile            # Container configuration
├── verify_repo_access.py # Repository verification script
└── README.md            # This file
```

## Development

### Running Tests
Currently, the repository focuses on functional verification. Run the verification script to ensure all components are working:
```bash
python3 verify_repo_access.py
```

## Contributing

Contributions are welcome! Please ensure your code:
- Follows the existing code style
- Includes appropriate error handling
- Documents new features in the README

## License

This project is part of the AkiraChix educational initiative.

## Contact

For questions or issues, please open an issue on GitHub.
