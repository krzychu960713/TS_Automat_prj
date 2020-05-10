from statemachine import Transition
from klasy import Generator
from automaty.robot import *
from automaty.ladownica import *
from automaty.przybijanie import *
from robo.robotFunction import *

import robopy.base.model as robot

model = robot.Puma560()

# create paths from transitions (exemplary)
path_0 = wsunWozek + wysunWozek
paths = [path_0]

path0_przybijanie = [przybijKlocekAzAlarmem, przybijKlocekA]
path1_przybijanie = [przybijKlocekA, przybijKlocekB, przybijKlocekA]
path2_przybijanie = [przybijKlocekB, przybijKlocekBzAlarmem, przybijKlocekA]
paths_przybijanie = path0_przybijanie + path1_przybijanie + path2_przybijanie

robotPath = []
start, robotPath = init(model, robotPath)

# execute paths
for path in paths:

    # create a supervisor
    supervisor_main = Generator.create_master(master_states_main, master_transitions_main)

    for event in path:

        # launch a transition in our supervisor
        master_transitions_main[event]._run(supervisor_main)
        print(supervisor_main.current_state)

        if supervisor_main.current_state.value == "robot_gotowy":
            for path_p in paths_przybijanie:
                supervisor_przybijanie = Generator.create_master(master_states_przybicie, master_transitions_przybicie)
                for event_p in path_p:
                    master_transitions_przybicie[event_p]._run(supervisor_przybijanie)
                    print(supervisor_przybijanie.current_state)
                print('Klocek przybity')

            supervisor_zszywacz = Generator.create_master(master_states_zszywacz, master_transitions_zszywacz)
            for event_z in ladujZszywki:
                master_transitions_zszywacz[event_z]._run(supervisor_zszywacz)
                print(supervisor_zszywacz.current_state)
                print("ZAŁADOWAŁ ZSZYWKI")

model.animate(stances=robotPath, frame_rate=30, unit='deg')