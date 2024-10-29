from setuptools import setup, find_packages

setup(
    name="Simple_Dropbox",                       # Nom de votre module
    version="1.0.5",                             # Version du module
    author="Grivy16",                            # Nom de l'auteur
    author_email="grivy16publix@gmail.com",     # Email de l'auteur
    description="Un accès plus simple mais moins complet à Dropbox",  # Description courte
    long_description=open("README.md").read(),   # Longue description (contenu du fichier README)
    long_description_content_type="text/markdown", # Type de contenu pour la longue description
    url="https://github.com/Grivy16/Dropbox_module.git", # Lien vers le dépôt GitHub (à modifier)
    packages=find_packages(),                     # Trouve tous les sous-modules
    install_requires=[                            # Liste des dépendances
        # Par exemple, 'requests', 'dropbox', etc.
    ],
    classifiers=[                                 # Classifications du module
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",                     # Version minimale de Python requise
)
