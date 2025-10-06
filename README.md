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
