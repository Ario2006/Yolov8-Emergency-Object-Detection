# YOLOv8 Web Application

A simple web application for object detection using YOLOv8. Upload images and get predictions with bounding boxes, confidence scores, and statistics.

## Project Structure

```
yolo_web_app/
├── frontend/          # Next.js frontend
│   ├── src/
│   │   └── app/
│   │       ├── page.js
│   │       ├── layout.js
│   │       └── globals.css
│   ├── package.json
│   ├── next.config.js
│   └── tailwind.config.js
├── backend/           # Express backend
│   ├── server.js
│   ├── package.json
│   ├── uploads/       # Uploaded images (created automatically)
│   ├── outputs/       # Prediction results (created automatically)
│   └── models/        # Place your model files here
├── python/            # Python inference scripts
│   ├── inference.py
│   └── requirements.txt
└── README.md
```

## Setup and Data Download

Since the training datasets and models are large (~10GB total), they are not included in the repository. You can download them automatically using the provided script:

1. **Install requirements:**
   ```bash
   pip install -r python/requirements.txt
   ```

2. **Run the download script:**
   ```bash
   python scripts/download_assets.py
   ```

This script will automatically create the necessary folders and download:
- **Train Data** (Google Drive Folder)
- **Test Data** (Google Drive Folder)
- **best.pt** (Model file placed in `backend/models/`)

## Prerequisites

- Node.js 18+ 
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

### 1. Install Python Dependencies

```bash
cd python
pip install -r requirements.txt
```

This will install:
- ultralytics (YOLOv8)
- opencv-python
- numpy
- Pillow

### 2. Install Backend Dependencies

```bash
cd backend
npm install
```

### 3. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 4. Add Your Custom Model (Optional)

Place your trained model files in the `backend/models/` directory:
- `best.pt` (PyTorch format)
- `best.onnx` (ONNX format)

If no custom model is found, the application will use the default YOLOv8n model.

## Running the Application

### Start the Backend Server

```bash
cd backend
npm run dev
```

The backend will run on http://localhost:5000

### Start the Frontend (in a new terminal)

```bash
cd frontend
npm run dev
```

The frontend will run on http://localhost:3000

## Usage

1. Open http://localhost:3000 in your browser
2. Select a model from the dropdown (or use the default YOLOv8n)
3. Drag and drop an image or click to upload
4. Click "Run Detection"
5. View the results with bounding boxes, confidence scores, and statistics

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/models` | GET | List available models |
| `/api/predict` | POST | Upload image and run detection |

## Features

- 📤 Drag & drop image upload
- 🔍 YOLOv8 object detection
- 📊 Detection statistics (confidence, class distribution)
- 🎯 Support for custom trained models (.pt, .onnx)
- 🖼️ Annotated output images with bounding boxes
- 📱 Responsive design

## Troubleshooting

### Python not found
Make sure Python 3 is installed and accessible as `python3` in your terminal.

### Model loading issues
- Ensure ultralytics is properly installed
- Check that model files are in the correct format (.pt or .onnx)

### Port conflicts
- Backend default: 5000 (change with `PORT` environment variable)
- Frontend default: 3000 (Next.js default)

## License

MIT

---

## 🚀 Deployment Guide

This application can be deployed for free using **Vercel** (frontend) and **Render** (backend).

### Prerequisites for Deployment

1. A [GitHub](https://github.com) account
2. A [Vercel](https://vercel.com) account (free)
3. A [Render](https://render.com) account (free)

### Step 1: Push to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - YOLOv8 Web App"

# Create a new repository on GitHub and push
git remote add origin https://github.com/YOUR_USERNAME/yolo-web-app.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy Backend on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:
   - **Name:** `yolo-backend`
   - **Root Directory:** (leave blank)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r python/requirements.txt && cd backend && npm install`
   - **Start Command:** `cd backend && npm start`
5. Add Environment Variables:
   - `NODE_ENV` = `production`
   - `PORT` = `5001`
6. Choose **Free** plan and click **"Create Web Service"**
7. Wait for deployment (may take 5-10 minutes)
8. Copy your backend URL (e.g., `https://yolo-backend.onrender.com`)

### Step 3: Deploy Frontend on Vercel

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset:** Next.js
   - **Root Directory:** `frontend`
5. Add Environment Variables:
   - `NEXT_PUBLIC_API_URL` = `https://yolo-backend.onrender.com` (your Render URL)
6. Click **"Deploy"**
7. Wait for deployment (usually 1-2 minutes)

### Step 4: Test Your Deployment

1. Open your Vercel URL (e.g., `https://yolo-web-app.vercel.app`)
2. Upload an image and run detection
3. Verify everything works!

### ⚠️ Important Notes

- **Free tier limitations:** Render's free tier spins down after 15 minutes of inactivity. First request may take ~30 seconds.
- **Model files:** The default YOLOv8n model will be downloaded on first use. Custom models need to be included in the repo or downloaded during build.
- **Storage:** Uploaded images are temporary on free tier (no persistent storage).

### Troubleshooting Deployment

| Issue | Solution |
|-------|----------|
| Backend not starting | Check Render logs for Python/Node errors |
| CORS errors | Verify `NEXT_PUBLIC_API_URL` matches your Render URL |
| Slow first request | Normal for free tier - wait ~30 seconds |
| Model download fails | Check Render has enough memory (may need paid tier for large models) |
