# setup.py
from setuptools import setup, find_packages

setup(
    name="ser-gen",                    # نام پکیج
    version="1.0.0",                         # نسخه پکیج
    author="Ali Ayati",                      # نام نویسنده
    author_email="ayatiali910@gmail.com",   # ایمیل نویسنده
    description="A serial generator library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
