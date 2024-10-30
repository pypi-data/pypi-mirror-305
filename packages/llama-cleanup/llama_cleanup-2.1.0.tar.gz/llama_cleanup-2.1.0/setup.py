from setuptools import setup, find_packages

setup(
    name="llama-cleanup",
    version="2.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "langchain_ollama"
    ],
    extras_require={
        "all": []  # No extra dependencies, but triggers the inclusion of optional files
    },
    include_package_data=True,
    description="A package to process addresses and filter out noise",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Andrew",
    author_email="gordienko.adg@gmail.com",
    url="https://github.com/AndrewGordienko/address-cleanup",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'llama_cleanup_process=llama_cleanup.main:process_addresses',
        ],
    },
    package_data={
        "llama_cleanup": [
            "optional_files/clean_address_transformer_model.zip",
            "optional_files/mappings.json",
            "optional_files/tokenizer/*",
        ]
    },
    python_requires='>=3.8',
)

