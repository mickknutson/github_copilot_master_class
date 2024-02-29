# NOTE: import os is required for the operations on the file system.
# It has been added here to make the code pilot code generation
# easier to read and understand.
import os
import platform
import datetime


class Logger:

    def __init__(self, logfile):
        self.logfile = logfile

        """
        TODO 1.1:
        Verify logfile is a file reference not a directory
        If not, raise an exception stating "The path for the log file must be a file, not a directory."
        Create a reference called folder from logfile
        """
        # Add code here
        if not os.path.isfile(logfile):
            raise Exception("The path for the log file must be a file, not a directory.")
        
        folder = os.path.dirname(logfile)
        
        """
        TODO 1.2:
        Verify the folder exists
        If the folder does not exist, raise an exception stating "The folder for the log file does not exist."
        """
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

        """
        TODO 1.3: Remove the following print statement:
        """
        #print("******* LOG METHOD SHOULD BE IMPLEMENTED FIRST ******* ")

        """
        TODO 1.4: Highligh the below print statement, open copilot with 'comand+i' and enter the following prompt:
        Print the text reference to the console with the prefix "    log="
        """
        # add code here
        print("    log=", text)
        
        """
        TODO 1.5: 
        Open the log file reference with append plus mode
        String Format the text reference appending a newline character
        Write the formatted text to the log file
        """
        # OPTION 1: Add the code using copilot inline completion with prompt above:
        with open(self.logfile, 'a+') as fout:
            formatted_text = "{0}\n".format(text)
            fout.write(formatted_text)


        # OPTION 2: Put curser below and allow copilot to add code:
        #with open(self.logfile, 'a+') as fout:
        #    fout.write("{0}\n".format(text))


