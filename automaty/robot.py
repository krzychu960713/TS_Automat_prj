from statemachine import State, Transition
# define states for a master (way of passing args to class)
options_main = [
    {"name": "Wozek wysuniety", "initial": True, "value": "wozek_wysuniety"},   # 0
    {"name": "Wozek wsuniety", "initial": False, "value": "wozek_wsuniety"},    # 1
    {"name": "Robot pracuje", "initial": False, "value": "robot_pracuje"},   # 2
    {"name": "Pozycja A", "initial": False, "value": "pozycja_a"},   # 3
    {"name": "Pozycja B", "initial": False, "value": "pozycja_b"},   # 4
    {"name": "Alarm A", "initial": False, "value": "alarm_a"},   # 5
    {"name": "Alarm B", "initial": False, "value": "alarm_b"},   # 6
    {"name": "Zlap klocek", "initial": False, "value": "zlap_klocek"},   # 7
    {"name": "Przybij klocek", "initial": False, "value": "przybij_klocek"}]   # 8

# create State objects for a master
# ** -> unpack dict to args
master_states_main = [State(**opt) for opt in options_main]

# valid transitions for a master (indices of states from-to)
form_to_main = [
    [0, [1]],
    [1, [0, 2]],
    [2, [1, 3, 4]],
    [3, [5, 7]],
    [4, [6, 7]],
    [5, [3]],
    [6, [4]],
    [7, [8]],
    [8, [2]]
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
