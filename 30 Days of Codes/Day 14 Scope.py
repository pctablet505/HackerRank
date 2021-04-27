self.maximumDifference = float('-inf')


def computeDifference(self):
    for i in range(len(self.__elements)):
        for j in range(i + 1, len(self.__elements)):
            self.maximumDifference = max(self.maximumDifference, abs(self.__elements[i] - self.__elements[j]))


# Add your code here
