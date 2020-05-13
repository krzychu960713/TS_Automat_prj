from statemachine import State, Transition
from .tranzycja import *
# define states for a master (way of passing args to class)
options_zszywacz = [
    {"name": "Pozycja arsenal", "initial": True, "value": "pozycja_arsenal"},  # 0
    {"name": "Laduj zszywki", "initial": False, "value": "laduj_zszywki"},  # 1
    {"name": "Alarm zszywki", "initial": False, "value": "alarm_zszywki"}]  # 2

# create State objects for a master
master_states_zszywacz = [State(**opt) for opt in options_zszywacz]

# valid transitions for a master (indices of states from-to)
form_to_zszywacz = [
    [0, [1, 2]],
    [1, [0]],
    [2, [0]]
]

master_states_zszywacz, master_transitions_zszywacz = setTransition(form_to_zszywacz, master_states_zszywacz, 'z')

ladujZszywki = ["z_0_1", "z_1_0"]
ladujZszywkizAlarmem = ["z_0_2", "z_2_0", "z_0_1", "z_1_0"]