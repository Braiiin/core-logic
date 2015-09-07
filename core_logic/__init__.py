"""

Sample Configuration
--------------------

Everything in this folder is simply a sample configuration. Feel free to
alter it entirely, or even restructure it.

You may wish to keep this file, however.

"""
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd()+"/logic"))

from logic import create_app


def create_core_app(**kwargs):
    """Create a template Flask app"""
    app = create_app(**kwargs)

    return app
