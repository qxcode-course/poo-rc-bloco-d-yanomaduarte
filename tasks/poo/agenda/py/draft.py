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
    
class Agenda:
    def __init__(self):
        self.__contacts = []

    def __findPosByName(self, name: str) -> int:
        for i, contact in enumerate(self.__contacts):
            if contact.getName() == name:
                return i
        return -1
    
    def addContact(self, name: str, fones: list):
        pos = self.__findPosByName(name)

        if pos != -1:
            contact = self.__contacts[pos]
        else:
            contact = Contact(name)
            self.__contacts.append(contact)
            self.__contacts.sort(key=lambda c: c.getName())

        for fone in fones:
            contact.addFone(fone.getId(), fone.getNumber())

    def rmContact(self, name: str):
        pos = self.__findPosByName(name)
        if pos != -1:
            del self.__contacts[pos]
        else:
            print("fail: contact not found")

    def getContact(self, name: str):
        pos = self.__findPosByName(name)
        if pos != -1:
            return self.__contacts[pos]
        return None
    
    def search(self, pattern: str) -> list:
        results = []
        for contact in self.__contacts:
            if pattern in contact.getName():
                results.append(contact)
                continue

            for fone in contact.getFones():
                if pattern in str(fone):
                    results.append(contact)
                    break
        return results 
    
    def getFavorited(self) -> list:
        favorited = []
        for contact in self.__contacts:
            if contact.isFavorited():
                favorited.append(contact)
        return favorited

    def getContacts(self) -> list:
        return self.__contacts   


    def __str__(self):
        lines = []
        for contact in self.__contacts:
            lines.append(str(contact))
        return "\n".join(lines)

        
        

def main():
    agenda = Agenda()
        
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

        elif cmd == "add":
            name = args[1]
            fones_temp = []
            for token in args[2:]:
                parts = token.split(":")
                fones_temp.append(Fone(parts[0], parts[1]))
            agenda.addContact(name, fones_temp)
        
        elif cmd == "rm":
            name = args[1]
            agenda.rmContact(name)

        elif cmd == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            if contact is not None:
                contact.rmFone(index)
            else:
                print("fail: contato não encontrado")

        elif cmd == "show":
            print(agenda)

        elif cmd == "tfav":
            name = args[1]
            contact = agenda.getContact(name)
            if contact is not None:
                contact.toogleFavorited()
            else:
                print("fail: contato não encontrado")

        elif cmd == "favs":
            favs = agenda.getFavorited()
            for c in favs:
                print(c)

        elif cmd == "search":
            pattern = args[1]
            results = agenda.search(pattern)
            for c in results:
                print(c)

if __name__ == "__main__":
    main()