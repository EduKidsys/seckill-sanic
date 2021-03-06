#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 shady <shady@MrRobot.local>
#

import logging
from sanic import Sanic
from sanic.response import json

from views import seckill_bp
from config import load_config
from config.server import app
from config.server import tracing


logger = logging.getLogger("sanic")

# add blueprint
app.blueprint(seckill_bp)


@app.route("/")
async def index(request):
    return json("seckill products")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=True)
