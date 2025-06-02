from setuptools import setup, find_packages

setup(
    name="rpg_backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.95.2",
        "uvicorn==0.22.0",
        "motor==3.1.2",
        "pymongo==4.3.3",
        "beanie==1.19.1"
    ],
    python_requires=">=3.9"
)
