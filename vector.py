import random
import os

class MyVector:

    def __init__(self, args):
        if isinstance(args, list) and all(isinstance(x, (int, float)) for x in args):
            self.values = args
        else:
            raise RuntimeError("Vector must be in form of a list with int/floats")

    @classmethod
    def load_from_file(cls, filename):
        try:
            filesize = os.path.getsize(filename)
            if filesize == 0:
                raise RuntimeError("File is empty")
            else:
                file_open = open(filename)
                lines = []
                for line in file_open:
                    line = line.strip()
                    if line == "":
                        continue
                    else:
                        lines.append(line)
            file_open.close()
            vector = []
            for l in lines:
                try:
                    l = float(l)
                    vector.append(l)
                except ValueError:
                    raise RuntimeError("Wrong value ")
            return MyVector(vector)
        except FileNotFoundError:
            raise RuntimeError(filename + " file does not exist!")

    def save_to_file(self, filename):
        content = self.values
        if content != []:
            f = open(filename, "w")
            for i in content:
                f.write(str(i) + "\n")
        else:
            raise RuntimeError("There is nothing to save! ")
        f.close()

    def __getitem__(self, idx):
        return self.values[idx]

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return str(self.values)

    def __add__(self, other):
        result = []
        if isinstance(other, (int, float)):
            raise RuntimeError("One value can not be added to vector")
        elif isinstance(other, str):
            raise RuntimeError("String value can not be added to vector")
        elif isinstance(other.values, list):
            if len(self.values) == len(other.values):
                for (i, j) in zip(self.values, other.values):
                    result.append(i + j)
            elif other.values == []:
                raise RuntimeError("Empty list can not be added to vector")
            else:
                raise RuntimeError("Vectors don't have the same length")
        else:
            raise RuntimeError("Only vectors can be added to vector")
        return MyVector(result)

    def __iadd__(self, other):
        result = []
        if isinstance(other, (int, float)):
            raise RuntimeError("One value can not be added to vector")
        elif isinstance(other, str):
            raise RuntimeError("String value can not be added to vector")
        elif isinstance(other.values, list):
            if len(self.values) == len(other.values):
                for (i, j) in zip(self.values, other.values):
                    result.append(i + j)
                self.values = result
            elif other.values == []:
                raise RuntimeError("Empty list can not be added to vector")
            else:
                raise RuntimeError("Vectors don't have the same length! ")
        return self

    def __mul__(self, other):
        result = []
        if isinstance(other, (int, float)):
            for i in self.values:
                result.append(i * other)
        elif isinstance(other, str):
            raise RuntimeError("String value can not be multiply by vector")
        elif isinstance(other.values, list):
            if len(self.values) == len(other.values):
                for (i, j) in zip(self.values, other.values):
                    result.append(i * j)
            elif other.values == []:
                raise RuntimeError("Empty list can not be multiply by vector")
            else:
                raise RuntimeError("Vectors don't have the same length ")
        return MyVector(result)

    __rmul__ = __mul__

    def __imul__(self, other):
        result = []
        if isinstance(other, (int, float)):
            for i in self.values:
                result.append(i * other)
                self.values = result
        elif isinstance(other, str):
            raise RuntimeError("String value can not be multiply by vector")
        elif isinstance(other.values, list):
            if len(self.values) == len(other.values):
                for (i, j) in zip(self.values, other.values):
                    result.append(i * j)
                    self.values = result
            elif other.values == []:
                raise RuntimeError("Empty list can not be multiply by vector")
            else:
                raise RuntimeError("Vectors don't have the same length ")
        return self

    def inner_product(self, other):
        if isinstance(other, (int, float)):
            raise RuntimeError("This method is possible only for vectors")
        elif isinstance(other, str):
            raise RuntimeError("This method is possible only for vectors")
        elif isinstance(other.values, list):
            if other.values == []:
                raise RuntimeError("This method is not possible for empty list")
            elif len(self.values) == len(other.values):
                r = []
                for (a, b) in zip(self.values, other.values):
                    r.append(a * b)
                result = [sum(r)]

            else:
                raise RuntimeError("Vectors don't have the same lengths")

        return MyVector(result)

    def cross_product(self, other):
        if isinstance(other, (int, float)):
            raise RuntimeError("This method is possible only for vectors")
        elif isinstance(other, str):
            raise RuntimeError("This method is possible only for vectors")
        elif isinstance(other.values, list):
            if other.values == []:
                raise RuntimeError("This method is not possible for empty list")
            elif (len(self.values) == 3 and len(self.values) == 3):
                result = []
                x = (self.values[1] * other.values[2]) - (self.values[2] * other.values[1])
                y = (self.values[2] * other.values[0]) - (self.values[0] * other.values[2])
                z = (self.values[0] * other.values[1]) - (self.values[1] * other.values[0])
                result.append(x)
                result.append(y)
                result.append(z)
            else:
                raise RuntimeError("Only possible for vectors with length = 3")
        return MyVector(result)

    @classmethod
    def random_vector(cls, length): #if the lengths = 10 indexes are from 0 to 9
        vector = []
        if length == 0:
            raise RuntimeError("Empty vector is not allowed")
        else:
            for i in range(length):
                vector.append(0)
            lowerBound = 1
            upperBound = 1000
            for i in range(len(vector)):
                v = random.uniform(lowerBound, upperBound)
                v = round(v, 5)
                vector[i] = v
        return MyVector(vector)

