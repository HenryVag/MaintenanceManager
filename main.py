#Author: Henry Våg
#Description: Main file for maintenance manager application

from inputChecks import mileageCheck
from maintenanceSelectionLogic import maintenance_selection



def get_user_mileage():
    mileage = input("Enter driven kilometers:")
    if mileageCheck(mileage):
        return mileage
    
def main():
    while True:
        user_mileage = get_user_mileage()
        maintenance_selection(user_mileage)



if __name__=="__main__":
    main()