from math import radians, cos, sin, asin, sqrt

EARTH_RADIUS = 6371000


def count_distance(graph, start, end):
    start_object = graph.nodes[start]
    end_object = graph.nodes[end]

    start_lng = radians(start_object.position[1])
    end_lng = radians(end_object.position[1])
    start_lat = radians(start_object.position[0])
    end_lat = radians(end_object.position[0])

    distance_lon = end_lng - start_lng
    distance_lat = end_lat - start_lat
    a = sin(distance_lat / 2)**2 + cos(start_lat) * \
        cos(end_lat) * sin(distance_lon / 2)**2
    b = 2 * asin(sqrt(a))
    # return the distance in meters
    return (round(b * EARTH_RADIUS, 3))
