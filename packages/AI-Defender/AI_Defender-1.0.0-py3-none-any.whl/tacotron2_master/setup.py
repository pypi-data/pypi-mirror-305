from setuptools import setup, find_packages

setup(
    name='GionyTTS',
    version='0.1.0',
    description='GionyTTS: A Custom Text-to-Speech Engine',
    author='Giony Ortiz',
    author_email='your-email@example.com',
    url='https://github.com/yourusername/GionyTTS',  # Replace with your GitHub/project link
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        'torch>=2.4.0',
        'tensorflow>=2.14.0',
        'librosa>=0.10.0',
        'scipy>=1.10.1',
        'numpy>=1.24.0',
        'pandas>=2.0.0',
        'matplotlib>=3.8.0',
        'pydantic>=2.7.0',
        'transformers>=4.44.2',
        'datasets>=2.19.0',
        'sentencepiece>=0.1.99',
        'tqdm>=4.66.1',
        'pytorch-lightning>=2.1.0',
        'librosa>=0.9.2,<0.10.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
