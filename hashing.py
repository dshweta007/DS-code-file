class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no, self.name, self.balance = acc_no, name, balance
    def __str__(self):
        return f"{self.acc_no} | {self.name} | Rs.{self.balance}"
 
class ChainingHash:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]
    def h(self, key):
        return key % self.size
    def search(self, key):
        for a in self.table[self.h(key)]:
            if a.acc_no == key:
                return a
        return None
    def insert(self, acc):
        if self.search(acc.acc_no):
            print("Duplicate account number!"); return
        self.table[self.h(acc.acc_no)].append(acc)
    def delete(self, key):
        a = self.search(key)
        if a:
            self.table[self.h(key)].remove(a); return True
        return False
    def display(self):
        for i, chain in enumerate(self.table):
            print(i, "->", " -> ".join(str(a) for a in chain) or "empty")
 
class OpenAddressHash:
    DELETED = object()
    def __init__(self, size=7, mode="linear"):
        self.size, self.mode = size, mode
        self.table = [None] * size
    def probe(self, key, i):
        step = i if self.mode == "linear" else i * i
        return (key % self.size + step) % self.size
    def search(self, key):
        for i in range(self.size):
            slot = self.table[self.probe(key, i)]
            if slot is None:
                return None
            if slot is not self.DELETED and slot.acc_no == key:
                return slot
        return None
    def insert(self, acc):
        if self.search(acc.acc_no):
            print("Duplicate account number!"); return
        for i in range(self.size):
            idx = self.probe(acc.acc_no, i)
            if self.table[idx] is None or self.table[idx] is self.DELETED:
                self.table[idx] = acc; return
        print("Hash table is full / no free slot found!")
    def delete(self, key):
        for i in range(self.size):
            idx = self.probe(key, i)
            slot = self.table[idx]
            if slot is None:
                return False
            if slot is not self.DELETED and slot.acc_no == key:
                self.table[idx] = self.DELETED; return True
        return False
    def display(self):
        for i, s in enumerate(self.table):
            if s is None: print(i, "-> empty")
            elif s is self.DELETED: print(i, "-> deleted")
            else: print(i, "->", s)
 
def main():
    print("1.Chaining  2.Linear Probing  3.Quadratic Probing")
    c = input("Choose method: ")
    ht = ChainingHash(7) if c == "1" else OpenAddressHash(7, "linear" if c == "2" else "quadratic")
    while True:
        print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            ht.insert(Account(int(input("Account No: ")), input("Name: "), float(input("Balance: "))))
        elif ch == "2":
            r = ht.search(int(input("Account No: ")))
            print(r if r else "Record not found")
        elif ch == "3":
            print("Deleted" if ht.delete(int(input("Account No: "))) else "Record not found")
        elif ch == "4":
            ht.display()
        elif ch == "5":
            break
 
main()
