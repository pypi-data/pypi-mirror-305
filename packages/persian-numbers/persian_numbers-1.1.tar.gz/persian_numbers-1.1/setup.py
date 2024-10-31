from setuptools import setup, find_packages

setup(
    name='persian_numbers',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    description='A Django template filter to convert numbers to Persian in template tags',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hossein Meymandi',
    author_email='hossainm67@gmail.com',
    url='https://github.com/hmeymandi/persian_numbers',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
