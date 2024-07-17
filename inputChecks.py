#Author: Henry Våg
#Description: File for checking user inputs


def mileageCheck(mileage):
    try:
        int(mileage)
        print("User mileage is a number")
        return mileage
    except:
        print("invalid input")
        
