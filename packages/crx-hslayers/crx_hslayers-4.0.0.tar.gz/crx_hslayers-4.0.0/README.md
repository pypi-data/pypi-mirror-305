# HSLayers-NG map widget for Wagtail CodeRed CMS

Note: Has npm dependency on [HSLayers-NG](https://www.npmjs.com/package/hslayers-ng-app) that gets automatically installed into static files. `python manage.py collectstatic` must be executed for the module to correctly locate the HSLayers bundles.

## Instalation

1. Install this package from PyPi using folowing command:

```
$ pip install crx-hslayers
```

2. Add 'hslayers' and 'wagtail_crx_block_frontend_assets' to the INSTALLED_APPS list in the settings/base.py

```
INSTALLED_APPS = [
    # This project
    'website',

    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    ...
    'wagtail_crx_block_frontend_assets',
    'crx_hslayers'
]
```

3. Install HSLayers app package from npm

```
cd ./static/hslayers
npm install
```

4. Use crx_hslayers in any of your Wagtail models and migrate properly

5. Collect static files from crx-hslayers to your Wagtail site

```
$ python3 manage.py collectstatic
```

6. Restart Wagtail

7. New HSLayers blocks are added to the CMS
   - HSLayers map
   - Clima map

## Development

Update semantic version of the package

Run test update without commiting

```
$ bumpver update --patch(--minor|--major) --dry
```

Run update and commit the changes to the repo

```
$ bumpver update --patch(--minor|--major)
```

## Manual package publishing

Delete all previous builds in the dist/\* directory.

Linux:

```
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```

Windows:

```
py -m build
py -m pip install --upgrade twine
py -m twine upload dist/*
```

Use `__token__` for the username and API token acquired at pypi.org for password.

Upload to Test PyPi:

```
python3 -m twine upload --repository testpypi dist/*
```
