from statemachine import State, Transition
from .tranzycja import *
# define states for a master (way of passing args to class)
options_main = [
    {"name": "Wozek wysuniety", "initial": True, "value": "wozek_wysuniety"},   # 0
    {"name": "Wozek wsuniety", "initial": False, "value": "wozek_wsuniety"},    # 1
    {"name": "Robot gotowy", "initial": False, "value": "robot_gotowy"},   # 2
    {"name": "ladowanie", "initial": False, "value": "ladowanie"},   # 3
    {"name": "przybijanie", "initial": False, "value": "przybijanie"}   # 4
]
# create State objects for a master
# ** -> unpack dict to args
master_states_main = [State(**opt) for opt in options_main]

# valid transitions for a master (indices of states from-to)
form_to_main = [
    [0, [1]],
    [1, [0, 2]],
    [2, [1, 3, 4]],
    [3, [2]],
    [4, [2]]
]

master_states_main, master_transitions_main = setTransition(form_to_main, master_states_main, 'm')

wsunWozek = ["m_0_1", "m_1_2"]    # wsuniecie wozka
wysunWozek = ["m_2_1", "m_1_0"]    # wysuniecie wozka
ladowanie_start = ["m_2_3"]         # rozpoczęcie ładowania
ladowanie_end = ["m_3_2"]         # zakończenie ładowania
przybijanie_start = ["m_2_4"]         # rozpoczęcie przybijania
przybijanie_end = ["m_4_2"]         # zakończenie przybijania
