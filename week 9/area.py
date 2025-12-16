def triangle_area( b, h ):
    if b <= 0 or h <= 0:
        raise ValueError("Base and height must be positive numbers")
    return float(b*h/2)
