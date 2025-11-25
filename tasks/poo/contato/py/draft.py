class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self, number: str) -> str:
        return self.number

    def isValid(self, number: str)-> bool:
        valid_char = "0123456789()"
        for char in number:
            if char not in valid_char:
                return False
            return True
        
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.fones = []
        self.favorited = False

    def addFone(self, id: str, number: str):
        if Fone.isValid(number):
            self.fones.append(Fone(id, number))
        else:
            print("fail: número inválido")


    def __str__(self):
        return f"{self.__name}"
        

def main():
    contact = Contact("")
        
    while True:
        try:
            line = input()
        except EOFError:
            break

        print(f"${line}")
        args = line.split()

        if len(args) == 0:
            continue

        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "init":
            name = args[1]
            contact = Contact(name)

        elif cmd == "show":
            print(contact)


if __name__ == "__main__":
    main()