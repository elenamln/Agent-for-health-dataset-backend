# Asthma Agentic Backend

This backend service provides an API for question answering on asthma-related data via Google’s Gemini generative AI model. It uses FastAPI to expose a `/ask` endpoint where users can upload CSV data and submit questions for AI-powered answers.

---

## Features

- Upload CSV datasets containing asthma data
- Ask natural language questions about the data
- Receive AI-generated responses based on the content
- CORS enabled for integration with frontend applications (e.g., Flutter app)

---

## Setup & Installation

### Prerequisites

- Python 3.9 or newer
- Google API key with access to Gemini API
- `pip` package manager

### Steps

1. Clone the backend repository or navigate to the backend folder

   ```bash
   git clone https://github.com/elenamln/asthma-agentic.git
   cd asthma-agentic/backend
