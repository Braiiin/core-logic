#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/logic.braiiin.com/logic")
sys.path.insert(0,"/var/www/logic.braiiin.com")

from core_logic import create_core_app

app = create_core_app(root='core_logic', config='ProductionConfig')

if __name__ == "__main__":
    app.run(**app.config['INIT'])
