import workers

n = 60
instances = [1, 2, 50, 100, 500, 5000]
price =    [10, 2, 12, 16, 54.25, 1]


def interpolate(n):
    wk = workers.work(n,instances,price)

    if (n < 2 or n > 2000):
        wk.check_instance_limits()

    elif (len(instances) > 100 or len(price) > 100):
        wk.check_price_list_size()

    elif n in instances:
        wk.price_exists()

    elif len(instances) == 1:
        wk.only_price()

    elif (n > max(instances) or (n < min(instances))):
        wk.find_extrapolation()

    elif  min(instances) <= n <= max(instances):
        wk.find_interpolate()










