# 📰 AI-powered Journalism  

![Banner](https://via.placeholder.com/1000x200.png?text=AI+Powered+Journalism)  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)  
[![RSS](https://img.shields.io/badge/RSS-Feed-orange)](https://en.wikipedia.org/wiki/RSS)  
[![feedparser](https://img.shields.io/badge/feedparser-latest-brightgreen)](https://pythonhosted.org/feedparser/)  
[![newspaper3k](https://img.shields.io/badge/newspaper3k-article%20scraping-yellow)](https://newspaper.readthedocs.io/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Chat with LLaMA](https://img.shields.io/badge/LLaMA3-Chat-blueviolet)](https://huggingface.co/meta-llama)  
[![Status](https://img.shields.io/badge/Status-Prototype-blue)]()  

---

⭐ **Star this repo** — your support helps improve it!  

---

## 🔥 Overview

**AI-powered Journalism** is a Flask-based web app that:  
- Scrapes [BBC World RSS](https://www.bbc.com/news/world/rss.xml).  
- Extracts and cleans full-text articles with [newspaper3k](https://newspaper.readthedocs.io/).  
- Summarizes them into concise bullet points with [LLaMA 3](https://huggingface.co/meta-llama).  
- Lets you chat with articles directly via natural language questions.  

---

## ⚙️ Project Structure  

```bash
AI-powered-journalism/
├── app.py              # Flask app with scraping, summarization, chat
├── templates/          # HTML templates
│   ├── news.html       # Article listing
│   └── chat.html       # Chat + summary interface
├── static/             # (Optional) CSS, JS, images
```

Here’s a **preview** of the README rewritten with all your requirements added in. I’ve kept it professional, concise, and aimed at developers with solid experience.

---

# AI-powered Journalism

AI-powered Journalism is a prototype web application that combines automated article scraping, summarization, and conversational Q&A. It fetches articles from an [RSS feed](https://en.wikipedia.org/wiki/RSS), parses them into structured text, and enables interaction through summarization and question answering powered by LLaMA 3. The application is built with [Flask](https://flask.palletsprojects.com/) and uses HTML templates for rendering content.

---

## Techniques

* **RSS Feed Parsing**: Uses [feedparser](https://pythonhosted.org/feedparser/) to process RSS XML and extract article metadata.
* **Article Extraction**: Leverages [newspaper3k](https://newspaper.readthedocs.io/en/latest/) for structured downloading and parsing of article text.
* **Templating**: Applies [Jinja2](https://jinja.palletsprojects.com/) to render server-side templates dynamically with variables passed from Flask routes.
* **Form Handling with Query Parameters**: Uses `<form>` with [hidden inputs](https://developer.mozilla.org/docs/Web/HTML/Element/input/hidden) and query strings to maintain state across requests without sessions.
* **Summarization via API**: Connects to [Hugging Face Inference API](https://huggingface.co/inference-api) through the [OpenAI Python client](https://github.com/openai/openai-python) for structured, bullet-point summaries.
* **Conversational Prompting**: Article text is injected directly into prompts, enabling targeted Q&A.
* **CSS UI Styling**: The frontend includes [box-shadow](https://developer.mozilla.org/docs/Web/CSS/box-shadow), [border-radius](https://developer.mozilla.org/docs/Web/CSS/border-radius), and hover effects for card layouts.

---

## Libraries and Services

* [Flask](https://flask.palletsprojects.com/) – lightweight backend framework
* [feedparser](https://pythonhosted.org/feedparser/) – RSS/Atom parsing
* [newspaper3k](https://newspaper.readthedocs.io/en/latest/) – content extraction
* [OpenAI Python Client](https://github.com/openai/openai-python) – API client adapted for Hugging Face endpoints
* [Hugging Face Inference API](https://huggingface.co/inference-api) – LLaMA-based summarization and chat
* [Jinja2](https://jinja.palletsprojects.com/) – server-side templating

---

## Project Structure

```bash
AI-powered-journalism/
├── app.py              # Flask application logic: scraping, summarization, chat
├── templates/          # Jinja2 HTML templates
│   ├── news.html       # Displays articles list with links to chat
│   └── chat.html       # Summarization + conversational UI
├── static/             # Placeholder for CSS, JS, and images
```

* **`templates/`**: Holds server-rendered HTML files.
* **`static/`**: Intended for custom stylesheets, JavaScript, or assets like logos and images.

---

## Notes

* Prototype release. Focused on scraping, summarization, and conversational Q&A workflows.
* Flexible enough to be extended with authentication, multiple news sources, or richer front-end interactions.

---


