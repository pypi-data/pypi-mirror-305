from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vectrs",
    version="0.3.1",
    author="Mir Sakib",
    author_email="sakib@paralex.tech",
    url="https://github.com/ParalexLabs/Vectrs-beta",
    description="A decentralized & distributed vector database network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "numpy>=1.21.5",
        "faiss-cpu>=1.7.2",
        "hnswlib>=0.8.0",
        "kademlia>=2.2.2",
        "aiohttp>=3.8.5",
        "websockets>=10.0",
        "scipy>=1.9.3",
        "anthropic>=0.2.8",
        "transformers>=4.30.2",
        "sentence-transformers>=2.2.2",
        "pydantic>=1.10.0",
        "networkx>=2.8.0",
        "langchain>=0.0.200",
        "loguru>=0.7.0",
    ],
    extras_require={
        'dev': [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.1",
            "black>=22.3.0",
            "isort>=5.10.1",
            "twine>=4.0.2",
            "build>=0.10.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "vectrs=vectrs.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/ParalexLabs/Vectrs-beta/issues",
        "Source": "https://github.com/ParalexLabs/Vectrs-beta",
        "Documentation": "https://docs.vectrs.xyz",
    },
)
