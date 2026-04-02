from flask import Flask, render_template, request, jsonify
from Chatbot_United import chatbot_united

app = Flask(__name__)

@app.route('/')
def home():\
    return render_template('home.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/ucl_learnings')
def ucl_learnings():
    return render_template('news_articles/ucl_learnings.html')

@app.route('/europa_article')
def europa_article():
    return render_template('news_articles/europa_article.html')

@app.route('/key_questions')
def key_questions():
    return render_template('news_articles/key_questions.html')

@app.route('/match_officials')
def match_officials():
    return render_template('news_articles/match_officials.html')

@app.route('/hivis_ball')
def hivis_ball():
    return render_template('news_articles/hivis_ball.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = chatbot_united.main(user_message)
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True)