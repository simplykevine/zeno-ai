# Zeno AI Repository - Detailed File Structure

## Overview
Zeno AI is an AI-powered Economist Assistant for East African agricultural trade analysis. The system provides scenario analysis, forecasting, comparative analysis, and knowledge base queries using advanced machine learning models and a RAG (Retrieval-Augmented Generation) system.

## Repository Statistics
- **Total Files**: 27 files
- **Python Modules**: 14 files
- **Configuration Files**: 4 files
- **Prompt Templates**: 7 files
- **Total Lines of Code**: ~1,955 lines

---

## Directory Structure

```
zeno-ai/
├── .git/                           # Git version control directory
├── .github/                        # GitHub configuration
│   └── pull_request_template.md   # PR template (45 lines)
├── .gitignore                      # Git ignore patterns (582 bytes)
├── Dockerfile                      # Container configuration (13 lines)
├── Procfile                        # Deployment configuration (1 line)
├── README.md                       # Project documentation (1 line)
└── zeno_agent/                     # Main application package
    ├── __init__.py                 # Package initializer (0 lines)
    ├── agent.py                    # Main agent orchestrator (452 lines)
    ├── comparative.py              # Comparative analysis module (104 lines)
    ├── db_utils.py                 # Database utilities (182 lines)
    ├── embedding_utils.py          # Text embedding utilities (41 lines)
    ├── forecasting.py              # Forecasting agent (325 lines)
    ├── log_utils.py                # Logging utilities (49 lines)
    ├── rag_tools.py                # RAG knowledge base tools (20 lines)
    ├── requirements.txt            # Python dependencies (116 lines)
    ├── root_agent.py               # Root agent entry point (0 lines)
    ├── root_agent.yaml             # Agent configuration (2 lines)
    ├── scenario.py                 # Scenario analysis module (215 lines)
    ├── prompts/                    # Prompt templates directory
    │   ├── missing_data.txt        # Missing data prompt (2 lines)
    │   ├── root_agent.txt          # Root agent prompt (13 lines)
    │   ├── router_prompt.txt       # Query routing prompt (28 lines)
    │   ├── scenario_examples.txt   # Scenario examples (9 lines)
    │   ├── scenario_subagent.txt   # Scenario subagent prompt (9 lines)
    │   ├── scenario_template.txt   # Scenario output template (22 lines)
    │   └── scenario_what_if_prompt.txt  # What-if analysis prompt (9 lines)
    ├── scenario_graphs/            # Generated visualization output
    │   └── maize_kenya_scenario_drop20.png  # Example scenario graph (PNG)
    └── tools/                      # Utility tools package
        ├── __init__.py             # Tools package initializer (1 line)
        ├── db.py                   # Database operations (217 lines)
        ├── graphing.py             # Chart generation (42 lines)
        └── query.py                # Query utilities (38 lines)
```

---

## File Descriptions

### Root Level Files

#### Configuration Files

**Dockerfile** (13 lines)
- Base image: `python:3.11-slim`
- Working directory: `/app`
- Installs dependencies from `zeno_agent/requirements.txt`
- Installs FastAPI and Uvicorn
- Exposes port 8080
- Runs the FastAPI application via Uvicorn

**Procfile** (1 line)
- Deployment configuration for cloud platforms (e.g., Heroku)
- Starts web server: `uvicorn web_api:app --host=0.0.0.0 --port=${PORT:-8080}`

**.gitignore** (582 bytes)
- Excludes Python cache files (`__pycache__`, `*.pyc`)
- Excludes environment files and build artifacts
- Excludes IDE configuration files

**README.md** (1 line)
- Currently minimal, needs expansion

---

### Main Application Package (`zeno_agent/`)

#### Core Agent Modules

