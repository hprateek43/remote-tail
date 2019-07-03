import sys
from os import path
import pusher

pusher_client = pusher.Pusher(
  app_id='617671',
  key='0f38f1644efd1f057d43',
  secret='1aab5d511aa2c5d2b18d',
  cluster='ap2',
  ssl=True
)


def tail_file(filename):
    # first check if the file exists
    if path.exists(filename):
        # open file and mark initial position as zero
        f = open(filename)
        p = 0
        while True:
            # move to the last known position
            f.seek(p)
            latest_data = f.read()
            # update the current postion
            p = f.tell()
            if latest_data:
                # send data to pubnub service 
                pusher_client.trigger('my-channel', 'my-event', {'message': latest_data})
                # optional: Enable printing in local console
                # print(latest_data)
    else:
        print("File does not exist. Bad Request")




if __name__ == "__main__":
    # The program takes the file to tail as the first arguement and show the logs on the terminal
    if len(sys.argv)>1:
        print("Trying to tail file: " , str(sys.argv[1]))
        tail_file(sys.argv[1])
    else:
        # handle the condtion when filename is missing
        print("Bad Invocation.\nUsage:  <scriptname> <file to tail>")


