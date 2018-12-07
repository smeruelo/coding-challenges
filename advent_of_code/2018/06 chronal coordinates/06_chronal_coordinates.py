#!/usr/bin/python3
# https://adventofcode.com/2018/day/6

def area_1(points):
    max_x = max(points.values(), key=lambda x: x[0])[0]
    max_y = max(points.values(), key=lambda x: x[1])[1]
    grid = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
    for point_id, point in points.items():
        x, y = point[0], point[1]
        grid[y][x] = point_id

    # calculate min distances (brute force)
    for row in range(max_y + 1):
        for col in range(max_x + 1):
            if grid[row][col] == '.':
                min_distance = max_x + max_y
                min_point = '.'
                for point_id, point in points.items():
                    x, y = point[0], point[1]
                    distance = abs(col - x) + abs(row - y)
                    if distance < min_distance:
                        min_distance = distance
                        min_point = point_id
                        grid[row][col] = min_point
                    elif distance == min_distance:
                        min_point = '.'
                        grid[row][col] = min_point

    # determine IDs in borders
    up = set(grid[0])
    down = set(grid[-1])
    left = set([row[0] for row in grid])
    right = set([row[-1] for row in grid])
    borders = up | down | left | right

    # calculate areas for points not in borders
    max_area = 0
    for point_id in set(points.keys()).difference(borders):
        count = 0
        for row in grid:
            count += sum(map(lambda x: x == point_id, row))
        max_area = max(max_area, count)

    return max_area

def area_2(points):
    max_x = max(points.values(), key=lambda x: x[0])[0]
    max_y = max(points.values(), key=lambda x: x[1])[1]
    grid = [[False] * (max_x + 1) for _ in range(max_y + 1)]

    area = 0
    for row in range(max_y + 1):
        for col in range(max_x + 1):
            sum_distances = 0
            for point_id, point in points.items():
                x, y = point[0], point[1]
                sum_distances += abs(col - x) + abs(row - y)
            if sum_distances < 10000:
                grid[row][col] = True
        area += sum(grid[row])
    return area


if __name__ == '__main__':
    with open('06_chronal_coordinates.input') as f:
        data = f.read().split('\n')

    points = dict(enumerate(list(map(lambda x: list(map(int, x.split(', '))), data))))
    print(area_1(points))
    print(area_2(points))