**agent.py** (452 lines) - *Main Agent Orchestrator*
- **Purpose**: Central orchestration layer for routing and handling user queries
- **Key Components**:
  - `SUPPORTED_COUNTRIES`: Kenya, Rwanda, Tanzania, Uganda, Ethiopia
  - `SUPPORTED_COMMODITIES`: Maize, Coffee, Tea
  - `is_in_scope()`: Validates if query is within supported scope
  - `parse_query()`: Extracts entities from user queries
  - `route_query()`: Routes queries to appropriate sub-agents
  - FastAPI endpoints: `/query`, `/healthz`
  - CLI interface via `run_cli()` and `main()`
- **Dependencies**: FastAPI, Google Generative AI, database tools, sub-agents
- **API Endpoints**:
  - `POST /query`: Main query endpoint (returns JSON with analysis and optional graph)
  - `GET /healthz`: Health check endpoint

**forecasting.py** (325 lines) - *Forecasting Sub-Agent*
- **Purpose**: Time series forecasting for agricultural trade metrics
- **Key Components**:
  - `ForecastingAgent` class
  - `parse_timeframe()`: Converts natural language timeframes to periods
  - `preprocess_data()`: Data cleaning and feature engineering
  - `select_model()`: Chooses best forecasting model
  - Model implementations:
    - `run_prophet()`: Facebook Prophet model
    - `run_arima()`: ARIMA statistical model
    - `run_xgboost()`: XGBoost regression model
    - `run_ensemble()`: Combined model approach
  - `calculate_confidence()`: Confidence interval analysis
  - `adjust_forecast_with_rag()`: RAG-enhanced forecast adjustment
- **Supported Metrics**: price, export_volume, revenue
- **Models**: Prophet, ARIMA, XGBoost, Ensemble

**scenario.py** (215 lines) - *Scenario Analysis Sub-Agent*
- **Purpose**: What-if analysis and shock simulation for commodities
- **Key Components**:
  - `ScenarioSubAgent` class
  - `handle()`: Main scenario processing method
  - Shock simulation (price increase/decrease by percentage)
  - Visualization generation
  - Integration with RAG for context-aware explanations
- **Features**:
  - Simulates price shocks (e.g., "What if maize price drops by 20%?")
  - Projects future prices over specified timeframes
  - Generates comparison graphs (baseline vs. scenario)

**comparative.py** (104 lines) - *Comparative Analysis Module*
- **Purpose**: Cross-country and cross-commodity comparisons
- **Key Features**:
  - Compare metrics across countries
  - Compare commodities within a country
  - Time-based trend comparisons
  - Statistical analysis and insights

**rag_tools.py** (20 lines) - *RAG Knowledge Base Interface*
- **Purpose**: Interface to knowledge base for contextual information
- **Key Function**: `ask_knowledgebase()`
- Retrieves relevant documents using semantic search
- Enhances responses with expert knowledge

#### Utility Modules

**db_utils.py** (182 lines) - *Database Utilities*
- **Purpose**: High-level database operations and data retrieval
- **Key Functions**:
  - `get_country_id_by_name()`: Country lookup
  - `get_crop_id_by_name()`: Crop/commodity lookup
  - `get_indicator_id_by_metric()`: Metric identifier lookup
  - `get_trade_data_from_db()`: Historical trade data retrieval
  - `query_rag_embeddings_semantic()`: Semantic search on knowledge base
- **Database Schema**: Uses PostgreSQL with vector embeddings (pgvector)

**embedding_utils.py** (41 lines) - *Text Embedding Utilities*
- **Purpose**: Generate text embeddings for semantic search
- **Key Function**: `encode_query_to_vector()`
- Uses Google Generative AI for embeddings
- Supports vector similarity search

**log_utils.py** (49 lines) - *Logging Utilities*
- **Purpose**: Structured logging for debugging and monitoring
- **Key Function**: `log_step()`
- Provides step-by-step execution tracking
- Helpful for debugging multi-step agent workflows

