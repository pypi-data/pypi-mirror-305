from setuptools import setup, find_packages


setup(
    name='armenian-rag-test',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
                "PyYAML==6.0.2",
                "python-docx==1.1.2",
                "Spire.Doc==12.7.1",
                "weaviate-client==4.8.1",
                "sentence-transformers==3.2.1",
                "python-dotenv==1.0.1",
                "tabulate==0.9.0",
                "python-multipart==0.0.9",
                "anthropic==0.37.1",
                "openai==1.52.2",
                "deeplake==3.9.26",
                "pypdf==5.1.0"
            ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the required Python version
)
