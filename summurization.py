
from openai import OpenAI
from newspaper import Article
from flask import Flask, request, render_template, redirect, url_for
import feedparser
app=Flask(__name__)



def scraping():
    feed_url = "https://www.bbc.com/news/world/rss.xml" #to feTch the article link
    feed = feedparser.parse(feed_url)
    
    all_articles=[]

    for i in feed.entries:
        url = i.link
        article = Article(url)
        article.download() 
        article.parse()

        
        all_articles.append({
            "title": article.title,
            "text": article.text
        })      
    
    return all_articles

def summarization(article_text): #summarization part
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following news article into 3 bullet points. Include all important points. Use plain text format with asterisk bullets (* point). Do not use markdown formatting like ** or bold text. Format:\n* First point\n* Second point\n* Third point\n\nArticle: {article_text}"
            }
        ],
    )
    summary = completion.choices[0].message.content
    return summary

def chat_with_article(article_text, user_question): #chat part
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
        messages=[
            {
                "role": "user",
                "content": f"Based on this news article: {article_text}\n\nAnswer this question: {user_question}"
            }
        ],
    )
    answer = completion.choices[0].message.content
    return answer

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    articles = scraping()
    return render_template("news.html", articles=articles)

from flask import request

@app.route('/chat')
def chat():
    title = request.args.get('title')
    text = request.args.get('text')
    action = request.args.get('action')
    message = request.args.get('message')
    existing_summary = request.args.get('summary')
    
    summary = existing_summary
    answer = None
    
    if action == 'summarize':
        summary = summarization(text)
    elif action == 'send' and message:
        answer = chat_with_article(text, message)
        
        if existing_summary:
            summary = existing_summary
    
    return render_template("chat.html", title=title, text=text, summary=summary, answer=answer)
    
if __name__ == '__main__':
    app.run()

