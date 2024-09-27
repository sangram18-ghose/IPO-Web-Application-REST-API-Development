from setuptools import setup, find_packages

setup(
    name="IPO_Web_Application_REST_API_Development",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Sangram Ghose",
    author_email="your.email@example.com",
    description="Provides detailed IPO info including company details, pricing, dates, and performance metrics.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sangram18-ghose/IPO-Web-Application-REST-API-Development",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
