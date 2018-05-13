from opsworks_stack_manager import *
from slackclient import SlackClient

class SlackManager:

    def __init__(self, channel):
        self.channel = channel

    def send_stacks(self):
        return OpsworksInstanceManager.get_stacks()




a = SlackManager("test")
print(a.send_stacks())