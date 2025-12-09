"""
Setup configuration for Cricket Shot Detection package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="cricket-shot-detection",
    version="1.0.0",
    author="Cricket Shot Detection Team",
    author_email="support@cricketshot.ai",
    description="AI-powered cricket shot detection and performance analysis system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cricket-shot-detection",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/cricket-shot-detection/issues",
        "Documentation": "https://cricket-shot-detection.readthedocs.io",
        "Source Code": "https://github.com/yourusername/cricket-shot-detection",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tensorflow>=2.13.0",
        "keras>=2.13.0",
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "flask>=2.3.0",
        "flask-cors>=4.0.0",
        "matplotlib>=3.8.0",
        "plotly>=5.17.0",
        "requests>=2.31.0",
        "pillow>=10.0.0",
        "tqdm>=4.66.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.10.0",
            "flake8>=6.1.0",
            "mypy>=1.6.0",
            "sphinx>=7.2.0",
            "sphinx-rtd-theme>=2.0.0",
        ],
        "gpu": [
            "tensorflow[and-cuda]>=2.13.0",
            "torch>=2.0.0",
            "torchvision>=0.15.0",
        ],
        "all": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.10.0",
            "flake8>=6.1.0",
            "mypy>=1.6.0",
            "fastapi>=0.104.0",
            "uvicorn>=0.24.0",
            "sqlalchemy>=2.0.0",
            "psycopg2-binary>=2.9.0",
            "pymongo>=4.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "cricket-shot-detect=src.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
