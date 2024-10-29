from setuptools import setup, find_packages

setup(
    name="uk_fuel_prices_api",
    version="1.0.0",
    package_dir={"": "src"},  # Tell setuptools packages are under src
    packages=find_packages(where="src"),
    install_requires=[
        "fastapi",
        "uvicorn",
        "aiohttp",
        "pandas",
        "pydantic"
    ],
)