**requirements.txt** (116 lines)
- **Core Dependencies**:
  - `fastapi==0.116.2`: Web framework
  - `uvicorn==0.36.0`: ASGI server
  - `google-genai==1.39.1`: Google Generative AI
  - `google-generativeai>=0.8.5`: Google AI embeddings
  - `prophet==1.1.7`: Time series forecasting
  - `xgboost==3.0.5`: Gradient boosting
  - `statsmodels==0.14.5`: Statistical modeling
  - `pandas==2.3.2`: Data manipulation
  - `numpy==2.3.3`: Numerical computing
  - `matplotlib==3.10.6`: Plotting
  - `psycopg2-binary==2.9.10`: PostgreSQL adapter
  - `SQLAlchemy==2.0.43`: SQL toolkit
  - `scikit-learn==1.7.2`: Machine learning utilities

**root_agent.py** (0 lines)
- Placeholder file for potential root agent implementation

**root_agent.yaml** (2 lines)
- Agent configuration file (minimal)

---

### Tools Package (`zeno_agent/tools/`)

**db.py** (217 lines) - *Database Operations*
- **Purpose**: Low-level database operations and connections
- **Key Functions**:
  - `get_text_embedding()`: Generate embeddings using Gemini API
  - `embed_text()`: Text to vector conversion
  - `get_trade_data()`: Fetch historical trade data with metadata
  - `query_embeddings()`: Vector similarity search using pgvector
  - `semantic_search_rag_embeddings()`: RAG document retrieval
- **Database Connection**: PostgreSQL via SQLAlchemy and psycopg2
- **Features**: 
  - Handles trade data with metadata (source, updated_at, notes)
  - Supports vector similarity search with pgvector extension
  - Returns last N months of historical data

**graphing.py** (42 lines) - *Visualization Generation*
- **Purpose**: Generate charts and graphs for analysis results
- **Key Function**: `plot_price_scenario()`
- Creates matplotlib-based visualizations
- Outputs PNG files to `scenario_graphs/` directory
- Compares baseline vs. scenario projections

**query.py** (38 lines) - *Query Processing Utilities*
- **Purpose**: Helper functions for query parsing and processing
- Supports natural language query understanding

**__init__.py** (1 line)
- Exports key functions: `get_trade_data`, `semantic_search_rag_embeddings`

---

### Prompts Directory (`zeno_agent/prompts/`)

This directory contains text templates for various agent interactions:

**router_prompt.txt** (28 lines)
- Classifies user queries into types: scenario, forecast, comparative, rag
- Extracts parameters: commodity, country, metric, percentage, direction, timeframe
- Returns JSON-formatted query metadata

**scenario_template.txt** (22 lines)
- Template for scenario analysis output
- Structures the response with:
  - Step 1: Historical data retrieval
  - Step 2: Shock application
  - Step 3: Visualization
  - Step 4: Result interpretation

**scenario_what_if_prompt.txt** (9 lines)
- Guides the what-if scenario analysis format
- Helps structure hypothetical questions

**scenario_subagent.txt** (9 lines)
- Instructions for the scenario sub-agent
- Defines behavior and response format

**scenario_examples.txt** (9 lines)
- Example queries for scenario analysis
- Helps users understand capabilities

**root_agent.txt** (13 lines)
- Root-level agent instructions
- Top-level orchestration guidance

**missing_data.txt** (2 lines)
- Error message template when data is unavailable

---

### Output Directory (`zeno_agent/scenario_graphs/`)

**maize_kenya_scenario_drop20.png**
- Example output: PNG visualization (800x500px)
- Shows scenario analysis results
- Compares baseline vs. projected trends

---

## Architecture Overview

### Agent Hierarchy
1. **Main Agent** (`agent.py`)
   - Routes queries to appropriate sub-agents
   - Handles API endpoints
   - Manages CLI interface

2. **Sub-Agents**:
   - **ForecastingAgent**: Time series predictions
   - **ScenarioSubAgent**: What-if analysis
   - **Comparative Module**: Cross-sectional comparisons
   - **RAG Tools**: Knowledge base queries

