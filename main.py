import google.generativeai as genai
from PIL import Image
import os
import json_repair
import dotenv
from allrecipes import AllRecipes
from flask import Flask, render_template, request, redirect, url_for
from googleapiclient.discovery import build

app = Flask(__name__)
all_recipes = AllRecipes()

PROMPT = """
Analyse the image and return the following information in JSON format
{
    "title": "Name of the dish",
    "description": "Description of the dish",
    "ingredients": [
        "ingredient1",
        "ingredient2"
    ]
}"""
            

@app.route("/")
def main():
    articles = all_recipes.homepage()

    return render_template("home.html", articles=articles)

@app.route("/search")
def search():
    query = request.args.get("query").strip()
    
    # Redirect to homepage if query not found
    if not query:
        return redirect(url_for('main'))
    
    search_results = all_recipes.search(query)

    return render_template("search.html", query=query, search_results=search_results)

@app.route("/image", methods=["POST"])
def image():
    genai.configure(api_key=GEMINI_API_KEY)
    img = request.files.get('image')
    
    pil_image = Image.open(img)
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([PROMPT, pil_image])
    
    response_text = response.text
    json_repair.loads(response_text)

    return "Success", 200


@app.route("/recipe/<recipe>")
def recipe(recipe: str):
    youtube_videos = get_youtube_data(recipe + " recipe")
    return render_template("recipe.html", recipe=recipe.title(), youtube_videos=youtube_videos)


def get_youtube_data(prompt, max_results=10) -> list[str]:
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    results = []
    
    request = youtube.search().list(
        q=prompt,
        part='snippet',
        maxResults=max_results
    )

    responses = request.execute()
    
    for item in responses['items']:        
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            results.append(video_id)

    return results



if __name__ == '__main__':
    # Load environment variables from .env
    dotenv.load_dotenv()

    GEMINI_API_KEY = os.environ["GOOGLE_API_KEY"]
    YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]

    # Auto reload for changes to project
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Run on all interfaces on port 8080 in debug mode
    app.run(debug=True, host='0.0.0.0', port=8080)

