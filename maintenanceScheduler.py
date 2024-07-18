#Author: Henry Våg
#Description:

import json

class MaintenanceScheduler:

    def __init__(self, json_file):
        self.json_file = json_file
        self.maintenance_tasks = {}
        self.upcoming_maintenance_mileage = 0
        self.upcoming_maintenance_variable = 0
        self.load_tasks()

    


    def load_tasks(self):
        tasks = open(self.json_file)
        data = json.load(tasks)
        self.maintenance_tasks = data["motorcycles"]["kawasaki_er_5"]["maintenance_tasks"]
        

    def maintenance_selection(self, mileage):
        mileage = float(mileage)
        if mileage < 6000:
            print("perform 1K maintenance according to manual")

        else:
            maintenance_variable = mileage/6000
            self.upcoming_maintenance_mileage = int(maintenance_variable) * 6000 + 6000
            self.upcoming_maintenance_variable = self.upcoming_maintenance_mileage/12000
        
        print(f'Next maintenance to be performed at {self.upcoming_maintenance_mileage}km')    
        
        
    def print_upcoming_tasks(self):
        for task in self.maintenance_tasks:
            if task["interval_km"] != "" and self.upcoming_maintenance_mileage % task["interval_km"] == 0 :
                print(task)