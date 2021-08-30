trade_tryon = {'ns': 'green', 'ew': 'red'}
# Assertions are for programmer errors not user errors. Errors not meant to recover from. User errors raise exceptions.

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'yellow'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    assert 'red' in intersection.values(), 'Neither light is red.' + str(intersection)



switchLights(trade_tryon)