#Author: Henry Våg
#Description: Logic for maintenance selection (6K or 12K maintenance)


def maintenance_selection(mileage):
    mileage = float(mileage)
    if mileage < 6000:
        print("perform 1K maintenance according to manual")

    else:
        maintenance_variable = mileage/6000
        upcoming_maintenance_mileage = int(maintenance_variable) * 6000 + 6000
    
    print(upcoming_maintenance_mileage)