from setuptools import setup, find_packages

setup(
    name="k8sidecar-python-lib",
    version="0.1",
    description="Descripción de tu librería",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Andoni Salcedo Navarro",
    author_email="andonisalcedo@gmail.com",
    url="https://github.com/cloudmedialab-uv/k8sidecar-python-lib",  
    packages=find_packages(exclude=["examples*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "cloudevents==1.11.0"
    ],
)
