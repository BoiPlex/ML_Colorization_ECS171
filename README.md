# Image Colorization - ML Project

## Project Structure

```
├── training/              # Model training code
│   ├── model.py          # Model architecture: Link to colab notebook or something
│
└── web_app/              # Web application
    ├── backend/          # Flask API
    │   ├── app.py        # API endpoints
    │   └── requirements.txt
    └── frontend/         # Web UI
```

## Architecture

**Training** (`/training`):
- Develop and train the colorization model
- Save trained model to Hugging Face Hub

**Backend** (`/web_app/backend`):
- Flask API that loads model from Hugging Face
- `/predict` endpoint: accepts image → returns colorized image
- Model loaded once on startup, persists in memory

**Frontend** (`/web_app/frontend`):
- Web UI for uploading grayscale images
- Calls backend `/predict` endpoint
- Displays colorized results

## Key Design Notes

- **Single Git Repo**: Training code and web app are in the same repository
- **Model Storage**: Trained model is uploaded to Hugging Face Model Hub
- **No Retraining**: Backend downloads model once and keeps it in memory
- **Scalable**: Model persists across requests, no redundant loading
