from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in get_pass/__init__.py
from get_pass import __version__ as version

setup(
	name="get_pass",
	version=version,
	description="For generating visitors a get pass",
	author="Atharva",
	author_email="athrva.dhareshivkar@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
