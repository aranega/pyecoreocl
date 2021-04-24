from pyecoreocl.compiler import dummy_compiler, OCLTuple
from pyecore.resources import ResourceSet
import pyecore
import cmd

class OCLShell(cmd.Cmd):
    intro = 'OCL Interpreter'
    prompt = '(ocl) '
    file = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rset = ResourceSet()
        self.vars = {
            'rset': self.rset,
            'ecore': pyecore.ecore
        }
        self.gvars = {
            'OCLTuple': OCLTuple
        }
        self.vars['metavars'] = self.vars

    def do_load(self, arg):
        try:
            print(f'!! Loading {arg}')
            res = self.rset.get_resource(arg)
            self.vars['self'] = res.contents[0]
        except Exception as e:
            print(e)

    def do_register(self, arg):
        try:
            print(f'!! Registering {arg}')
            res = self.rset.get_resource(arg)
            root = res.contents[0]
            self.rset.metamodel_registry[root.nsURI] = root
        except Exception as e:
            print(e)

    def do_assign(self, arg):
        try:
            var, expression = arg.split()
            res = self.compile_execute(expression)
            self.vars[var.strip()] = res
        except Exception as e:
            print(e)

    def default(self, line):
        if ':=' in line:
            self.assign(line)
            return
        try:
            print(f"{self.compile_execute(line)!r}")
        except Exception as e:
            print(e)

    def assign(self, arg):
        try:
            var, expression = arg.split(':=')
            res = self.compile_execute(expression)
            self.vars[var.strip()] = res
        except Exception as e:
            print(e)

    def compile_execute(self, line):
        cmd = dummy_compiler(line)
        print(f"!! expr: {cmd}")
        code = compile(f"{cmd}", '<ocl_expr>', 'eval')
        return eval(code, self.gvars, self.vars)

    def do_quit(self, arg):
        print("\n!! Exiting")
        return True

    do_q = do_quit
    do_EOF = do_quit

OCLShell().cmdloop()
