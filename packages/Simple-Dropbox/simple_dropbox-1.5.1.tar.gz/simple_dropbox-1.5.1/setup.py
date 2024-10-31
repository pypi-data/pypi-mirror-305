from setuptools import setup, find_packages

setup(
    name="Simple_Dropbox",
    version="1.5.1",
    author="Grivy16",
    author_email="grivy16publix@gmail.com",
    description="Un accès plus simple mais moins complet à Dropbox",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Grivy16/Dropbox_module/wiki",
    packages=find_packages(),
    install_requires=[
        # Ajoutez ici les bibliothèques dont votre module a besoin
        'requests',
        'dropbox',
        "clipboard",
        "customtkinter"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
