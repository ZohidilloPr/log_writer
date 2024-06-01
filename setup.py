from setuptools import setup, find_packages

setup(
    name='log_writer',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    author='Zohidillo Turgunov',
    license="MIT",
    author_email='zohidilloturgunov@mail.ru',
    description='A simple logging package, Loglarni filega yozib borish uchun kichik packege',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/ZohidilloPr/log_writer/tree/main',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
