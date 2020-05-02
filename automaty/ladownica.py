from statemachine import State, Transition
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

# create transitions for a master (as a dict)
master_transitions_zszywacz = {}

for indices in form_to_zszywacz:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "z_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states_zszywacz[from_idx], master_states_zszywacz[to_idx], identifier=op_identifier)
        master_transitions_zszywacz[op_identifier] = transition

        # add transition to source state
        master_states_zszywacz[from_idx].transitions.append(transition)

ladujZszywki = ["z_0_1", "z_1_0"]
ladujZszywkizAlarmem = ["z_0_2", "z_2_0", "z_0_1", "z_1_0"]