from setuptools import setup, find_packages

setup(
    name="zohencel-ai",
    version="0.1.0",
    description="A Python package for voice assistant, chatbot development, and analysis tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vishnu K",
    author_email="vishnuperiye26@gmail.com",
    url="https://github.com/yourusername/zohencel-ai",
    packages=find_packages(),
    install_requires=[
        "numpy",            # For numerical processing
        # "scipy",            # For audio signal processing
        # "pyaudio",          # For voice input/output
        # "nltk",             # For NLP tasks
        # "transformers",     # For pre-trained language models
        "requests",         # For making API calls
        # Add more dependencies as required
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
