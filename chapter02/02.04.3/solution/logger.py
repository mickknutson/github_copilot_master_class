# NOTE: import os is required for the operations on the file system.
# It has been added here to make the code pilot code generation
# easier to read and understand.
import os
import platform
import datetime


class Logger:

    def __init__(self, logfile):
        self.logfile = logfile

        # TODO 1.1:
        # Add code here
        if os.path.isdir(logfile):
            raise Exception("The path for the log file must be a file, not a directory.")

        folder = os.path.dirname(logfile)

        # TODO 1.2:
        # Add code here
        if not os.path.exists(folder):
            raise Exception("The folder for the log file does not exist.")


    def log(self, msg):
        machine = platform.node()
        now = datetime.datetime.now()
        date = "{0}_{1}_{2} {3}:{4}:{5}".format(
            now.year, now.month, now.day,
            now.hour, now.minute, now.second)

        text = "{0}/{1}: {2}".format(machine, date, msg)

        # TODO 1.3:

        # TODO 1.4:
        print("    log=" + text)

        # TODO 1.5:
        # OPTION 1: or
        # OPTION 2:
        with open(self.logfile, 'a+') as fout:
            fout.write("{0}\n".format(text))
