from statemachine import State, Transition
from .tranzycja import *
# define states for a master (way of passing args to class)
options_przybicie = [
    {"name": "Robot pracuje", "initial": True, "value": "robot_pracuje"},  # 0
    {"name": "Pozycja A", "initial": False, "value": "pozycja_a"},   # 1
    {"name": "Pozycja B", "initial": False, "value": "pozycja_b"},   # 2
    {"name": "Alarm A", "initial": False, "value": "alarm_a"},   # 3
    {"name": "Alarm B", "initial": False, "value": "alarm_b"},   # 4
    {"name": "Zlap klocek", "initial": False, "value": "zlap_klocek"},   # 5
    {"name": "Przybij klocek", "initial": False, "value": "przybij_klocek"}]   # 6

# create State objects for a master
# ** -> unpack dict to args
master_states_przybicie = [State(**opt) for opt in options_przybicie]

# valid transitions for a master (indices of states from-to)
form_to_przybicie = [
    [0, [1, 2]],
    [1, [3, 5]],
    [2, [4, 5]],
    [3, [1]],
    [4, [2]],
    [5, [6]],
    [6, [0]],
]

master_states_przybicie, master_transitions_przybicie = setTransition(form_to_przybicie, master_states_przybicie, 'p')

przybijKlocekA = ["p_0_1", "p_1_5", "p_5_6", "p_6_0"]    # przybicie klocka A
przybijKlocekAzAlarmem = ["p_0_1", "p_1_3", "p_3_1", "p_1_5", "p_5_6", "p_6_0"]  # przybicie klocka A z alarmem

przybijKlocekB = ["p_0_2", "p_2_5", "p_5_6", "p_6_0"]    # przybicie klocka B
przybijKlocekBzAlarmem = ["p_0_2", "p_2_4", "p_4_2", "p_2_5", "p_5_6", "p_6_0"]  # przybicie klocka B z alarmem