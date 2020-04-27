from statemachine import State, Transition
# define states for a master (way of passing args to class)
options_main = [
    {"name": "Wozek wysuniety", "initial": True, "value": "wozek_wysuniety"},   # 0
    {"name": "Wozek wsuniety", "initial": False, "value": "wozek_wsuniety"},    # 1
    {"name": "Robot gotowy", "initial": False, "value": "robot_gotowy"}   # 2
]
# create State objects for a master
# ** -> unpack dict to args
master_states_main = [State(**opt) for opt in options_main]

# valid transitions for a master (indices of states from-to)
form_to_main = [
    [0, [1]],
    [1, [0, 2]],
    [2, [0]]
]

# create transitions for a master (as a dict)
master_transitions_main = {}

for indices in form_to_main:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states_main[from_idx], master_states_main[to_idx], identifier=op_identifier)
        master_transitions_main[op_identifier] = transition

        # add transition to source state
        master_states_main[from_idx].transitions.append(transition)

wsunWozek = ["m_0_1", "m_1_2"]    # wsuniecie wozka
wysunWozek = ["m_2_1", "m_1_0"]    # wysuniecie wozka