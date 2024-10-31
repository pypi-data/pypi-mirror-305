from setuptools import setup, find_packages

setup(
    name='alignMAP',
    version='1.0.0',
    description='Multi-Human-Value Alignment Palette (MAP) offers a first-principle approach to align AI systems with diverse, dynamically defined human values.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wang8740/MAP',
    author='Xinran Wang',
    author_email='wang8740@umn.edu',  # Replace with your actual email
    packages=find_packages(where="."),       # Automatically find packages
    package_dir={'': '.'},                   # Specify where packages are located
    include_package_data=True,               # Include non-code files specified in MANIFEST.in
    install_requires=[
        "torch>=2.4.0",
        "torchaudio>=2.4.1",
        "torchvision>=0.19.1",
        "transformers==4.44.2",
        "scikit-learn==1.3.2",
        "scipy==1.5.4",
        "pandas==2.0.3",
        "tqdm==4.66.5",
        "sentencepiece==0.2.0",
        "safetensors==0.4.5",
        "fastapi==0.115.0",
        "uvicorn==0.30.6",
        "wandb==0.18.1",
        "gradio==3.43.1",
        "sphinx==7.1.2",
        "sphinx-rtd-theme==3.0.1",
        "sphinxcontrib-mermaid==1.0.0",
        "dataset==1.6.2",
        "datasets==3.0.0",
        "huggingface-hub==0.25.0",
    ],
    python_requires='>=3.8',               
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
