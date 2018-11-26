# moinmoin-import

Import file content into MoinMoin Wiki

## Installation

### Requirements

Python 3 is needed. Tested using latest stable Python 3.6 and 3.5.

Dependencies:

- requests
- bs4

Install with [pip](https://pip.pypa.io/en/stable/):

    pip install requests bs4

You don't have to install the script. Just download the latest stable version from [GitHub](https://github.com/greenbone/moinmoin-import/releases).

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

For any question on the usage of moinmoin-import please
[create an issue](https://github.com/greenbone/moinmoin-import/issues) on GitHub.

## Maintainer

This project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/greenbone/moinmoin-import/pulls) on GitHub.
For bigger changes, please discuss it first in the
[issues](https://github.com/greenbone/moinmoin-import/issues).

Please follow our [Contribution guide](CONTRIBUTING.md).

## License

Copyright (C) 2018 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
