from time import sleep
class attraction:
    def __init__(self,name,capacity):
        self._name = name
        self._capacity = capacity
        self.passengers = []
    def get_details(self):
        print("NAME OF ATTRACTION: ", self._name)
        print("CAPACITY: ", self._capacity)
    def start(self):
        print("...Attraction is starting!")
    
class ThrillRide(attraction):
    def __init__(self,name,capacity,height):
        super().__init__(name,capacity)
        self._height = height
    def start(self):
        print("Passengers of the %s ride: %s" %(self._name,self.passengers))
        sleep(1)
        print("...Thrill ride %s is about to start!" %(self._name))
    def is_el(self,v):
        return True if v._height >= self._height else False


class family(attraction):
    def __init__(self,name,capacity,age):
        super().__init__(name,capacity)
        self._age = age
    def start(self):
        print("Passengers on the %s ride: %s" %(self._name,self.passengers))
        sleep(1)
        print("...Family ride %s is about to start!" %(self._name))
    def is_el(self,v):
        return True if v._age >= self._age else False

class staff:
    def __init__(self,name,role):
        self._name = name
        self._role = role
    def work(self):
        print('Staff %s is performing their role: %s' %(self._name,self._role))
    def summary(self):
        print("------ %s's SUMMARY ------")
        print('NAME: ', self.name)
        print('ROLE: ', self.role)
        print('\n')
        sleep(1)
class Manager(staff):
    def __init__(self,name,team):
        self._name = name
        self._role = 'Manager'
        self._team = team
    def add_staff(self,s):
        self._team.append(s)
    def get_summary_team(self):
        for s in self._team:
            s.summary()
class visitor:
    def __init__(self,name,age,height):
        self._name = name
        self._age = age
        self._height = height
    def ride_attraction(self,att):
        if att.is_el(self):
            att.passengers.append(self._name)
            print("%s is boarding the %s ride!" %(self._name,att._name))
        else:
            print("%s is not eligible to ride the %s" %(self._name,att._name))
dragon = ThrillRide('Dragon Coaster',20,140)
mosquito = ThrillRide("Mosquito's Den",20,160)
round = family('Merry-Go-Round',30,4)
cup = family('Tiny Teacups',15,7)

normal = visitor('Taco',16,166)
normal2 = visitor('Grape',16,170)
child = visitor('Lilo',5,90)

normal.ride_attraction(dragon)
sleep(1)
normal2.ride_attraction(round)
sleep(1)
child.ride_attraction(round)
sleep(1)
child.ride_attraction(cup)
sleep(2)

dragon.start()
sleep(1)
round.start()
sleep(1)
cup.start()
sleep(1)
