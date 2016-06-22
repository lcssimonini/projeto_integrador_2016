from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/cursos/<course_id>')
def show_course_page(course_id):
    return render_template('courses.html', course_id=course_id)

if __name__ == "__main__":
    app.run(debug=True)
