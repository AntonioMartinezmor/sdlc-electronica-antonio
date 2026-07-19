import json
class Recorder:
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, message:dict):
        with open(self.filename, "a") as f:
            f.write(json.dumps(message)+"\n")
            