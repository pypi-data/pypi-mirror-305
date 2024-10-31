from setuptools import setup, find_packages

setup(
    name="autoreview-ufz-VS",
    version="0.2",
    packages=find_packages(),
    install_requires=["pandas", "tqdm", "numpy", "docx", "xlsxwriter", "scikit-learn"],
    entry_points={
        "console_scripts": ["autoreview=autoreview.__main__:main"],
    },
    author="Votre Nom",
    description="Un package pour automatiser des opérations sur des fichiers Excel.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/votre_github/autoreview",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
