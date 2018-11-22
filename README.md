# moinmoin-import

Import file content into MoinMoin Wiki

## Installation

### Requirements

Python 3 is needed. Tested using latest stable Python 3.6.

Dependencies:

- requests
- bs4

Install with [pip](https://pip.pypa.io/en/stable/):

    pip install requests bs4

You don't have to install the script. Just download the latest stable version from [GitLab](https://gitlab.greenbone.net/qm/moinmoin-import/tags).

## Usage

See all options with:

    ./moinmoin_import.py --help

In this example, the script uses the provided credentials to login to the MoinMoin Wiki and upload the content of the files matching the pattern `page-*.txt`. Pages named after the file name (without extension) are created at the provided URL, for example `page-1.txt` becomes `https://wiki.example.com/Website/Archive/page-1`.

    ./moinmoin_import.py --username UserName --password ***** --files 'page-*.txt' --url https://wiki.example.com/Website/Archive/

You can upload single files using `--files page-1.txt`.

Existing content will be overwritten!
But MoinMoin is versioned, so nothing is lost.

## Known limitations

- For login the domain given by `--url` is used, so it will not work if the wiki is served
under different URL like https://example.com/wiki/. Subdomains are supported.
- You might have to higher the surge protection of the wiki or the sleep time in the script

## Support

For any question on the usage of this tool please ask David Kleuker (david.kleuker@greenbone.net). If you found a problem with the software, please [create an issue](https://gitlab.greenbone.net/qm/moinmoin-import/issues) on GitLab.

## Maintainer

This project is maintained by David Kleuker (david.kleuker@greenbone.net).

## Contributing

Your contributions are highly appreciated. Please [create a merge request](https://gitlab.greenbone.net/qm/moinmoin-import/merge_requests) on GitLab. Bigger changes need to be discussed with the development team via the [issues section on GitLab](https://gitlab.greenbone.net/qm/moinmoin-import/issues) first.

## License

Copyright (C) 2018 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
