from flask import Flask, jsonify, request, render_template, redirect, url_for

from bot import chatbot_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dep')
def dep():
    return render_template('dep.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/singleblog')
def singleblog():
    return render_template('single-blog.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')




@app.route('/chat-api', methods=['POST'])
def get_bot_response():
    print(request.json)
    question = request.json.get('question')
    print(f'QUESTION: {question}')
    answer = chatbot_response(question)
    print(f'ANSWER: {answer}')

    return jsonify({
        'question': question,
        'answer': answer
    })


@app.route('/chat', methods=['GET', 'POST'])
def get_chatbot_response():
    # if request.method == 'POST':
    #     req = request.form
    #     question = req.get('question')
    #     print(question)
    #     answer = chatbot_response(question)
    #     print(answer)
    #     return render_template('chat.html', answer=answer)
    return render_template('chat.html')

@app.route('/get')
def get():
    msg = request.args.get("msg")   
    answer = chatbot_response(msg)
    return answer

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
