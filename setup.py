from setuptools import setup, find_packages

setup(
    name="questionpdfgenerator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["jinja2", "pdfkit", "reportlab"],
    extras_require={"dev": ["pytest", "black", "flake8"]},
    entry_points={
        "console_scripts": [
            "extract-questions=src.text_extraction:main",
            "generate-pdf=src.pdf_generation:main",
        ]
    },
    author="Abdessamad",
    description="A tool for extracting questions and generating PDFs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
