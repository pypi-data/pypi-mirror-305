from setuptools import setup, find_packages

setup(
    name='htcopkmeans',
    version='1.5',
    description='This is just a copy of the original repo https://github.com/Behrouz-Babaki/COP-Kmeans',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    author='Behrouz Babaki',
    author_email='',
    url='https://github.com/hongtaoh/COP-Kmeans',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
