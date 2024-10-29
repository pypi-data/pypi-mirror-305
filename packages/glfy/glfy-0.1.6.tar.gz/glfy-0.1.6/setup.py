from setuptools import setup, find_packages

# Read the contents of the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="glfy",
    version="0.1.6",
    description="Convert videos and images to ASCII art, including live streaming.",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    author="dumgum82",
    author_email="dumgum42@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'glfy': ['fonts/**/*'],
    },
    install_requires=[
        "opencv-python",
        "Pillow",
        "numpy",
        "mediapipe",
        "pyvirtualcam",
        "mss"
    ],
    entry_points={
        'console_scripts': [
            'glfy=glfy.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
