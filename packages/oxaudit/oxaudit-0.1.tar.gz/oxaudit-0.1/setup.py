from setuptools import setup, find_packages

setup(
    name="oxaudit",                     # Name of the package
    version="0.1",                      # Initial version
    packages=find_packages(),           # Automatically find and include all packages
    install_requires=[],                # Add any dependencies here, if needed
    description="A simple package with a function that prints 'Hello, world!'",
    long_description=open("README.md").read(),    # Long description from README
    long_description_content_type="text/markdown", # Format of README
    url="https://github.com/yourusername/your-repository",  # Replace with your GitHub repo URL
    author="Your Name",                 # Your name
    author_email="you@example.com",     # Your contact email
    license="MIT",                      # License type
    classifiers=[                       # Additional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",            # Minimum Python version requirement
)
