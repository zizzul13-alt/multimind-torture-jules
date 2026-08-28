# MultiMind Platform Torture Test — SvelteKit + FastAPI (Candidate 3)

Isolated proof-of-concept repository evaluating SvelteKit + FastAPI as candidate presentation/backend platform for MultiMind.

## Startup & Reproduction Instructions

### 1. Backend Setup & Startup (FastAPI)
```bash
# Install backend Python dependencies
pip install -r backend/requirements.txt

# Run backend tests
PYTHONPATH=. pytest backend/test_backend.py

# Start FastAPI backend server (Port 8000)
PYTHONPATH=. python3 -m uvicorn backend.main:app --port 8000
```

### 2. Frontend Setup & Startup (SvelteKit)
```bash
cd frontend

# Install Node dependencies
npm install

# Build production SvelteKit adapter
npm run build

# Start SvelteKit dev server (Port 5173)
npm run dev -- --port 5173
```

### 3. Automated Playwright Testing
```bash
# Run full automated Playwright test suite (Desktop + Mobile 390x844)
NODE_PATH=node_modules:frontend/node_modules npx playwright test --config=tests/playwright.config.js
```

### 4. Performance Measurement & Evidence Capture
```bash
# Measure initial network transfer, JS/CSS payload, and DOM node counts
NODE_PATH=node_modules:frontend/node_modules node tests/measure_performance.js

# Capture deterministic screenshots
NODE_PATH=node_modules:frontend/node_modules node tests/capture_evidence.js
```
