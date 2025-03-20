from setuptools import setup

setup(
    name="cnw",
    version="0.3",
    packages=["cnw"],
    package_dir={"cnw": "cnw"},
    install_requires=[
        # Add your dependencies here
        "numpy",
        "pandas",
        "opencv-python",
    ],
    entry_points={
        "console_scripts": [
            # Add command line scripts here
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for crop and weed detection dataset",
    url="https://github.com/yourusername/cropandweed-dataset",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
