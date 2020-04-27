from statemachine import Transition
from klasy import Generator
from automaty.robot import *
from automaty.ladownica import *

# przykladowy czujnik
czujnik_zszywek = False

# create paths from transitions (exemplary)
wsunWozek = ["m_0_1", "m_1_2"]    # wsuniecie wozka
wysunWozek = ["m_2_1", "m_1_0"]    # wysuniecie wozka

przybijKlocekA = ["m_2_3", "m_3_7", "m_7_8", "m_8_2"]    # przybicie klocka A
przybijKlocekAzAlarmem = ["m_2_3", "m_3_5", "m_5_3", "m_3_7", "m_7_8", "m_8_2"]  # przybicie klocka A z alarmem
przybijKlocekB = ["m_2_4", "m_4_7", "m_7_8", "m_8_2"]    # przybicie klocka B
przybijKlocekBzAlarmem = ["m_2_4", "m_4_6", "m_6_4", "m_4_7", "m_7_8", "m_8_2"]    # przybicie klocka B z alarmem

path_0 = wsunWozek + przybijKlocekA + przybijKlocekBzAlarmem + wysunWozek
path_1 = wsunWozek + przybijKlocekA + przybijKlocekA + przybijKlocekA + wysunWozek
path_2 = wsunWozek + przybijKlocekAzAlarmem + przybijKlocekBzAlarmem + przybijKlocekA + wysunWozek

paths = [path_0, path_1, path_2]

ladujZszywki = ["z_0_1"]
ladujZszywkizAlarmem = ["z_0_2", "z_2_0", "z_0_1"]

# execute paths
for path in paths:

    # create a supervisor
    supervisor_main = Generator.create_master(master_states_main, master_transitions_main)

    for event in path:

        # launch a transition in our supervisor
        master_transitions_main[event]._run(supervisor_main)
        print(supervisor_main.current_state)

        # tutaj sprawdza czy są zszywki jak nie uruchamia automat podrzedny ktory to robi
        if supervisor_main.current_state.value == "robot_pracuje":
            if not czujnik_zszywek:
                supervisor_zszywacz = Generator.create_master(master_states_zszywacz, master_transitions_zszywacz)
                for eventx in ladujZszywki:
                    # launch a transition in our supervisor
                    master_transitions_zszywacz[eventx]._run(supervisor_zszywacz)
                    print(supervisor_zszywacz.current_state)
                    print("ZAŁADOWAŁ ZSZYWKI")
