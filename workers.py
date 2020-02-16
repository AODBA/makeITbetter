from scipy import interpolate as lerp


class work:
    def __init__(self, n, instances, price):
        self.n = n
        self.instances = instances
        self.price = price

    def check_instance_limits(self):
            print("Instance number(" + str(self.n) + ") must be between 2 and 2000")

    def check_price_list_size(self):
            print('There are more than 100 items in the price list' + str(len(self.instances)) + ' ' + str(len(self.price)))

    def clean_instances(self):
        for index, item in enumerate(self.instances):
            if (item < 2) or (item > 2000):
                self.instances.pop(index)
                self.price.pop(index)

    def clean_prices(self):
        for index, item in enumerate(self.price):
            if (item == 0):
                self.instances.pop(index)
                self.price.pop(index)
            elif (item < 0):
                self.instances.pop(index)
                self.price.pop(index)
        for index, item in enumerate(self.price):
            if (item == 0):
                self.instances.pop(index)
                self.price.pop(index)
            elif (item < 0):
                self.instances.pop(index)
                self.price.pop(index)

    def check_db_same(self):
        # If Price list and Instance list are not having the same number of element exit
        if (len(self.price) != len(self.instances)):
            print("Price list and Instance list are not having the same number of element")

    def price_exists(self):
        self.clean_instances()
        self.clean_prices()
        priceEx = self.price[self.instances.index(self.n)]
        print(priceEx)

    def only_price(self):
        self.clean_instances()
        self.clean_prices()
        print(str(self.price[0]).format())

    def find_extrapolation(self):
        f = lerp.interp1d(self.instances[-2:], self.price[-2:], fill_value="extrapolate")
        v = f(self.n)
        print(str(round(float(str(f(self.n).astype(float))), 2)))

    # If Instance number is not in the db but there instances smaller and larger - run linear interpolation
    def find_interpolate(self):
            price_linear = []
            instances_linear = []
            price_filtered_small = []
            instances_filterd_small = []
            for index, item in enumerate(self.instances):
                if item < self.n:
                    instances_filterd_small.append(item)
                    price_filtered_small.append(self.price[index])
            price_filtered_big = []
            instances_filterd_big = []
            for index, item in enumerate(self.instances):
                if item > self.n:
                    instances_filterd_big.append(item)
                    price_filtered_big.append(self.price[index])
            price_linear.append(price_filtered_small[-1])
            price_linear.append(price_filtered_big[0])
            instances_linear.append(instances_filterd_small[-1])
            instances_linear.append(instances_filterd_big[0])
            f = lerp.interp1d(instances_linear, price_linear)
            print(str(f(self.n).astype(float)))
