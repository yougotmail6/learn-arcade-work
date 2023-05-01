import Baron
import Gorilla
import Mantis
import Osprey
import random





def main():


    
    ship_list = []

    BARON = Baron
    ship_list.append(BARON)

    gorilla = Gorilla
    ship_list.append(gorilla)

    JFO = Mantis
    ship_list.append(JFO)

    Osp = Osprey
    ship_list.append(Osp)


    print(random.choice(ship_list))
    
    
    



main()