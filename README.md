# dcp
The Directory of Collection Points is a reverse geocoding system with the objective to offer a centralized way for Device Management Systems (DMS) to be able to operate with the DMS responsible of a Place, when the only data they have is their geolocation.

## Installation
    pip install https://github.com/eReuse/dcp/tarball/master

TODO: Postgis & DB.

## Setup
Add `rest_framework_gis` and `dcp` in `settings.INSTALLED_APPS`, after `rest_framework`:

    INSTALLED_APPS = [
        # ...
        'django.contrib.gis',
        'rest_framework',
        'rest_framework_gis',
        'dcp',
        # ...
    ]

## API Reference
TODO

## License
GNU Affero General Public License, version 3 ([AGPL v3](https://www.gnu.org/licenses/agpl-3.0.html))
