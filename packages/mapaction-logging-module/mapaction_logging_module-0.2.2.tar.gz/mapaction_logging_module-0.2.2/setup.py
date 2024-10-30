from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mapaction_logging_module',
    version='0.2.2',
    author='Harry Sibbenga',             
    author_email='hsibbenga@mapaction.org',
    description='A structured logging module for MapAction applications with a Dashboard',
    long_description=long_description,  
    long_description_content_type="text/markdown", 
    url='https://github.com/mapaction/mapaction_logging_module.git',  
    packages=find_packages(),          
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',           
    install_requires=["streamlit", "pandas"]              
)