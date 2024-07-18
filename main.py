#Author: Henry Våg
#Description: Main file for maintenance manager application

from inputChecks import mileageCheck
from maintenanceSelectionLogic import maintenance_selection
from maintenanceScheduler import MaintenanceScheduler




def get_user_mileage():
    mileage = input("Enter driven kilometers:")
    if mileageCheck(mileage):
        return mileage
    
def main():
    app = MaintenanceScheduler("tasks.json")
    while True:
        user_mileage = get_user_mileage()
        app.maintenance_selection(user_mileage)
        app.load_tasks()
        app.print_upcoming_tasks()



if __name__=="__main__":
    main()


