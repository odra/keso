import requests

class Keso(object):
  def __init__(self, api_token=None):
    self.api_token = api_token

  def ping(self):
    pass