from setuptools import setup, find_packages

setup(
    name="ntwrk",
    version="1.0.2",
    author="khiat Mohammed Abderrezzak",
    author_email="khiat.dev@gmail.com",
    license="MIT",
    description="Sophisticate Graph",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/ntwrk/",
    packages=find_packages(),
    install_requires=[
        "hashtbl>=1.0.5",
    ],
    keywords=[
        "graph",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
