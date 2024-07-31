#Author: Henry Våg
#Description:

import json
from inputChecks import mileageCheck

class MaintenanceScheduler:

    def __init__(self, json_file):
        self.json_file = json_file
        self.maintenance_tasks = {}
        self.upcoming_maintenance_mileage = 0
        self.past_maintenance_mileage = 0
        self.upcoming_maintenance_variable = 0
        self.mileage = 0
        self.load_tasks()

    


    def load_tasks(self):
        tasks = open(self.json_file)
        data = json.load(tasks)
        self.maintenance_tasks = data["motorcycles"]["kawasaki_er_5"]["maintenance_tasks"]
        

    def maintenance_selection(self, mileage):
    # 

        mileage = float(mileage)
        if mileage < 6000:
            print("perform 1K maintenance according to manual")

        else:
            maintenance_variable = mileage/6000

            # Calculates the mileage for next maintenance
            self.upcoming_maintenance_mileage = int(maintenance_variable) * 6000 + 6000
            self.upcoming_maintenance_variable = self.upcoming_maintenance_mileage/12000

            #Calculates the mileage for the past/recent maintenance
            self.past_maintenance_mileage = int(maintenance_variable) * 6000 
            self.past_maintenance_variable = self.past_maintenance_mileage/12000
        
        
        
        
        
    def print_tasks(self):

        if self.upcoming_maintenance_mileage - int(self.mileage) < abs(self.past_maintenance_mileage - int(self.mileage)):
            self.print_upcoming_tasks()
        elif self.upcoming_maintenance_mileage - int(self.mileage) >abs(self.past_maintenance_mileage - int(self.mileage)):
            self.print_past_tasks()
        else:
            user_last_maintenance = input(f'Have you performed you last maintenance at {self.past_maintenance_mileage}km? y/n')
            if user_last_maintenance == "y":
                self.print_upcoming_tasks()
            elif user_last_maintenance == "n":
                self.print_past_tasks()
            else:
                print("Invalid input")

    def get_user_mileage(self):
        mileage = input("Enter driven kilometers:")
        if mileageCheck(mileage):
            self.mileage = mileage
            return mileage
        
    def print_upcoming_tasks(self):
        print("")
        print("--------------------")
        print(f'Next maintenance to be performed at {self.upcoming_maintenance_mileage}km')
        print("")
        for task in self.maintenance_tasks:
            if task["interval_km"] != "" and self.upcoming_maintenance_mileage % task["interval_km"] == 0 :
                print(task["description"])
        print("")
        print("--------------------")
    def print_past_tasks(self):
        print("")
        print("--------------------")
        print(f'Past maintenance should have been performed at {self.past_maintenance_mileage}km')
        print("")
        for task in self.maintenance_tasks:
            if task["interval_km"] != "" and self.past_maintenance_mileage % task["interval_km"] == 0 :
                print(task["description"])
        print("--------------------")
        print("")