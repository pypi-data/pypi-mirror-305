from setuptools import setup, find_packages
setup(
    name='matrice',
    version='0.2',
    package_dir={'': 'src'},  # Point to the 'src' folder for packages
    packages=find_packages(where='src'),  # Find packages inside 'src'
)




