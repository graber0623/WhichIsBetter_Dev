from logging import FileHandler, Formatter, INFO


class InfoFileLogger:
    def __init__(self, flaskapp, filename, level=INFO, format='%(asctime)s %(levelname)s: %(message)s'):
        self.app = flaskapp
        self.filename = filename
        self.level = level
        self.format = format
        self._setup_logger()

    def _setup_logger(self):
        handler = FileHandler(self.filename)
        handler.setLevel(self.level)
        handler.setFormatter(Formatter(self.format))
        self.app.logger.addHandler(handler)
