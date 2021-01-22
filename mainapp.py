import ui
from store import Store
from person import Person

class MainApp(object):
    def __init__(self):
        self.__isRunning = True
        self.__curStep = 0
        self.__curInput = None
        self.__steps = ui.Steps()
        self.__phoneBook = []
        self.__store = Store()

    def run(self):
        # inint store
        self.__phoneBook = self.__store.readStore()
        # start steps
        while(self.__isRunning):
            self.__steps.getStep(self.__curStep)
            self.inputParse()
        print('Thank you for using our app!')

    def stop(self):
        self.__isRunning = False
    
    def printPhoneBook(self):
        for person in self.__phoneBook:
            print(person)
            print('')
    
    def searchPerson(self, sample):
        result = []
        for person in self.__phoneBook:
            if ((sample.lower() in person.name.lower()) or
                (sample.lower() in person.phone.lower())):
                result.append(person)
        return result
    
    def createPerson(self):
        result = Person('noname', '', '', '')
        tmpVal = input('Name: ')
        if (tmpVal.lower() in ['exit', '0']):
            return tmpVal
        else:
            result.name = tmpVal
        tmpVal = input('Phone: ')
        if (tmpVal.lower() in ['exit', '0']):
            return tmpVal
        else:
            result.phone = tmpVal
        tmpVal = input('Email: ')
        if (tmpVal.lower() in ['exit', '0']):
            return tmpVal
        else:
            result.email = tmpVal
        tmpVal = input('Info: ')
        if (tmpVal.lower() in ['exit', '0']):
            return tmpVal
        else:
            result.email = tmpVal
        self.__phoneBook.append(result)
        self.__store.writeStore(self.__phoneBook)
        return result

    def inputParse(self):
        if (self.__curStep == 0):
            self.__curInput = input('Make your choise: ')
            if (self.__curInput.lower() == 'exit'):
                self.stop()
            if (self.__curInput in ['1', '2', '3']):
                self.__curStep = int(self.__curInput)
        elif (self.__curStep == 1):
            self.__curInput = input('Make your choise: ')
            if (self.__curInput.lower() == 'exit'):
                self.stop()
            elif (self.__curInput in ['0']):
                self.__curStep = int(self.__curInput)
            else:
                result = self.searchPerson(self.__curInput)
                for person in result:
                    print(person)
                    print('\n')
        elif (self.__curStep == 2):
            self.__curInput = self.createPerson()
            if (self.__curInput.lower() == 'exit'):
                self.stop()
            elif (self.__curInput in ['0']):
                self.__curStep = int(self.__curInput)
            else:
                print(self.__curInput)
        elif (self.__curStep == 3):
            self.printPhoneBook()
            self.__curInput = input('Make your choise: ')
            if (self.__curInput.lower() == 'exit'):
                self.stop()
            if (self.__curInput in ['0']):
                self.__curStep = int(self.__curInput)
       