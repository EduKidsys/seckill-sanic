#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 shady <shady@MrRobot.local>
#
import datetime
from peewee import MySQLDatabase
from peewee import (
    Model,
    CharField,
    IntegerField,
    BooleanField,
    FloatField,
    DateTimeField,
    PrimaryKeyField,
)
from config import load_config

config = load_config()
db = MySQLDatabase(**config["DB_CONFIG"])


class Product(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=250, unique=True)
    description = CharField(max_length=600, null=True)
    price = FloatField(default=0)
    inventory = IntegerField(default=0)
    created = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = "product"
        database = db
