#!/usr/local/bin/python3
import json
import os
from logger import Logger


class Program:
    def __init__(self):
        this_folder = os.path.dirname(__file__)
        data_folder = os.path.join(this_folder, os.pardir, "data")
        self.data_folder = os.path.abspath(data_folder)
        self.logger = Logger(os.path.join(self.data_folder, "log.txt"))

        print("*" * 50)
        print("* this_folder: ", this_folder)
        print("* data_folder: ", data_folder)
        print("* self.data_folder: ", self.data_folder)
        print("*" * 50)

    def run(self):
        try:
            self.log_startup()
            self.load_json()
            self.load_csv()
        except Exception as e:
            print(e.__repr__())

    def log_startup(self):
        self.logger.log("Application starting up...")
        self.logger.log("Data folder: {0}".format(self.data_folder))


    def load_json(self):
        filename = os.path.join(self.data_folder, "python-course.json")
        self.logger.log("******* BEGIN LOAD_JSON *******")

        # TODO 2.1:
        # TODO 2.2:
        self.logger.log("Opening JSON file: {0}".format(filename))

        # TODO 2.3:
        with open(filename, "r") as fin:
            data = json.loads(fin.read())
            print("Course title: {0}".format(data["Name"]))
            self.logger.log("Found course title to be: {0}".format(data["Name"]))
            engagements = data["Engagements"]
            print("Number of engagements: {0}".format(len(engagements)))
            print("Locations:")
            for e in engagements:
                print("\t" + e["City"] + " on " + e["StartDate"] + " [active? " + str(e["ActiveEngagement"]) + "]")
        print()


    def load_csv(self):
        filename = os.path.join(self.data_folder, "fx-seven-day.csv")
        self.logger.log("******* BEGIN LOAD_CSV *******")

        # TODO 3.1:
        # TODO 3.2:
        self.logger.log("Loading CSV file: {0}".format(filename))

        # TODO 3.3:

        """ TODO 3.5: Answer what is the 7 day average for RUPEEs to USD?
        (need to go from rupees -> canadian dollars -> usd)
        hint: build a lookup of each row by ID (e.g. CZK),
              store the seven day values as a list of floats.
             
        Prompt:
        lookup currency references
        Get reference to INR as rupee
        Lookup USD as usd

        Get the average rupees values per canadian dollar
        Get the average usd values per canadian dollar
        Get rupees per USD
        """
        # TODO: 3.6
        # Start by typing "lookup" and then pressing "tab" to see the method signature
        # This should run build_currency_lookup from the filename
        
        # TODO: 3.7, after you have the lookup, you can access the INR and USD values
        # simply hit ENTER and let Copilot do the work for you.

        lookup = self.build_currency_lookup(filename)
        rupee = lookup["INR"]
        usd = lookup["USD"]
        rupees_per_canadian_dollar = self.average(rupee["values"])
        usa_per_canadian_dollar = self.average(usd["values"])
        rupee_per_usd = usa_per_canadian_dollar / rupees_per_canadian_dollar

        # TODO 3.8: show and log the answer 1 USD is worth X Rupees
        # note: this value should be around 60.
        # we have provided an average method below for you to use

        # Print `1 USD is worth X Rupees.` and log it.

        print("1 USD is worth {0} Rupees.".format(rupee_per_usd))
        self.logger.log("1 USD is worth {0} Rupees.".format(rupee_per_usd))


    # TODO 3.4:
    @staticmethod
    def build_currency_lookup(filename):
        lookup = dict()
        with open(filename, "r") as fin:
            for line in fin:
                if line is None:
                    continue
                if line.strip().startswith("#"):
                    continue
                if line.strip().startswith("Date"):
                    continue

                parts = line.split(sep=',')
                entry = {
                    "name": parts[0].strip(),
                    "key": parts[1].strip(),
                    "values": [
                        float(parts[2]),
                        float(parts[3]),
                        float(parts[4]),
                        float(parts[5]),
                        float(parts[6]),
                        float(parts[7]),
                        float(parts[8]),
                    ]
                }

                lookup[entry["key"]] = entry
        return lookup


    @staticmethod
    def average(numbers):
        if len(numbers) <= 0:
            return float('nan')

        return sum(numbers) / float(len(numbers))


if __name__ == "__main__":
    p = Program()
    p.run()