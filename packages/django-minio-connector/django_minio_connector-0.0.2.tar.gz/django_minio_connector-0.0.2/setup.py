from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'Django >= 5.1',
    'minio >= 7.2.10',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.11',
    'Environment :: Web Environment',
    'Framework :: Django :: 5.1',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

with open('../README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='django_minio_connector',
    version='0.0.2',
    url='https://github.com/max-dev-py/django-minio-connector',

    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    author='Maxim Ustinov',
    author_email='MaximVUstinovk@gmail.com',
    license='Apache License 2.0',

    description='Django storage backend to use MinIO as file storage. It is wrapper over "minio" library.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',

    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    keywords='django storage minio',
    python_requires='>=3.11',
)
