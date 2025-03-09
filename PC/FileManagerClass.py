import time

class FileManager():

    def __init__(self, filename=None):

        if filename:
            self.filename = filename
        else: 
            self.filename = f"data_{time.time()}.csv"

    def save_data(self, data):
        # save data in a file everytime the mcu gives new data points
        pass