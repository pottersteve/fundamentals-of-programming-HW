def analyze_courses(course_a, course_b):
    res = {}
    res["all"] = course_a.union(course_b)
    res["both"] = course_a.intersection(course_b)
    res["disjoint"] = len(course_a.intersection(course_b)) == 0
    res["only_a"] = course_a.difference(course_b)
    res["only_b"] = course_b.difference(course_a)

    return res