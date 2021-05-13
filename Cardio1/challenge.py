def triangle_type(sides):
    largest = 0
    counter = 0
    sum = 0

    if len(sides) == 3:
        for i in sides:
            sum = sum + i
            if largest < i:
                largest = i
        for i in sides:
            if largest == i:
                counter = counter + 1

        if sum - largest > largest:
            if counter == 1:
                print('The Triangle is Scalene')
            elif counter == 2:
                print('The triangle is Isosceles')
            elif counter == 3:
                print('The triangle is Equilateral')
        else:
            print('The triangles sides are NOT long enough')
    else:
        print('You need three sides to form a Triangle')


def first():
    print("""
    Welcome to TruLin software!
    We would like calculate if your triangle is:
    Scalene | Isosceles | Equilateral
    So please introduce the three sides in cm.
    """)
    side_a = int(input('Introduce side a: '))
    side_b = int(input('Introduce side b: '))
    side_c = int(input('Introduce side c: '))
    sides = (side_a, side_b, side_c)
    h = int(input('Introduce a heigh in cm: '))
    b = int(input('Introduce a base in cm: '))
    txt = 'The area of the Triangle is {}cm^2'

    area = (b * h) / 2

    print(txt.format(area))
    triangle_type(sides)


if __name__ == "__main__":
    first()