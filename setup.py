from setuptools import setup, find_packages


# Dynamically calculate the version
version = __import__('dcp').__version__

setup(
    name="ereuse-dcp",
    version=version,
    packages=find_packages(),
    license = 'AGPLv3 License',
    description = ('The Directory of Collection Points is a reverse geocoding'
                    ' system with the objective to offer a centralized way for'
                    ' Device Management Systems (DMS) to be able to operate '
                    'with the DMS responsible of a Place, when the only data '
                    'they have is their geolocation.'),
    url = 'https://github.com/eReuse/dcp',
    author = 'eReuse team',
    install_requires=['djangorestframework-gis'],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Utilities',
    ],
)
