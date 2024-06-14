import re
import random
import turtle
from tkinter import messagebox




class LSystem:
    def __init__(self, t, axiom, length, angle):

        self.state = axiom
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.regex_keys = []
        self.operation_functions = {}
        self.stop_generate = 0


    def add_rules(self, *rules):

        for rule in rules:
            key, value = rule[:2]
            probability = rule[2] if len(rule) == 3 else 1

            key_re = re.escape(key)

            if not isinstance(value, str):
                print("key_re1", key_re)
                key_re = re.sub(r"([a-z]+)([, ]*)",
                                lambda m: r"([-+]?\b\d+(?:\.\d+)?\b)" + m.group(2), key_re)

                self.regex_keys.append(key_re)
                print("self.regex_keys", self.regex_keys)
                print("key_re2", key_re)

            self.rules.setdefault(key, []).append((value, key_re, probability))

            print("self.rules", self.rules)

    def stochastic_lsys(self, rules):

        random_prob = random.random()
        total_prob = 0


        for rule in rules:
            total_prob += rule[2]
            if random_prob < total_prob:
                return rule

        return rules[0]

    def update_state_by_rules(self, match):

        if not self.current_rules:
            return ""

        selected_rule = self.current_rules[0] if len(self.current_rules) == 1 else self.stochastic_lsys(
            self.current_rules)

        if isinstance(selected_rule[0], str):
            return selected_rule[0].lower()
        else:
            args = list(map(float, match.groups()))
            print(args)
            parametric_result = selected_rule[0](*args)
            return parametric_result.lower()

    def process_iterations(self, num_iterations):

        for iteration in range(num_iterations):
            if len(self.state) > 500000:
                self.stop_generate = 1
                return

            for key, rules in self.rules.items():
                self.current_rules = rules
                self.state = re.sub(rules[0][1], self.update_state_by_rules, self.state)
                self.current_rules = None

            self.state = self.state.upper()

    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def add_rules_move(self, *moves):
        for key, func in moves:
            self.operation_functions[key] = func



    def execute_command(self, cmd, args, factor):

        if any(char in cmd for char in ['F', 'H', 'G']):

            factor = self.execute_forward_command(cmd[0], args, factor)

        elif 'S' in cmd:
            self.execute_up_and_forward_command(args)
        elif any(char in cmd for char in ['+', '-']):
            self.execute_turn_command(cmd[0], args)
        elif any(char in cmd for char in ['A', 'L', 'Z', 'I', 'U']):
            self.execute_custom_command(cmd[0], args)
        elif '[' in cmd:

            self.push_turtle_state_to_stack()
        elif ']' in cmd:
            factor = 0
            self.pop_turtle_state_from_stack()
        return factor

    def draw_plant(self, start_pos, start_angle):

        self.t.clear()
        self.turtle_stack = []
        if self.stop_generate == 1:
            messagebox.showerror("Ошибка", "Выбрано слишком большое поколение фрактала!")
            return
        self.t.screen.tracer(0, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()


        key_list_re = "|".join(self.regex_keys)
        factor = 1
        for values in re.finditer(r"(" + key_list_re + r"|.)", self.state):

            cmd = values.group(0)
            #print(cmd)
            args = [float(x) for x in values.groups()[1:] if x]
            factor = self.execute_command(cmd , args, factor)


    def execute_forward_command(self, cmd, args, factor):
        if len(args) > 0 and self.operation_functions.get(cmd):
            factor += 12
            self.operation_functions[cmd](self.t, self.length, *args, factor=factor)

        else:
            self.t.fd(self.length)
        return factor

    def execute_up_and_forward_command(self, args):

        if len(args) > 0 and self.operation_functions.get('S'):
            self.operation_functions['S'](self.t, self.length, *args)
        else:
            self.t.up()
            self.t.forward(self.length)
            self.t.down()

    def execute_turn_command(self, cmd, args):
        if len(args) > 0 and self.operation_functions.get(cmd):
            self.operation_functions[cmd](self.t, self.angle, *args)
        else:
            if cmd == '+':
                self.t.left(self.angle)
            elif cmd == '-':
                self.t.right(self.angle)

    def execute_custom_command(self, cmd, args):
        if self.operation_functions.get(cmd):
            self.operation_functions[cmd](self.t, self.length, *args)

    def push_turtle_state_to_stack(self):
        self.turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))

    def pop_turtle_state_from_stack(self):
        if self.turtle_stack:
            xcor, ycor, head, w = self.turtle_stack.pop()
            self.set_turtle((xcor, ycor, head))
            self.width = w
            self.t.pensize(w)