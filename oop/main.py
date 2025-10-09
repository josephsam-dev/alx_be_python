from polymorphism_demo import Rectangle, Circle, Triangle  # <-- add Triangle here

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(6, 4)  # <-- add a Triangle instance
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
