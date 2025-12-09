"""
Flask web application for Cricket Shot Detection
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import uuid
from datetime import datetime
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, 
            static_folder='static',
            static_url_path='/static',
            template_folder='.')

CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB

# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Mock shot data for demo
MOCK_SHOTS = [
    {'type': 'Cover Drive', 'confidence': 0.92, 'frame': 15, 'timestamp': '0:05'},
    {'type': 'Pull Shot', 'confidence': 0.88, 'frame': 45, 'timestamp': '0:15'},
    {'type': 'Straight Drive', 'confidence': 0.85, 'frame': 75, 'timestamp': '0:25'},
    {'type': 'Cut Shot', 'confidence': 0.91, 'frame': 105, 'timestamp': '0:35'},
    {'type': 'Sweep Shot', 'confidence': 0.79, 'frame': 135, 'timestamp': '0:45'},
    {'type': 'Defensive Shot', 'confidence': 0.83, 'frame': 165, 'timestamp': '0:55'},
]

SHOT_CLASSES = {
    'Cover Drive': 'Shot played to the cover fielding area',
    'Pull Shot': 'Aggressive shot to short-pitched deliveries',
    'Cut Shot': 'Lateral shot to deliveries outside off-stump',
    'Sweep Shot': 'Shot played with bent knees toward fine leg',
    'Straight Drive': 'Shot along the ground to the bowler',
    'Defensive Shot': 'Conservative batting technique'
}


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Serve main dashboard"""
    return render_template('index.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }), 200


@app.route('/api/config', methods=['GET'])
def get_config():
    """Get system configuration"""
    return jsonify({
        'shot_classes': SHOT_CLASSES,
        'supported_formats': list(ALLOWED_EXTENSIONS),
        'max_file_size': MAX_FILE_SIZE,
        'model_types': [
            'cnn-lstm',
            '3d-cnn',
            'transfer-learning'
        ],
        'frame_rates': [5, 10, 15, 30]
    }), 200


@app.route('/api/predict', methods=['POST'])
def predict():
    """Process video and detect shots"""
    try:
        # Check if file is in request
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        file = request.files['video']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'error': f'Unsupported format. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Get parameters
        player_name = request.form.get('player_name', 'Unknown Player')
        model_type = request.form.get('model_type', 'cnn-lstm')
        confidence_threshold = float(request.form.get('confidence_threshold', 75)) / 100
        frame_rate = int(request.form.get('frame_rate', 30))
        
        # Save file
        filename = f"{uuid.uuid4()}_{file.filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Create result ID
        result_id = str(uuid.uuid4())
        
        # Mock prediction (in production, call actual ML model)
        shots = [
            {
                'type': shot['type'],
                'confidence': shot['confidence'],
                'frame': shot['frame'],
                'timestamp': shot['timestamp'],
                'description': SHOT_CLASSES.get(shot['type'], '')
            }
            for shot in MOCK_SHOTS
            if shot['confidence'] >= confidence_threshold
        ]
        
        # Calculate statistics
        total_shots = len(shots)
        avg_confidence = sum(s['confidence'] for s in shots) / total_shots if shots else 0
        
        response = {
            'result_id': result_id,
            'status': 'success',
            'player_name': player_name,
            'model_type': model_type,
            'frame_rate': frame_rate,
            'shots': shots,
            'analytics': {
                'total_shots': total_shots,
                'avg_confidence': round(avg_confidence, 3),
                'coverage': 1.0,
                'processing_time': 2.3
            },
            'metadata': {
                'filename': filename,
                'size': os.path.getsize(filepath),
                'timestamp': datetime.utcnow().isoformat()
            }
        }
        
        # Save result
        result_file = f"results/{result_id}.json"
        os.makedirs('results', exist_ok=True)
        with open(result_file, 'w') as f:
            json.dump(response, f, indent=2)
        
        logger.info(f"Prediction completed for {filename}: {total_shots} shots detected")
        
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/results/<result_id>', methods=['GET'])
def get_results(result_id):
    """Retrieve analysis results"""
    try:
        result_file = f"results/{result_id}.json"
        
        if not os.path.exists(result_file):
            return jsonify({'error': 'Result not found'}), 404
        
        with open(result_file, 'r') as f:
            results = json.load(f)
        
        return jsonify(results), 200
    
    except Exception as e:
        logger.error(f"Error retrieving results: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/player/stats/<player_name>', methods=['GET'])
def get_player_stats(player_name):
    """Get player performance statistics"""
    try:
        # This would query database in production
        stats = {
            'player_name': player_name,
            'total_analyses': 15,
            'total_shots': 89,
            'shot_distribution': {
                'Cover Drive': 28,
                'Pull Shot': 21,
                'Straight Drive': 18,
                'Cut Shot': 12,
                'Sweep Shot': 7,
                'Defensive Shot': 3
            },
            'avg_confidence': 0.88,
            'accuracy_trend': [0.85, 0.86, 0.87, 0.88, 0.88, 0.89],
            'performance_rating': 4.2
        }
        
        return jsonify(stats), 200
    
    except Exception as e:
        logger.error(f"Error getting player stats: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available models"""
    models = [
        {
            'id': 'cnn-lstm',
            'name': 'CNN-LSTM Hybrid',
            'accuracy': '89.3%',
            'inference_time': '2.1s',
            'description': 'Hybrid architecture combining CNN and LSTM for shot detection'
        },
        {
            'id': '3d-cnn',
            'name': '3D CNN',
            'accuracy': '87.8%',
            'inference_time': '2.8s',
            'description': '3-dimensional convolution for spatio-temporal feature extraction'
        },
        {
            'id': 'transfer-learning',
            'name': 'Transfer Learning (ResNet50)',
            'accuracy': '86.5%',
            'inference_time': '1.9s',
            'description': 'Pre-trained ResNet50 fine-tuned for cricket shot classification'
        }
    ]
    
    return jsonify(models), 200


@app.route('/api/system/info', methods=['GET'])
def system_info():
    """Get system information"""
    import platform
    import psutil
    
    try:
        info = {
            'system': {
                'platform': platform.platform(),
                'processor': platform.processor(),
                'python_version': platform.python_version()
            },
            'resources': {
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_percent': psutil.disk_usage('/').percent
            },
            'app': {
                'version': '1.0.0',
                'environment': os.getenv('ENVIRONMENT', 'development'),
                'debug': app.debug
            }
        }
        
        return jsonify(info), 200
    
    except Exception as e:
        logger.error(f"Error getting system info: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({
        'error': f'File too large. Maximum size: {MAX_FILE_SIZE / (1024*1024):.0f}MB'
    }), 413


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Resource not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


@app.before_request
def before_request():
    """Log incoming requests"""
    logger.info(f"{request.method} {request.path}")


@app.after_request
def after_request(response):
    """Add security headers"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == '__main__':
    # Development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
