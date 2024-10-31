from setuptools import setup, find_packages

setup(
    name="autoreview-ufz-VS",
    version="1.0.1",
    author="Vianney Sicard",
    author_email="vianney.sicard@ufz.de",
    description="A package for automating operations on Excel files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_github_username/autoreviewufzvs",
    packages=find_packages(),  # Trouve tous les packages dans le projet
    install_requires=[
        "pandas>=1.1.0,<2.0.0",
        "tqdm>=4.0.0",
        "numpy>=1.18.0",
        "python-docx>=1.1.2",
        "XlsxWriter>=3.2.0",
        "scikit-learn>=1.5.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "autoreviewufzvs=autoreviewufzvs.__main__:main",
        ],
    },
)
