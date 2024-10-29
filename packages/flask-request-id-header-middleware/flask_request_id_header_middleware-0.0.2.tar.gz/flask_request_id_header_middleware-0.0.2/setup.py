from setuptools import setup, find_packages

version = '0.0.2'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flask_request_id_header_middleware',
    version=version,
    author='Shatrugna Rao Korukanti',
    author_email='shatrugna_korukanti@tecnics.com',
    description='Python Flask Middleware to log and set Request ID in the HTTP header',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=[
        'Flask',
        # 'requests',
    ],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)