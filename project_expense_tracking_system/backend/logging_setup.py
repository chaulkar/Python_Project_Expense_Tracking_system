import logging

def setup_logger(name, log_file="server.log", level=logging.DEBUG ):

    #create custom logger
    logger = logging.getLogger(name)

    #configure the custom logger
    logger.setLevel(level)
    filehandler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger
