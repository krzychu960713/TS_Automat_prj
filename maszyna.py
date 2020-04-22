from statemachine import StateMachine, State, Transition

# define states for a master (way of passing args to class)
options = [
    {"name": "Wozek wysuniety", "initial": True, "value": "wozek_wysuniety"},   # 0
    {"name": "Wozek wsuniety", "initial": False, "value": "wozek_wsuniety"},    # 1
    {"name": "Robot pracuje", "initial": False, "value": "robot_pracuje"},   # 2
    {"name": "Pozycja A", "initial": False, "value": "pozycja_a"},   # 3
    {"name": "Pozycja B", "initial": False, "value": "pozycja_b"},   # 4
    {"name": "Alarm A", "initial": False, "value": "alarm_a"},   # 5
    {"name": "Alarm B", "initial": False, "value": "alarm_b"},   # 6
    {"name": "Zlap klocek", "initial": False, "value": "zlap_klocek"},   # 7
    {"name": "Przybij klocek", "initial": False, "value": "przybij_klocek"},   # 8
    {"name": "Pozycja arsenal", "initial": False, "value": "pozycja_arsenal"},   # 9
    {"name": "Laduj zszywki", "initial": False, "value": "laduj_zszywki"},   # 10
    {"name": "Alarm zszywki", "initial": False, "value": "alarm_zszywki"}]   # 11


# create State objects for a master
# ** -> unpack dict to args
master_states = [State(**opt) for opt in options]

# valid transitions for a master (indices of states from-to)
form_to = [
    [0, [1]],
    [1, [0, 2]],
    [2, [1, 3, 4, 9]],
    [3, [5, 7]],
    [4, [6, 7]],
    [5, [3]],
    [6, [4]],
    [7, [8]],
    [8, [2]],
    [9, [10, 11]],
    [10, [2]],
    [11, [9]],
]

# create transitions for a master (as a dict)
master_transitions = {}
for indices in form_to:
    from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
    for to_idx in to_idx_tuple:  # iterate over destinations from a source state
        op_identifier = "m_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

        # create transition object and add it to the master_transitions dict
        transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
        master_transitions[op_identifier] = transition

        # add transition to source state
        master_states[from_idx].transitions.append(transition)


# create a generator class
class Generator(StateMachine):
    states = []
    transitions = []
    states_map = {}
    current_state = None

    def __init__(self, states, transitions):

        # creating each new object needs clearing its variables (otherwise they're duplicated)
        self.states = []
        self.transitions = []
        self.states_map = {}
        self.current_state = states[0]

        # create fields of states and transitions using setattr()
        # create lists of states and transitions
        # create states map - needed by StateMachine to map states and its values
        for s in states:
            setattr(self, str(s.name).lower(), s)
            self.states.append(s)
            self.states_map[s.value] = str(s.name)

        for key in transitions:
            setattr(self, str(transitions[key].identifier).lower(), transitions[key])
            self.transitions.append(transitions[key])

        # super() - allows us to use methods of StateMachine in our Generator object
        super(Generator, self).__init__()

    # define a printable introduction of a class
    def __repr__(self):
        return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
            type(self).__name__, self.model, self.state_field,
            self.current_state.identifier,
        )

    # method of creating objects in a flexible way (we can define multiple functions
    # which will create objects in different ways)
    @classmethod
    def create_master(cls, states, transitions) -> 'Generator':
        return cls(states, transitions)


# create paths from transitions (exemplary)
path_0 = ["m_0_1", "m_1_2"]    # wsuniecie wozka
path_1 = ["m_2_1", "m_1_0"]    # wysuniecie wozka

path_2 = path_0 + ["m_2_3", "m_3_7", "m_7_8", "m_8_2"]    # przybicie klocka A
path_3 = path_0 + ["m_2_3", "m_3_5", "m_5_3", "m_3_7", "m_7_8", "m_8_2"] + path_1    # przybicie klocka A z alarmem
path_4 = path_0 + ["m_2_4", "m_4_7", "m_7_8", "m_8_2"]    # przybicie klocka B
path_5 = path_0 + ["m_2_4", "m_4_6", "m_6_4", "m_4_7", "m_7_8", "m_8_2"]    # przybicie klocka B z alarmem
path_6 = path_0 + ["m_2_9", "m_9_10", "m_10_2"]    # ladowanie zszywek
path_7 = path_0 + ["m_2_9", "m_9_11", "m_11_9", "m_9_10", "m_10_2"]  # ladowanie z alarmem


paths = [path_0, path_2, path_3, path_4, path_5, path_6, path_7]


# execute paths
for path in paths:

    # create a supervisor
    supervisor = Generator.create_master(master_states, master_transitions)
    print('\n' + str(supervisor))

    # run supervisor for exemplary path
    print("Executing path: {}".format(path))
    for event in path:

        # launch a transition in our supervisor
        master_transitions[event]._run(supervisor)
        print(supervisor.current_state)

        # add slave
        if supervisor.current_state.value == "alarm_a":
            # TODO: automata 1 (for) slave1
            print("Stachu przynies klockow A")
            ...

        if supervisor.current_state.value == "alarm_b":
            # TODO: automata 2 (for) slave2
            print("Staszek przynies klockow B")
            ...

        if supervisor.current_state.value == "alarm_zszywki":
            # TODO: automata 3 (for) slave3
            print("Jerzy załaduj proce")
            ...

        if supervisor.current_state.value == "wozek_wysuniety":
            # TODO: automata 3 (for) slave3
            print("Jan ciag za wajche")
            ...
