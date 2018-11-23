from math import sqrt

def main():

    n = 3
    c = ['c1', 'c2', 'c3']
    x = [1, 2, 3]
    y = [3, 2, 3]
    q = ['c1', 'c2', 'c3']

    closestStraightCity(c, x, y, q)


def closestStraightCity(c, x, y, q):

    results = []

    dicty = {}

    for i in range(0, len(c)):
        dicty[c[i]] = [x[i], y[i]]

    print(dicty)

    for query in q:
        city = dicty[query]
        print("city: {}".format(city))
        set = {}

        for key in dicty:
            if bool(dicty[key][0] == city[0]) ^ bool(dicty[key][1] == city[1]):
                set[key] = dicty[key]
        print(set)

        if len(set) == 0:
            results.append('NONE')
            continue
        # if len(set) == 1:
        #     for key in set:
        #         results.append(key.__str__())
        #     # continue

        smallest_distance = 100000000
        closestCity = ''
        for key in set:
            one = set[key][0] - city[0]
            one *= one

            two = set[key][1] - city[1]
            two *= two

            distance = sqrt(one + two)
            if distance < smallest_distance:
                smallest_distance = distance
                closestCity = key.__str__()
            print(distance)

        results.append(closestCity)
        print('End Query')
    print(results)

    return results



if __name__ == "__main__":
    main()
