# 🍽️ Ratatouille – A Modern Recipe Discovery Platform

**Ratatouille** is an AI powered web application that transforms how you explore recipes. It leverages web scraping and image analysis with generative AI to offer a seamless and engaging culinary experience.

<details>
  <summary><b>User Interface Preview</b></summary>
<br>

<p align="center">
<img src="https://github.com/user-attachments/assets/c469f814-162b-464e-ae67-7142ea8893ff">
<br>
<img src="https://github.com/user-attachments/assets/2ada188d-b810-45ce-b555-a541ee624c39">
<br>
<img src="https://github.com/user-attachments/assets/c9c77e9b-324b-4af5-a597-98c997510481">
</p>
</details>

## 🔗 Devpost

Explore our project on [Devpost](https://devpost.com/software/ratatouille-xtq1ir) for an in-depth look at our project's mission and impact.

## 🚀 Features

- **Dynamic Recipe Discovery:**  
  Efficiently scrapes and displays recipes from trusted sources to keep your cooking game strong.

- **Intelligent Search:**  
  Quickly find recipes with a smart search functionality based on dish names and ingredients.

- **Image Analysis:**  
  Upload or link an image, and our AI extracts key details like dish name, description, and ingredients.

- **Video Integration:**  
  Access related YouTube videos with easy integration for step-by-step cooking tutorials.

## 🔍 How It Works

### Flask Application

- **Backend Framework:**  
  Built with Python and Flask, providing robust API endpoints and dynamic web page rendering.  
  - Main entry point: [app.py](app.py)

### Recipe Scraper

- **Web Scraping:**  
  Utilizes the [`AllRecipes`](allrecipes/__init__.py) class to fetch and parse recipe details.

### Image Analyzer

- **Generative AI Integration:**  
  Processes images using Google Generative AI and extracts meaningful details for each dish.

### Video Fetching

- **YouTube Integration:**  
  Dynamically retrieves and displays related recipe videos using `yt-dlp`.


## ⚙️ Getting Started

### Prerequisites

- [Python 3](https://python.org)
- [Google Gemini API Key](https://ai.google.com)
- [FreeImage API Key](https://freeimage.host/page/api)

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/Edddro/ratatouille.git
   cd Ratatouille
   ```

2. **Set Up a Virtual Environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   - Rename `.env.example` to `.env`.
   - Fill in the required variables:
     - `FREEIMAGE_API_KEY`
     - `GOOGLE_API_KEY`

5. **Run the Application:**

   ```sh
   python app.py
   ```

   Access the app at [http://localhost:8080](http://localhost:8080).

## 📁 Project Structure

```
├── allrecipes/               # Recipe scraping utilities
│   └── __init__.py           # Contains the AllRecipes scraper class
├── app.py                    # Main Flask application logic
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── static/                   # Static assets: images, scripts (e.g., scanImage.js)
├── templates/                # Jinja2 templates for HTML pages
└── vercel.json               # Vercel deployment configuration
```

## 📞 Contact

For questions or support, please open an issue on GitHub.
