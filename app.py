from flask import Flask, render_template, request
from models import Comment

comments = []
initial_comments = [
    Comment("First comment", "positive"),
    Comment("This platform is trash", "negative"),
    Comment("Wow! Amazing", "positive"),
]

comments.extend(initial_comments)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    comments_per_page = 4
    start_index = (page - 1) * comments_per_page
    end_index = start_index + comments_per_page
    if request.method == 'POST':
        text = request.form['comment_text']
        category = request.form['comment_category']

        new_comment = Comment(text, category)
        comments.insert(0, new_comment)
    page_comments = comments[start_index:end_index]
    return render_template('page.html', comments=page_comments, page = page)


if __name__ == '__main__':
    app.run(debug=True)
