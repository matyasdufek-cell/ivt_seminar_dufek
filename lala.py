def rectangle_area(a, b):
    return f"{a*b} cm3"

def triangle_area(a, v):
    return f"{a*v/2} cm3"

if __name__ == "__main__":
    print(f"a = 3cm, b = 4cm, S={rectangle_area(3, 4)}")
    print(f"a = 3cm, v = 4cm, S={triangle_area(3, 4)}")