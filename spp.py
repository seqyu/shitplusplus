class shitInterpreter:
    def __init__(self):
        self.vars = {}

    def parse_line(self, line):
        line = line.split("#")[0].strip()
        if not line:
            return None

        if line.startswith("$"):
            self.assign(line)
        elif line.startswith("??"):
            self.if_condition(line)
        elif line.startswith("!!"):
            self.shout_value(line)
        else:
            raise SyntaxError("WHAT THE FUCK IS THIS????!!!")

    def assign(self, line):
        try:
            parts = line.split(" ", 2) 
            if len(parts) < 3:
                raise ValueError("Incomplete nonsense detected. Here are some tips: This is 100% your fault, so just write better code.")

            _, var, val = parts

            if val.isdigit():
                val = int(val)
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            else:
                raise ValueError("What kind of fucking value is this bruh")

            self.vars[var] = val
        except Exception as e:
            raise SyntaxError(f"Assignment failed. Are you even fucking trying? Error: {e}")

    def if_condition(self, line):
        try:
            parts = line.split(" ", 4)  
            if len(parts) < 5:
                raise ValueError("What kind of condition is this shit?")

            _, var, cond, val, code = parts

            if cond != "<>":
                raise ValueError("Condition operator not cool enough.")

            if self.vars.get(var) != int(val):
                self.execute(code)
        except Exception as e:
            raise SyntaxError(f"Conditional failed. You're ass at this. Error: {e}")

    def shout_value(self, line):
        try:
            parts = line.split(" ", 1)
            if len(parts) < 2:
                raise ValueError("What do you even want me to print?")

            _, var = parts
            print(self.vars.get(var, "?????"))
        except Exception as e:
            raise SyntaxError(f"Couldn't shout. Sad. >n< Error: {e}")

    def execute(self, code):
        lines = code.split("\n")
        for line in lines:
            line = line.strip()
            if line:
                try:
                    self.parse_line(line)
                except Exception as e:
                    print(f"Error processing line: {line}\n{e}")

    def execute_file(self, filename):
        try:
            with open(filename, 'r') as f:
                code = f.read()
                self.execute(code)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Great job you also suck at trying to execute a file.")
        except Exception as e:
            print(f"Error: {e}. Maybe it's time to rethink your life choices.")

if __name__ == "__main__":
    import sys

    interpreter = shitInterpreter()

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        interpreter.execute_file(filename)
    else:
        while True:
            try:
                user_input = input("Shit++> ")
                if user_input.lower() == "exit":
                    print("You're a failure :3")
                    break
                interpreter.execute(user_input)
            except Exception as e:
                print(f"Error: {e}\nHere are some tips: This is 100% your fault, just write better code.")
