from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, )

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/recipe/<recipe>")
def recipe(recipe: str):
    return render_template("recipe.html", recipe=recipe.title())

@app.route("/search")
def search():
    query = request.args.get("query").strip()
    
    # Redirect to homepage if query not found
    if not query:
        return redirect(url_for('main'))

    return render_template("search.html")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=8080)