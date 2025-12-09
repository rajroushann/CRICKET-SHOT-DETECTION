"""
Configuration settings for Cricket Shot Detection System
"""

import os
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class ModelConfig:
    """Model configuration"""
    MODEL_TYPE: str = 'cnn-lstm'  # Options: 'cnn-lstm', '3d-cnn', 'transfer-learning'
    INPUT_SHAPE: tuple = (30, 224, 224, 3)  # (frames, height, width, channels)
    NUM_CLASSES: int = 6
    BATCH_SIZE: int = 32
    DROPOUT_RATE: float = 0.5
    LEARNING_RATE: float = 0.001
    OPTIMIZER: str = 'adam'
    LOSS_FUNCTION: str = 'categorical_crossentropy'


@dataclass
class TrainingConfig:
    """Training configuration"""
    EPOCHS: int = 50
    EARLY_STOPPING_PATIENCE: int = 10
    VALIDATION_SPLIT: float = 0.2
    RANDOM_SEED: int = 42
    USE_CHECKPOINT: bool = True
    CHECKPOINT_DIR: str = 'checkpoints/'
    LOG_DIR: str = 'logs/'


@dataclass
class PreprocessingConfig:
    """Data preprocessing configuration"""
    FRAME_RATE: int = 30
    RESIZE_HEIGHT: int = 224
    RESIZE_WIDTH: int = 224
    NORMALIZE: bool = True
    AUGMENT: bool = True
    AUGMENTATION_TECHNIQUES: List[str] = None
    
    def __post_init__(self):
        if self.AUGMENTATION_TECHNIQUES is None:
            self.AUGMENTATION_TECHNIQUES = [
                'rotation',
                'horizontal_flip',
                'brightness',
                'contrast'
            ]


@dataclass
class DataConfig:
    """Data configuration"""
    DATA_DIR: str = 'data/'
    RAW_DATA_DIR: str = 'data/raw/'
    PROCESSED_DATA_DIR: str = 'data/processed/'
    ANNOTATIONS_DIR: str = 'data/annotations/'
    TRAIN_SPLIT: float = 0.8
    VAL_SPLIT: float = 0.1
    TEST_SPLIT: float = 0.1
    MAX_VIDEO_SIZE: int = 500 * 1024 * 1024  # 500MB
    SUPPORTED_FORMATS: List[str] = None
    
    def __post_init__(self):
        if self.SUPPORTED_FORMATS is None:
            self.SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv']


@dataclass
class APIConfig:
    """API configuration"""
    API_HOST: str = '0.0.0.0'
    API_PORT: int = 8000
    WORKERS: int = 4
    DEBUG: bool = False
    ENABLE_CORS: bool = True
    CORS_ORIGINS: List[str] = None
    RATE_LIMIT: int = 100  # requests per minute
    MAX_UPLOAD_SIZE: int = 500 * 1024 * 1024  # 500MB
    
    def __post_init__(self):
        if self.CORS_ORIGINS is None:
            self.CORS_ORIGINS = ['*']


@dataclass
class DatabaseConfig:
    """Database configuration"""
    DB_TYPE: str = 'postgresql'  # Options: 'postgresql', 'mongodb', 'sqlite'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_NAME: str = 'cricket_shots'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    ECHO_SQL: bool = False


@dataclass
class LoggingConfig:
    """Logging configuration"""
    LOG_LEVEL: str = 'INFO'
    LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE: str = 'logs/app.log'
    MAX_LOG_SIZE: int = 10 * 1024 * 1024  # 10MB


@dataclass
class InferenceConfig:
    """Inference configuration"""
    CONFIDENCE_THRESHOLD: float = 0.75
    MIN_FRAMES: int = 10
    STRIDE: int = 5
    USE_GPU: bool = True
    BATCH_INFERENCE: bool = True
    INFERENCE_BATCH_SIZE: int = 8


class Config:
    """Main configuration class combining all configs"""
    
    def __init__(self):
        self.model = ModelConfig()
        self.training = TrainingConfig()
        self.preprocessing = PreprocessingConfig()
        self.data = DataConfig()
        self.api = APIConfig()
        self.database = DatabaseConfig()
        self.logging = LoggingConfig()
        self.inference = InferenceConfig()
        
        # Create required directories
        self._create_directories()
    
    def _create_directories(self):
        """Create required directories if they don't exist"""
        directories = [
            self.data.DATA_DIR,
            self.data.RAW_DATA_DIR,
            self.data.PROCESSED_DATA_DIR,
            self.data.ANNOTATIONS_DIR,
            self.training.CHECKPOINT_DIR,
            self.training.LOG_DIR,
            os.path.dirname(self.logging.LOG_FILE)
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def to_dict(self) -> Dict:
        """Convert configuration to dictionary"""
        return {
            'model': vars(self.model),
            'training': vars(self.training),
            'preprocessing': vars(self.preprocessing),
            'data': vars(self.data),
            'api': vars(self.api),
            'database': vars(self.database),
            'logging': vars(self.logging),
            'inference': vars(self.inference)
        }


# Create global config instance
config = Config()
