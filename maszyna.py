from statemachine import Transition
from klasy import Generator
from automaty.robot import *
from automaty.ladownica import *
from automaty.przybijanie import *

# przykladowy czujnik
czujnik_zszywek = False

# create paths from transitions (exemplary)

path_0 = wsunWozek


paths = [path_0]

# execute paths
for path in paths:

    # create a supervisor
    supervisor_main = Generator.create_master(master_states_main, master_transitions_main)

    for event in path:

        # launch a transition in our supervisor
        master_transitions_main[event]._run(supervisor_main)
        print(supervisor_main.current_state)

        # tutaj sprawdza czy są zszywki jak nie uruchamia automat podrzedny ktory to robi
        if supervisor_main.current_state.value == "robot_gotowy":
            for path_1 in ladujZszywki:
                supervisor_zszywacz = Generator.create_master(master_states_zszywacz, master_transitions_zszywacz)
                for eventx in ladujZszywki:
                    # launch a transition in our supervisor
                    master_transitions_zszywacz[eventx]._run(supervisor_zszywacz)
                    print(supervisor_zszywacz.current_state)
                    print("ZAŁADOWAŁ ZSZYWKI")
