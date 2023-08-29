class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity      # [None, None, None, None]
        self.__values = [None] * self.__max_capacity    # we treat them as arrays (masivi)
        self.__length = 0

    def add(self, key, value):
        self[key] = value

    def get(self, key, message=None):
        try:
            return self[key]
        except KeyError:
            return message

    def delete(self, key, message=None):
        try:
            del self[key]
            return f"{key} deleted"
        except KeyError:
            return message

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"{key} is not in the hash table")

    def __delitem__(self, key):
        try:
            index = self.__keys.index(key)
            # self.__keys.remove(key)
            # self.__values.pop(index)
            self.__keys[index] = None
            self.__values[index] = None
        except ValueError:
            raise KeyError(f"{key} is not in the hash table")

    def __setitem__(self, key, value):
        # if there is such key -> update the value
        # if there is not such key then catch the ValueError and continue
        try:
            index = self.__keys.index(key)
            self.__values[index] = value

        except ValueError:
            pass
        else:
            return

        # checking if there is space for this index
        if len(self) == self.__max_capacity:
            self.__resize()

        index = self.__calc_index(key)
        self.__keys[index] = key
        self.__values[index] = value

        self.__length += 1

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity

        self.__max_capacity *= 2

    def __calc_index(self, key):
        # will sum the ASCII values for every char in the key
        # to get a valid index we % by max_capacity (4) -> we'll always get numbers between 0-3
        index = sum(ord(c) for c in str(key)) % self.__max_capacity
        index = self.__get_index(index)

        return index

    def __get_index(self, index):
        while True:
            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity  # that way we'll always get a valid index
                # and doesn't go over the max_capacity (IndexError)

            index += 1

    def __len__(self):
        return self.__length

    def __str__(self):
        result = []

        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                result.append(f"{self.__keys[i]}: {self.__values[i]}")

        return "{" + ', '.join(result) + "}"


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = True
table["is_driver"] = False
table.add("can_fight", True)

print(table)
print(table.get("name"))
print(table.get("hi", "Hi does not exist"))
print(table.delete("is_driver", "Not Found"))
print(table.delete("is_driver", "Not Found"))
print(table["age"])
print(len(table))
