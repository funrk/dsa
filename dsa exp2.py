class HashFunction:
    def _init_(self):
        self.h = [{'key': -1, 'name': 'NULL'} for _ in range(10)]

    def insert(self):
        cnt = 0
        while cnt < 10:
            k = int(input("\n\tEnter a Telephone No: "))
            n = input("\n\tEnter a Client Name: ")
            hi = k % 10  # hash function
            if self.h[hi]['key'] == -1:
                self.h[hi]['key'] = k
                self.h[hi]['name'] = n
            else:
                if self.h[hi]['key'] % 10 != hi:
                    temp = self.h[hi]['key']
                    ntemp = self.h[hi]['name']
                    self.h[hi]['key'] = k
                    self.h[hi]['name'] = n
                    flag = False
                    for i in range(hi + 1, 10):
                        if self.h[i]['key'] == -1:
                            self.h[i]['key'] = temp
                            self.h[i]['name'] = ntemp
                            flag = True
                            break
                    if not flag:
                        for i in range(hi):
                            if self.h[i]['key'] == -1:
                                self.h[i]['key'] = temp
                                self.h[i]['name'] = ntemp
                                break
                else:
                    flag = False
                    for i in range(hi + 1, 10):
                        if self.h[i]['key'] == -1:
                            self.h[i]['key'] = k
                            self.h[i]['name'] = n
                            flag = True
                            break
                    if not flag:
                        for i in range(hi):
                            if self.h[i]['key'] == -1:
                                self.h[i]['key'] = k
                                self.h[i]['name'] = n
                                break
            cnt += 1
            ans = input("\n\t..... Do You Want to Insert More Key: y/n")
            if ans.lower() != 'y':
                break

    def find(self, k):
        for i, entry in enumerate(self.h):
            if entry['key'] == k:
                print("\n\t", entry['key'], " is Found at ", i, " Location With Name ", entry['name'])
                return i
        return -1

    def display(self):
        print("\n\t\tKey\t\tName")
        for i, entry in enumerate(self.h):
            print("\n\th[", i, "]\t", entry['key'], "\t\t", entry['name'])

    def delete(self, k):
        index = self.find(k)
        if index == -1:
            print("\n\tKey Not Found")
        else:
            self.h[index]['key'] = -1
            self.h[index]['name'] = 'NULL'
            print("\n\tKey is Deleted")


def main():
    obj = HashFunction()
    while True:
        print("\n\t***** Telephone (ADT) *****")
        print("\n\t1. Insert\n\t2. Display\n\t3. Find\n\t4. Delete\n\t5. Exit")
        ch = int(input("\n\t..... Enter Your Choice: "))
        if ch == 1:
            obj.insert()
        elif ch == 2:
            obj.display()
        elif ch == 3:
            k = int(input("\n\tEnter a Key Which You Want to Search: "))
            index = obj.find(k)
            if index == -1:
                print("\n\tKey Not Found")
        elif ch == 4:
            k = int(input("\n\tEnter a Key Which You Want to Delete: "))
            obj.delete(k)
        elif ch == 5:
            break
        ans = input("\n\t..... Do You Want to Continue in Main Menu:y/n ")
        if ans.lower() != 'y':
            break


if _name_ == "_main_":
    main()