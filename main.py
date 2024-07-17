#Author: Henry Våg
#Description: Main file for maintenance manager application

from inputChecks import mileageCheck



def get_user_mileage():
    mileage = input("Enter driven kilometers:")
    if mileageCheck(mileage):
        return mileage

def main():
    while True:
        get_user_mileage()
        



if __name__=="__main__":
    main()