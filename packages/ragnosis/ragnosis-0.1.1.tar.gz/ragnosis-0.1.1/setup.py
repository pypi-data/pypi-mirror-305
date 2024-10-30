from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ragnosis",
    version="0.1.0",
    author="Gabriel Reder",
    author_email="gk@reder.io",
    description="A short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gkreder/ragnosis",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.3.0,<0.4",
        "streamlit==1.37",
        "bs4>=4.12.3,<5",
        "rdflib==7.0.0",
        "langchain-community>=0.3.0,<0.4",
        "langchain-ollama>=0.2.0,<0.3",
        "fastembed>=0.3.6,<0.4",
        "faiss-cpu>=1.8.0.post1,<2",
        "langchain-openai>=0.2.0,<0.3",
        "pymupdf>=1.24.10,<2",
        "sentence-transformers>=3.1.1,<4",
        "langchain-huggingface>=0.1.0,<0.2",
        "langgraph>=0.2.34,<0.3",
        "markdown>=3.7,<4",
        "pdfkit>=1.0.0,<2",
        "openai>=1.48.0,<2",
        "python-dotenv==1.0.1",
        "langchain-rdf @ git+ssh://github.com/vemonet/langchain-rdf.git",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)