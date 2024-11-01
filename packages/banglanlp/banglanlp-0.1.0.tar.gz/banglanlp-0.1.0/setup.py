from setuptools import setup, find_packages

setup(
    name="banglanlp", 
    version="0.1.0",
    description="A Bangla stemmer for natural language processing (NLP)",
    long_description=open("README.md").read(),
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
