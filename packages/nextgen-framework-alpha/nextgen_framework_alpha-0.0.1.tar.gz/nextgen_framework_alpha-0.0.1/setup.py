from setuptools import setup, find_packages

setup(
    name="nextgen-framework-alpha",
    version="0.0.1",
    description="A Python library for the NextGen framework",
    author="Your Name",
    author_email="nextgen@example.com",
    url="https://github.com/yourusername/nextgen-framework",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "confluent-kafka",
        "openai",
        "azure-identity",
        "promptflow-tracing",
        "prompty",
    ],
    entry_points={
        "console_scripts": [
            "nextgen-cli=nextgen_framework.cli:main",
        ],
    },
)
