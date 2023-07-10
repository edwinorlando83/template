from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gt_food/__init__.py
from gt_food import __version__ as version

setup(
	name="gt_food",
	version=version,
	description="Sistema de Punto de Venta personalizado",
	author="michacloud",
	author_email="edwinorlando83@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
