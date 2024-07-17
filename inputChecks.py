#Author: Henry Våg
#Description: File for checking user inputs


def mileageCheck(mileage):
    try:
        int(mileage)
        print("number")
    except:
        print("invalid input")
