def run():
    client_choice = int(input("""
    Welcome to VoLum Calculator!
    Please choose a geometry shape:
    1) Cylinder
    2) Sphere
    """))
    PI = 3.14

    if client_choice == 1:
        h = float(input('Introduce a Height for the Cylinder: '))
        r = float(input('Introduce a radio for the Cylinder: '))

        cylinder_volume = PI * r**2 * h
        cylinder_volume = round(cylinder_volume, 2)
        txt = "The result has come. The volume is {} cm^3"
        print(txt.format(cylinder_volume))
    elif client_choice == 2:
        r = float(input('Introduce a radio for the Sphere: '))

        sphere_volume = (4 / 3) * PI * r**3
        sphere_volume = round(sphere_volume, 2)
        txt = "The result has come. The volume is {} cm^3"
        print(txt.format(sphere_volume))
    else:
        print('Please choose a correct option')


if __name__ == "__main__":
    run()