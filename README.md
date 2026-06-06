# NewsBrief AI

**AI-powered news article summarization platform that extracts content from URLs and generates concise summaries using transformer-based NLP models.**

---

## Overview

NewsBrief AI is an end-to-end NLP application designed to help users quickly understand lengthy news articles.

Users simply paste a news article URL into the application, and the system automatically:

* Extracts the article content,
* Validates the extracted text,z
* Generates a concise AI-powered summary,
* Displays the summary through an intuitive web interface.

The project combines modern Natural Language Processing techniques with production-oriented software engineering practices to create a deployable AI product.

---

## Problem Statement

Readers are exposed to an overwhelming amount of information every day, making it difficult to consume news efficiently.

While many summarization models exist, building a reliable real-world application requires more than simply loading a transformer model. Challenges such as article extraction, validation, inference, and frontend-backend integration must also be addressed.

NewsBrief AI aims to solve this problem by providing a streamlined summarization experience directly from article URLs.

---

## Features

* Paste news article URLs directly into the application.
* Automatic article extraction using multiple extraction strategies.
* Validation layer to reject incomplete extractions.
* Transformer-based summarization using DistilBART.
* FastAPI backend with interactive Swagger documentation.
* Lightweight frontend built with HTML, CSS, and JavaScript.
* Copy generated summaries with a single click.

---

## System Architecture

User URL
│
▼
FastAPI Endpoint
│
▼
Pipeline Service
│
▼
Article Extraction Layer
(Trafilatura + Newspaper3k)
│
▼
Validation Layer
│
▼
DistilBART Summarizer
│
▼
JSON Response
│
▼
Frontend Interface

---

## Technologies Used

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Natural Language Processing

* Hugging Face Transformers
* DistilBART (`sshleifer/distilbart-cnn-12-6`)
* PyTorch

### Article Extraction

* Trafilatura
* Newspaper3k

### Frontend

* HTML
* CSS
* JavaScript

### Development Environment

* Ubuntu
* VS Code
* Git

---

## Technical Challenges and Solutions

### Challenge: Incomplete Article Extraction

Some news websites returned only partial article content.

**Solution:**

Implemented a validation layer and fallback extraction mechanism to improve reliability.

---

### Challenge: Website Scraping Restrictions

Certain websites blocked automated extraction attempts.

**Solution:**

Introduced multiple extraction strategies to maximize compatibility.

---

### Challenge: Transformer Pipeline Compatibility

The installed Transformers version did not expose a summarization pipeline.

**Solution:**

Implemented summarization using `AutoTokenizer`, `AutoModelForSeq2SeqLM`, and manual generation logic.

---

## Example Workflow

1. User pastes a news article URL.
2. The backend extracts the article text.
3. The extracted content is validated.
4. DistilBART generates a summary.
5. The frontend displays the result.

---

## Run Locally

Clone the repository:

```bash
git clone <repository-url>

cd newsbrief-ai
```

Create and activate a virtual environment:

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn backend.main:app --reload
```

Start the frontend:

```bash
cd frontend

python3 -m http.server 5500
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

Frontend:

```
http://127.0.0.1:5500
```

---

## Skills Demonstrated

* Natural Language Processing
* Transformer-based Inference
* Sequence-to-Sequence Models
* FastAPI Development
* REST API Design
* Frontend-Backend Integration
* Error Handling
* Software Architecture
* Git Version Control
* Product-Oriented Machine Learning Development

---

## Future Improvements

* Azure deployment
* User authentication
* Summary history
* Multi-language summarization
* Browser-based extraction fallback using Playwright
* Fine-tuning on domain-specific summarization datasets

---

## Author

**Muhammad Jarrar Shaf**
