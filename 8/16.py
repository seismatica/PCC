from car_generator import make_car as mc


def main():
    subaru = mc("subaru", "outback", color="blue", tow_package=True)
    print(subaru)


main()