import boto3

client = boto3.client("opsworks")

stacks = {
    'd1': '5aaecd91-f15d-4d2c-b19e-5790bbad4431',
    'd2': '2342342-2342423-23434234'
}

class OpsworksInstanceManager:

    def __init__(self, stack):
        self.stack = stack

    @staticmethod
    def get_stacks():
        return list(stacks.keys())

    def start_stack(self):
        client.start_stack(stacks[self.stack])