v1 = MyVector([1,2,3])
v2 = MyVector([4,5,6])
v3 = MyVector([1,2,3,4,5])
v4 = MyVector([])
v5 = MyVector([6,7,8,9,10])

print(v5[0])
#load_from_file
#v = MyVector.load_from_file('file.txt')
#v = MyVector.load_from_file('empty_file.txt') #file is empty
#v = MyVector.load_from_file('filefilefile.txt') #file with this name does not exist
#v = MyVector.load_from_file('wrongValues.txt') #this file has 'x y z' as values
#v = MyVector.load_from_file('twodigit.txt')
#print(str(v))

#save_to_file
#v1 = MyVector([1, 2, 3])
#v = v1.save_to_file('saveVector.txt')
#check = MyVector.load_from_file('saveVector.txt')
#print(check.values)
#v = MyVector([])
#v.save_to_file('empty_save.txt')

#v2 = MyVector([10, 20, 30])
#v = v2.save_to_file('twoDigit_save.txt')
#check = MyVector.load_from_file('twoDigit_save.txt')
#print(check.values)
#v4.save_to_file('z.txt') #empty list to save

#v = MyVector.load_from_file('twodigit.txt')
#print(v)

#v1 = MyVector([1, 2, 3])
#result = v1.save_to_file('save.txt')
#check = MyVector.load_from_file('save.txt')
#print(check.values)

#__add__
#print(v1 + v2)
#print(v1 + 5)
#print(v1 + 'f')
#print(v1 + v3)
#print(v1 + v4)

#__iadd__
#v1 += v2
#print(v1)
#v1 += 5
#print(v1)
#v1 += 'f'
#print(v1)
#v1 += v3
#print(v1)
#v1 += v4
#print(v1)

#__mul__
#print(v1 * v2)
#print(v1 * 'f')
#print(v1 * v3)
#print(v1 * v4)

#__imul__
#v1 *= v2
#print(v1)
#v1 *= 5.0
#print(v1)
#v1 *= 'f'
#print(v1)
#v1 *= v3
#print(v1)
#v1 *= v4
#print(v1)

#inner product
#v = v1.inner_product(v2)
#v = v1.inner_product(5)
#v = v1.inner_product('f')
#v = v1.inner_product(v4) #with empty list
#v = v3.inner_product(v5)  #vectors with lengths  = 5
#v = v1.inner_product(v5) #another lengths of vectors
#print(str(v))

#cross_product
#v = v1.cross_product(v2)
#v = v1.cross_product(5)
#v = v1.cross_product('f')
#v = v1.cross_product(v4) #with empty list
#v = v3.cross_product(v5) #vectors with other lengths than 3
#v = v3.cross_product(v5) #v3 has length = 3, v5 - 5
#print(str(v))












