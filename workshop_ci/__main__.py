# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import click
import logging
import sys

from .application import App


@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def hello_world(first_name, last_name, verbose):
    app = App()
    if verbose:
        print("Performing hello world.")
    print(app.get_hello_world(first_name, last_name))


@click.group()
def main(args=None):
    """Command line utility"""
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)


main.add_command(hello_world)


if __name__ == "__main__":
    sys.exit(main())
