from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="banglanlp", 
    version="0.1.3",
    description="A Bangla Toolkit for natural language processing (NLP)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Md Istiak Tanvir",
    author_email="eruddro@gmail.com",  
    license="MIT",
    packages= find_packages(),
     package_data={
        "banglanlp": ["data/*.json"],  
    },
    install_requires=["pandas",],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Text Processing :: Linguistic",
        'Operating System :: OS Independent'
    ],
    python_requires=">=3.6",
)
