class StringStack:
    def __init__(self, *data):
        self.struct = ""
        self.locations = "0"
        self.locationDigits = "0"
        for i in list(data):
            self.struct += str(i)
            self.locations += str(len(str(i)))
            self.locationDigits += str(len(str(len(str(i)))))

    def pop(self):
        val = self.struct[:-(int(self.locations[:-int(self.locationDigits[-1])]) - 1)]
        self.struct = self.struct[:int(self.locations[:int(self.locationDigits[-1])])]
        return val

    def push(self, data):
        self.struct += str(data)
        self.locations += str(len(data))
        self.locationDigits += str(len(str(len(data))))

    def initialise(self):
        self.locations = ""
        self.locationDigits = ""
        self.struct = ""

    def printing(self):
        temp = self.struct
        temp1 = self.locations
        temp2 = self.locationDigits
        while len(temp1) > 1:
            temp = temp[int(temp1[int(temp2[0])]):]
            temp1 = temp1[int(temp2[0]):]
            temp2 = temp2[1:]


test = new StringStack(2, 5, 7)
