from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SentiToolKit",
    version="0.1.3",
    packages=find_packages(),  
    package_data={
        'SentiToolKit': ['SentiToolKit.keras', 'tokenizer.pkl'],
    },
    install_requires=[
        "tensorflow>=2.0",
        "scikit-learn",
    ],
    author="abcd",
    author_email="abcd@gmail.com",
    description="A sentiment analysis toolkit using a pre-trained TensorFlow model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Niall1985/SentiToolKit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sentitoolkit=SentiToolKit.Main_tensor_model:main',  
        ],
    },
)
