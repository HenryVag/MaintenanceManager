#Author: Henry Våg
#Description: Main file for maintenance manager application

from inputChecks import mileageCheck
from maintenanceSelectionLogic import maintenance_selection
from maintenanceScheduler import MaintenanceScheduler


    
def main():
    app = MaintenanceScheduler("tasks.json")
    while True:
        user_mileage = app.get_user_mileage()
        app.maintenance_selection(user_mileage)
        app.load_tasks()
        app.print_upcoming_tasks()



if __name__=="__main__":
    main()


