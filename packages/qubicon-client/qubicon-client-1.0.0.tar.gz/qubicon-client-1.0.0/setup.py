from setuptools import setup, find_packages

setup(
    name="qubicon-client",
    version="1.0.0",
    author="Stephan Karas",
    author_email="stephan.karas@qubicon-ag.com",
    description="CLI for interacting with the Qubicon platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://git.qub-lab.io/qub-client/models-client",
    packages=find_packages(),
    install_requires=[  # Specify dependencies here
        'pandas==2.2.3',
        'rapidfuzz==3.9.6',
        'requests==2.32.3',
        'rich==13.9.3',
        'tabulate==0.9.0',
    ],
    entry_points={
        "console_scripts": [
            "qubicon-client=qubicon_client.client:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
