# 🎓 AI Learning Roadmap Generator

An AI-powered Streamlit application that generates personalized learning roadmaps based on a user's domain, skill level, and available learning time.

## Features

- Personalized learning roadmaps
- Beginner, Intermediate, and Advanced skill levels
- Multiple learning-duration options
- Learning goals
- Prerequisites
- Chronological learning plans
- Practical exercises
- Recommended tools and technologies
- Project suggestions
- Final project
- Expected skills
- Markdown-formatted AI output

## Technologies

- Python
- Streamlit
- Groq API
- `openai/gpt-oss-120b`

## Project Structure

```text
AI-Learning-Roadmap-Generator/
├── app.py
├── requirements.txt
└── README.md
```

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

## API Key

This application reads the Groq API key from the `GROQ_API_KEY` environment variable.

For Google Colab, store your key in Colab Secrets with the name:

```text
GROQ_API_KEY
```

Then run the following in a Colab cell before starting Streamlit:

```python
from google.colab import userdata
import os

GROQ_API_KEY = userdata.get("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
```

Do not put your actual API key in `app.py` or commit it to GitHub.

## Run the Application

Run:

```bash
streamlit run app.py
```

The application normally runs at:

```text
http://localhost:8501
```

## Running in Google Colab

Start Streamlit with:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

For temporary public access during Colab development, Cloudflare Quick Tunnel can expose the local Streamlit server:

```bash
cloudflared tunnel --url http://127.0.0.1:8501
```

Cloudflare will provide a temporary `trycloudflare.com` URL.

## How It Works

```text
User
  ↓
Streamlit Interface
  ↓
Domain + Skill Level + Learning Time
  ↓
Python Roadmap Function
  ↓
Prompt Construction
  ↓
Groq API
  ↓
openai/gpt-oss-120b
  ↓
Generated Roadmap
  ↓
Streamlit Output
```

## Example Input

```text
Domain: Machine Learning
Skill Level: Beginner
Available Learning Time: 2 Months
```

The model generates a structured roadmap containing learning goals, prerequisites, topics, weekly planning, exercises, tools, projects, a final project, and expected skills.

## Future Improvements

- Hours available per day
- Learning goals
- Preferred learning style
- Recommended learning resources
- Progress tracking
- Weekly milestones
- Roadmap history
- Downloadable roadmaps
- Interactive quizzes
- AI-generated practice questions
- Personalized roadmap updates

## License

This project is intended for educational and learning purposes.