### Data Flow
1. User query → `agent.py` (routing)
2. Query classification and parameter extraction
3. Sub-agent execution (forecast/scenario/comparative/rag)
4. Database retrieval via `db.py` and `db_utils.py`
5. RAG enhancement via `rag_tools.py` and embeddings
6. Response generation with Google Generative AI
7. Optional visualization via `graphing.py`
8. Return JSON response with analysis and graph path

### Database Schema
- **trade_data**: Historical commodity trade data
- **trade_data_metadata**: Source and update information
- **rag_embeddings**: Vector embeddings for semantic search (pgvector)
- Supports countries: Kenya, Rwanda, Tanzania, Uganda, Ethiopia
- Supports commodities: Maize, Coffee, Tea

### Technologies
- **Backend**: Python 3.11, FastAPI, Uvicorn
- **AI/ML**: Google Generative AI (Gemini), Prophet, ARIMA, XGBoost
- **Database**: PostgreSQL with pgvector extension
- **Data Science**: pandas, numpy, scikit-learn, statsmodels
- **Visualization**: matplotlib
- **Deployment**: Docker, cloud-ready (Procfile)

---

## Key Features

1. **Multi-Model Forecasting**
   - Prophet for seasonal patterns
   - ARIMA for statistical time series
   - XGBoost for non-linear patterns
   - Ensemble methods for robust predictions

2. **Scenario Analysis**
   - Price shock simulation
   - Policy impact assessment
   - Natural event modeling (droughts, etc.)

3. **RAG-Enhanced Insights**
   - Semantic search on knowledge base
   - Context-aware explanations
   - Document-grounded responses

4. **Comparative Analysis**
   - Cross-country comparisons
   - Multi-commodity analysis
   - Temporal trend analysis

5. **RESTful API**
   - FastAPI with automatic documentation
   - JSON responses
   - Health check endpoint
   - Docker-ready deployment

---

## Environment Variables Required

- `GOOGLE_API_KEY`: Google Generative AI API key (required)
- `DATABASE_URL`: PostgreSQL connection string (required)
- `PORT`: Server port (default: 8080)

---

## API Usage

### Query Endpoint
```http
POST /query
Content-Type: application/json

{
  "query": "What if maize price drops by 20% in Kenya?"
}
```

**Response**:
```json
{
  "response": "Analysis text...",
  "graph_path": "scenario_graphs/maize_kenya_scenario_drop20.png",
  "followup": "Want to run another scenario?"
}
```

### Health Check
```http
GET /healthz
```

**Response**:
```json
{
  "status": "ok"
}
```

---

## Deployment

### Docker
```bash
docker build -t zeno-ai .
docker run -p 8080:8080 \
  -e GOOGLE_API_KEY=your_key \
  -e DATABASE_URL=postgresql://... \
  zeno-ai
```

### Cloud Platform (Heroku, etc.)
- Uses `Procfile` for automatic deployment
- Requires environment variables to be set
- Automatically scales with cloud platform features

---

## Development Workflow

1. **Installation**:
   ```bash
   pip install -r zeno_agent/requirements.txt
   ```

2. **Running Locally**:
   ```bash
   uvicorn zeno_agent.agent:app --host 0.0.0.0 --port 8080
   ```

3. **CLI Mode**:
   ```bash
   python -m zeno_agent.agent
   ```

---

## Future Enhancements

Based on the structure, potential areas for expansion:
- Expand `README.md` with comprehensive documentation
- Add unit tests (no test directory currently exists)
- Implement `root_agent.py` functionality
- Add more commodity types beyond maize, coffee, tea
- Expand country coverage
- Add authentication/authorization
- Implement caching for faster responses
- Add CI/CD pipeline configuration

---

## Summary

This repository is a well-structured AI-powered economic analysis system for East African agricultural trade. It combines modern ML techniques (Prophet, ARIMA, XGBoost) with advanced AI capabilities (Google Generative AI, RAG) to provide actionable insights for stakeholders in the agricultural trade sector.

The modular architecture separates concerns clearly:
- Agent orchestration
- Database operations
- Machine learning models
- Visualization
- Prompt engineering

This makes the codebase maintainable and extensible for future enhancements.
