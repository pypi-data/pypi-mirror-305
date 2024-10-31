# setup.py
from setuptools import setup, find_packages

setup(
    name="recaptcha_solver_google",
    version="0.1.0",
    author="Mohd Shakir",
    author_email="mohdshakir02003@gmail.com",
    description="A package to solve Google reCAPTCHA using Selenium.",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "pydub",
        "SpeechRecognition",
        "urllib3",  # Add more dependencies if needed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
