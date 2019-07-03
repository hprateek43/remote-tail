import pysher
import sys
import time
import json
# Add a logging handler so we can see the raw communication data. Enable to run in verbose mode. Can be set to be enabled via a flag like debug
# import logging
# root = logging.getLogger()
# root.setLevel(logging.INFO)
# ch = logging.StreamHandler(sys.stdout)
# root.addHandler(ch)
appkey = '0f38f1644efd1f057d43'
cluster = "ap2"
pusher = pysher.Pusher(appkey,cluster=cluster)

def  my_func(*args, **kwargs):
    print(json.loads(args[0])["message"])

# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able
def connect_handler(data):
    channel = pusher.subscribe('my-channel')
    channel.bind('my-event', my_func)

pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

while True:
    # Do other things in the meantime here...
    time.sleep(1)