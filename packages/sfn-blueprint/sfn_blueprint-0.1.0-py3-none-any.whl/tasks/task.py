class Task:
    def __init__(self, description: str, data=None, analysis=None, code=None):
        self.description = description
        self.data = data
        self.analysis = analysis
        self.code = code
