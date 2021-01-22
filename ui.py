class Steps(object):
    def __init__(self):
        self.__steps = [
            {
                'stepName': 'Main menu',
                'stepContent': '1. To find person type 1 and press Enter\n' +
                            '2. To create new person type 2 and press Enter\n' +
                            '3. To  get all phonebook type 3 and press Enter\n' +
                            '4. To exit the programm type exit and press Enter'
            },
            {
                'stepName': 'Find a person',
                'stepContent': '1. To find a person type part of a number or name and press Enter\n'
                            '2. To get back to main menu type 0 and press Enter\n' +
                            '3. To exit the programm type exit and press Enter'
            },
            {
                'stepName': 'Create new person',
                'stepContent': '1. To get back to main menu type 0 and press Enter\n' +
                            '2. To exit the programm type exit and press Enter'

            },
            {
                'stepName': 'PhoneBook',
                'stepContent': '1. To get back to main menu type 0 and press Enter\n' +
                            '2. To exit the programm type exit and press Enter'
            }
        ]
    
    def getStep(self, num):
        print(self.__steps[num]['stepName'])
        print(self.__steps[num]['stepContent'])
