class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number

    @staticmethod
    def isValid(number: str)-> bool:
        valid_char = "0123456789()."
        for char in number:
            if char not in valid_char:
                return False
        return True
        
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones = []
        self.__favorited = False

    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str):
        self.__name = name

    def getFones(self) -> list:
        return self.__fones
    
    def isFavorited(self) -> bool:
        return self.__favorited

    def addFone(self, id: str, number: str):
        if Fone.isValid(number):
            self.__fones.append(Fone(id, number))
        else:
            print("fail: invalid number")

    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            del self.__fones[index]
        else:
            print(f"fail: indice {index} nao existe")

    def toogleFavorited(self):
        self.__favorited = not self.__favorited

    def __str__(self):
        prefix = "@" if self.__favorited else "-"

        fones_str = []
        for fone in self.__fones:
            fones_str.append(str(fone))
        
        joined_fones = ", ".join(fones_str)

        return f"{prefix} {self.__name} [{joined_fones}]"
        

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

        elif cmd == "add":
            label = args[1]
            number = args[2]
            contact.addFone(label, number)

        elif cmd == "rm":
            index = int(args[1])
            contact.rmFone(index)

        elif cmd == "tfav":
            contact.toogleFavorited()


if __name__ == "__main__":
    main()