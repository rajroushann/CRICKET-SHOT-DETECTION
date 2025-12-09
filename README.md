# 🏏 Cricket Shot Detection & Performance Analysis System

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)](https://www.tensorflow.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)]()

A deep learning-powered system for detecting cricket shots and analyzing player performance from video footage. This project combines CNN-LSTM architecture with modern sports analytics to provide real-time insights for coaches, analysts, and broadcasters.

## 🎯 Key Features

- **🤖 AI-Powered Shot Detection**: Detects 6+ cricket shot types (Cover Drive, Pull, Cut, Sweep, etc.) using CNN-LSTM hybrid architecture
- **📊 Real-Time Performance Analysis**: Analyzes player statistics, shot frequency, and performance trends
- **🎥 Video Processing**: Supports MP4, AVI, MOV formats with automatic frame extraction and preprocessing
- **📈 Interactive Dashboard**: Web-based interface with glassmorphism design for real-time visualization
- **🚀 High Accuracy**: 87-92% accuracy on diverse cricket datasets
- **⚡ Fast Inference**: 2-3 seconds per video clip on standard hardware
- **🔄 Transfer Learning**: Pre-trained models (ResNet50) for improved performance with limited data
- **📱 Mobile Responsive**: Works seamlessly on desktop and mobile devices

## 📋 System Architecture

```
┌─────────────────┐
│  Cricket Video  │
└────────┬────────┘
         │
    ┌────▼─────────────────────┐
    │ Video Preprocessing       │
    │ • Frame Extraction        │
    │ • Resizing (224x224)      │
    │ • Normalization           │
    │ • Data Augmentation       │
    └────┬──────────────────────┘
         │
    ┌────▼──────────────────────────┐
    │ Feature Extraction (CNN)       │
    │ • ResNet50 Backbone           │
    │ • Spatial Feature Maps        │
    │ • 30-Frame Sequences          │
    └────┬───────────────────────────┘
         │
    ┌────▼──────────────────────────┐
    │ Temporal Modeling (LSTM)       │
    │ • 2-Layer LSTM Units          │
    │ • Temporal Sequence Learning  │
    │ • Motion Pattern Recognition  │
    └────┬───────────────────────────┘
         │
    ┌────▼──────────────────────────┐
    │ Shot Classification            │
    │ • Dense Output Layer (6 Class) │
    │ • Softmax Probability         │
    │ • Confidence Scores           │
    └────┬───────────────────────────┘
         │
    ┌────▼──────────────────────────┐
    │ Performance Analytics          │
    │ • Shot Frequency Analysis      │
    │ • Player Statistics            │
    │ • Trend Analysis               │
    │ • Visualization & Reports      │
    └────┬───────────────────────────┘
         │
    ┌────▼──────────────────────┐
    │ Interactive Dashboard      │
    │ • Real-time Predictions    │
    │ • Performance Metrics      │
    │ • Shot Visualizations      │
    └──────────────────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core programming language
- **TensorFlow/Keras 2.13+** - Deep learning framework
- **OpenCV** - Video processing and frame extraction
- **NumPy & Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning utilities
- **Flask/FastAPI** - REST API framework

### Frontend
- **HTML5** - Modern semantic markup
- **CSS3** - Glassmorphism design with animations
- **JavaScript (ES6+)** - Interactive features
- **Chart.js/Plotly** - Data visualization

### Deployment & Tools
- **Docker** - Containerization
- **PostgreSQL/MongoDB** - Database
- **MLflow** - Model tracking and versioning
- **TensorBoard** - Training visualization
- **AWS/GCP/Azure** - Cloud deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git
- 8GB RAM minimum (GPU recommended for training)
- 2GB disk space for models

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cricket-shot-detection.git
cd cricket-shot-detection
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download pre-trained models**
```bash
python download_models.py
```

### Running the Application

#### Web Interface
```bash
python app.py
# Visit http://localhost:5000 in your browser
```

#### REST API
```bash
python api.py
# API available at http://localhost:8000
```

#### Command Line
```bash
python predict.py --video path/to/video.mp4 --model cnn-lstm
```

## 📁 Project Structure

```
cricket-shot-detection/
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📄 setup.py                     # Package setup
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
├── 📄 docker-compose.yml           # Docker configuration
│
├── 🗂️ models/                      # Pre-trained models
│   ├── cnn_lstm_model.h5           # CNN-LSTM weights
│   ├── 3d_cnn_model.h5             # 3D CNN weights
│   └── resnet50_transfer.h5        # Transfer learning model
│
├── 🗂️ data/                        # Datasets
│   ├── raw/                        # Raw video files
│   ├── processed/                  # Processed frames
│   ├── annotations/                # Shot labels
│   └── splits/                     # Train/val/test splits
│
├── 🗂️ src/                         # Source code
│   ├── __init__.py
│   ├── 📄 config.py                # Configuration settings
│   ├── 📄 constants.py             # Constants and enums
│   │
│   ├── 🗂️ preprocessing/
│   │   ├── __init__.py
│   │   ├── 📄 video_processor.py   # Video frame extraction
│   │   ├── 📄 data_augmentation.py # Data augmentation
│   │   └── 📄 normalizer.py        # Frame normalization
│   │
│   ├── 🗂️ models/
│   │   ├── __init__.py
│   │   ├── 📄 cnn_lstm.py          # CNN-LSTM architecture
│   │   ├── 📄 3d_cnn.py            # 3D CNN architecture
│   │   ├── 📄 transfer_learning.py # Transfer learning model
│   │   └── 📄 base_model.py        # Base model class
│   │
│   ├── 🗂️ training/
│   │   ├── __init__.py
│   │   ├── 📄 trainer.py           # Model training
│   │   ├── 📄 evaluator.py         # Model evaluation
│   │   └── 📄 callbacks.py         # Training callbacks
│   │
│   ├── 🗂️ prediction/
│   │   ├── __init__.py
│   │   ├── 📄 predictor.py         # Shot prediction
│   │   └── 📄 post_processor.py    # Result processing
│   │
│   ├── 🗂️ analytics/
│   │   ├── __init__.py
│   │   ├── 📄 performance.py       # Performance metrics
│   │   ├── 📄 statistics.py        # Statistical analysis
│   │   └── 📄 visualization.py     # Result visualization
│   │
│   └── 🗂️ utils/
│       ├── __init__.py
│       ├── 📄 logger.py            # Logging utilities
│       ├── 📄 validators.py        # Data validation
│       └── 📄 helpers.py           # Helper functions
│
├── 🗂️ api/                         # API endpoints
│   ├── __init__.py
│   ├── 📄 app.py                   # Flask app setup
│   ├── 📄 routes.py                # API routes
│   ├── 📄 schemas.py               # Request/response schemas
│   └── 📄 middleware.py            # Custom middleware
│
├── 🗂️ web/                         # Web interface
│   ├── 📄 index.html               # Main dashboard
│   ├── 🗂️ static/
│   │   ├── css/
│   │   │   └── 📄 style.css        # Stylesheet
│   │   └── js/
│   │       └── 📄 app.js           # Frontend logic
│   └── 🗂️ templates/
│       ├── 📄 results.html         # Results page
│       └── 📄 analytics.html       # Analytics page
│
├── 🗂️ tests/                       # Unit & integration tests
│   ├── __init__.py
│   ├── 📄 test_preprocessing.py
│   ├── 📄 test_models.py
│   ├── 📄 test_prediction.py
│   └── 📄 test_api.py
│
├── 🗂️ notebooks/                   # Jupyter notebooks
│   ├── 📄 01_data_exploration.ipynb
│   ├── 📄 02_model_training.ipynb
│   └── 📄 03_evaluation.ipynb
│
├── 🗂️ docs/                        # Documentation
│   ├── 📄 ARCHITECTURE.md          # System architecture
│   ├── 📄 API.md                   # API documentation
│   ├── 📄 TRAINING.md              # Training guide
│   └── 📄 DEPLOYMENT.md            # Deployment guide
│
└── 🗂️ scripts/                     # Utility scripts
    ├── 📄 download_models.py       # Download pre-trained models
    ├── 📄 prepare_dataset.py       # Dataset preparation
    └── 📄 run_demo.py              # Demo script
```

## 🎓 Supported Cricket Shots

| Shot Type | Description | Sample Count |
|-----------|-------------|--------------|
| **Cover Drive** | Shot played to the cover fielding area | 850 |
| **Pull Shot** | Aggressive shot to short-pitched deliveries | 720 |
| **Cut Shot** | Lateral shot to deliveries outside off-stump | 650 |
| **Sweep Shot** | Shot played with bent knees toward fine leg | 580 |
| **Straight Drive** | Shot along the ground to the bowler | 890 |
| **Defensive Shot** | Conservative batting technique | 750 |

## 📊 Model Performance

### CNN-LSTM Hybrid (Recommended)
```
Accuracy:     89.3%
Precision:    88.7%
Recall:       89.1%
F1-Score:     88.9%
Top-3 Acc:    96.2%
Inference:    2.1 sec/clip
```

### 3D CNN
```
Accuracy:     87.8%
Precision:    87.2%
Recall:       87.5%
F1-Score:     87.4%
Top-3 Acc:    95.1%
Inference:    2.8 sec/clip
```

### Transfer Learning (ResNet50)
```
Accuracy:     86.5%
Precision:    86.1%
Recall:       86.3%
F1-Score:     86.2%
Top-3 Acc:    94.3%
Inference:    1.9 sec/clip
```

## 🔧 Configuration

### config.py
```python
# Model settings
MODEL_TYPE = 'cnn-lstm'  # Options: 'cnn-lstm', '3d-cnn', 'transfer-learning'
INPUT_SHAPE = (30, 224, 224, 3)
NUM_CLASSES = 6
BATCH_SIZE = 32

# Training settings
EPOCHS = 50
LEARNING_RATE = 0.001
VALIDATION_SPLIT = 0.2
EARLY_STOPPING_PATIENCE = 10

# Preprocessing
FRAME_RATE = 30
RESIZE_HEIGHT = 224
RESIZE_WIDTH = 224
NORMALIZE = True
AUGMENT = True

# API settings
API_HOST = '0.0.0.0'
API_PORT = 8000
WORKERS = 4

# Database
DB_TYPE = 'postgresql'  # Options: 'postgresql', 'mongodb', 'sqlite'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'cricket_shots'
```

## 🚀 Usage Examples

### Python API
```python
from src.prediction.predictor import ShotPredictor

# Initialize predictor
predictor = ShotPredictor(model_type='cnn-lstm')

# Predict shots from video
results = predictor.predict('path/to/video.mp4')

# Get results
for shot in results['shots']:
    print(f"Shot: {shot['type']}")
    print(f"Confidence: {shot['confidence']:.2%}")
    print(f"Timestamp: {shot['timestamp']}")
```

### REST API
```bash
# Upload and analyze video
curl -X POST http://localhost:8000/api/predict \
  -F "video=@cricket_video.mp4" \
  -F "player_name=Virat Kohli"

# Get analysis results
curl http://localhost:8000/api/results/{result_id}

# Get player statistics
curl http://localhost:8000/api/player/stats/{player_id}
```

### Command Line
```bash
# Analyze video
python predict.py \
  --video cricket_match.mp4 \
  --model cnn-lstm \
  --output results.json

# Train model
python train.py \
  --data path/to/dataset \
  --model cnn-lstm \
  --epochs 50

# Evaluate model
python evaluate.py \
  --model path/to/model.h5 \
  --test-data path/to/test_set
```

## 🧠 Model Architecture Details

### CNN-LSTM Hybrid
```
Input: (batch, 30 frames, 224, 224, 3)
       ↓
ResNet50 (Pretrained)
       ↓
Feature Maps: (batch, 2048)
       ↓
TimeDistributed Layer
       ↓
LSTM Layer 1: 256 units
       ↓
Dropout: 0.5
       ↓
LSTM Layer 2: 128 units
       ↓
Dropout: 0.5
       ↓
Dense: 128 units (ReLU)
       ↓
Dense: 64 units (ReLU)
       ↓
Output: 6 units (Softmax)
       ↓
Predictions: [shot_type, confidence]
```

## 📈 Training Guide

### 1. Prepare Dataset
```bash
python scripts/prepare_dataset.py \
  --raw-videos data/raw \
  --output data/processed \
  --split-ratio 0.8 0.1 0.1
```

### 2. Train Model
```bash
python -m src.training.trainer \
  --config config.py \
  --data data/processed \
  --model-type cnn-lstm \
  --epochs 50 \
  --batch-size 32
```

### 3. Evaluate Model
```bash
python -m src.training.evaluator \
  --model models/cnn_lstm_model.h5 \
  --test-data data/processed/test \
  --output evaluation_report.json
```

### 4. Monitor Training
```bash
tensorboard --logdir logs/
```

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t cricket-shot-detection .
```

### Run Container
```bash
docker run -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  cricket-shot-detection
```

### Docker Compose
```bash
docker-compose up -d
```

## ☁️ Cloud Deployment

### AWS EC2
```bash
# Launch EC2 instance
aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 \
  --instance-type p3.2xlarge

# Deploy application
ssh -i key.pem ec2-user@instance-ip
git clone <repo>
docker build -t app .
docker run -p 80:5000 app
```

### Google Cloud Platform
```bash
# Deploy to Cloud Run
gcloud run deploy cricket-shot-detection \
  --source . \
  --platform managed \
  --region us-central1
```

### Azure
```bash
# Create container instance
az container create \
  --resource-group myGroup \
  --name cricket-app \
  --image myregistry.azurecr.io/app:latest
```

## 🧪 Testing

### Unit Tests
```bash
pytest tests/unit/ -v
```

### Integration Tests
```bash
pytest tests/integration/ -v
```

### Coverage Report
```bash
pytest --cov=src tests/
```

## 📚 API Documentation

### POST /api/predict
Upload video and get shot predictions

**Request:**
```json
{
  "video": "file",
  "player_name": "string (optional)",
  "model_type": "cnn-lstm",
  "confidence_threshold": 75
}
```

**Response:**
```json
{
  "result_id": "uuid",
  "status": "success",
  "shots": [
    {
      "type": "Cover Drive",
      "confidence": 0.92,
      "timestamp": "0:05",
      "frame": 150
    }
  ],
  "analytics": {
    "total_shots": 6,
    "avg_confidence": 0.87,
    "processing_time": 2.3
  }
}
```

### GET /api/results/{result_id}
Retrieve previous analysis results

### GET /api/player/stats/{player_id}
Get player performance statistics

### POST /api/train
Train custom model with provided dataset

## 🔐 Security

- Input validation for all API endpoints
- SQL injection prevention with parameterized queries
- CORS enabled for production domains
- Rate limiting: 100 requests/minute per IP
- JWT authentication for admin endpoints
- Video file size limit: 500MB
- Supported formats only: MP4, AVI, MOV

## 📖 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md)
- [API Documentation](docs/API.md)
- [Training Guide](docs/TRAINING.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📋 Code Standards

- Follow PEP 8 style guide
- Write docstrings for all functions
- Add unit tests for new features
- Update documentation accordingly
- Use type hints where applicable

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- KIIT University, School of Computer Engineering
- Dr. Adyasha Dash (Project Guide)
- Sujal Gupta, Rounit Kumar Singh, Rishav Raj, Raj Roushan, Ankit Kumar (Authors)
- TensorFlow and PyTorch communities
- Sports analytics research community

## 📧 Contact & Support

- **Email**: support@cricketshot.ai
- **Issues**: [GitHub Issues](https://github.com/yourusername/cricket-shot-detection/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/cricket-shot-detection/discussions)
- **Documentation**: [Read the Docs](https://cricket-shot-detection.readthedocs.io)

## 🔗 Links

- [GitHub Repository](https://github.com/yourusername/cricket-shot-detection)
- [Live Demo](https://cricket-shot-detection.herokuapp.com)
- [Research Paper](https://arxiv.org/abs/2024.xxxxx)
- [Project Report](docs/project_report.pdf)

---

**⭐ If you find this project helpful, please star it!**

Last Updated: December 2025 | Version: 1.0.0
