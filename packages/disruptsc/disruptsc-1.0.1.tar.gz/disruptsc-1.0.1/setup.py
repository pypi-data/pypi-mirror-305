from setuptools import setup, find_packages

setup(
    name="disruptsc",
    version="1.0.1",
    description="A spatial agent-based model to simulate the dynamics supply chains subject to disruptions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Celian Colon",
    author_email="celian.colon.2007@polytechnique.org",
    url="https://github.com/ccolon/disruptsc",
    packages=find_packages(),
    license="CC BY-NC-ND 4.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "cpython",
        "geopandas==0.11.1",
        "networkx==2.8.6",
        "PyYAML==6.0"
    ],
)
