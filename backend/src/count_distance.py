from math import radians, cos, sin, asin, sqrt

EARTH_RADIUS = 6371000


def count_distance(graph, start, end):
    start_lon = radians(graph.nodes[start]['x'])
    end_lon = radians(graph.nodes[end]['x'])
    start_lat = radians(graph.nodes[start]['y'])
    end_lat = radians(graph.nodes[end]['y'])

    distance_lon = end_lon - start_lon
    distance_lat = end_lat - start_lat
    a = sin(distance_lat / 2)**2 + cos(start_lat) * \
        cos(end_lat) * sin(distance_lon / 2)**2
    b = 2 * asin(sqrt(a))
    # return the distance in meters
    return (b * EARTH_RADIUS)
