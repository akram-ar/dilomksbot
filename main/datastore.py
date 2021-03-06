# -*- coding: utf-8 -*-

from google.appengine.ext import ndb


__author__ = 'oon arfiandwi'


class DiloEvent(ndb.Model):
    """using Google Datastore as Database
    this is Model to save DILo Makassar events.
    """
    link = ndb.StringProperty(required=True, indexed=True)
    title = ndb.StringProperty(required=True, indexed=True)
    description = ndb.TextProperty()
    sendnotification = ndb.BooleanProperty(required=True, default=False)
    updated = ndb.DateTimeProperty()


class TelegramGroup(ndb.Model):
    """using Google Datastore as Database
    this is Model to save Telegram Group which receive notification broadcast
    """
    tgid = ndb.IntegerProperty(required=True)
    info = ndb.StringProperty()  # only remark, optional
    updated = ndb.DateTimeProperty()
