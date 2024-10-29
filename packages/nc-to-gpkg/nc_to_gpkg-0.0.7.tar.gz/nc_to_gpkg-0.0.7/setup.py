from setuptools import setup, find_packages

setup(
    name="nc_to_gpkg",
    version="0.0.7",
    description="A package for processing NetCDF files and merging with shapefiles",
    author="Isaac Barnhart",
    author_email="isaac.barnhart@corteva.com",
    packages=find_packages(),
    install_requires=['pandas', 'geopandas', 'xarray', 'shapely', 'tqdm'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)