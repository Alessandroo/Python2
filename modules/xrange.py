class MyXrange(object):
    def __init__(self, stop, start = 0, step = 1):
        self.stop = stop
        self.start = start
        self.step = step
        self.cur_value = start


    def __iter__(self):
        return self


    def __getitem__(self, item):
        return self.start + self.step * item


    def __len__(self):
        if self.start > self.stop:
            return 0
        return int((self.stop - self.start - 1) / self.step) + 1


    def __str__(self):
        return 'xrange({0}, {1}, {2})'.format(self.stop, self.start, self.step)


    def __next__(self):
        if self.cur_value < self.stop:
            result = self.cur_value
            self.cur_value += self.step

            return result
        else:
            self.cur_value = self.start
            raise StopIteration


def main():
    a = MyXrange(10)
    print(a)
    print("Length: {0}".format(len(a)))

    temp = []
    for i in a:
        temp.append(i)

    print(temp)
    print("\n")

    a = MyXrange(10, 5)
    print(a)
    print("Length: {0}".format(len(a)))

    temp = []
    for i in a:
        temp.append(i)

    print(temp)
    print("\n")

    a = MyXrange(21, 7, 3)
    print(a)
    print("Length: {0}".format(len(a)))

    temp = []
    for i in a:
        temp.append(i)

    print(temp)
    print("\n")


if __name__ == "__main__":
    main()
