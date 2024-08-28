import sys
try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")

print("here are all the valid tags:\n")

valid_tags = ('SYNC', 'stdin', 'BUILTIN', 'STRING', 'console', 'COMMENT', 'stdout',
              'TODO','stderr', 'hit', 'DEFINITION', 'KEYWORD', 'ERROR', 'sel')

for tag in valid_tags:
    shell.write(tag+"\n",tag)


t="ksn skfj"
for a in range(len(t)):
    shell.write(t[a],"ERROR")

shell.write("Wanna go explore? ","KEYWORD")
shell.write("OPTIONS","STRING")
shell.write(" : ","KEYWORD")
shell.write("Yes","DEFINITION")
shell.write(" or ","KEYWORD")
shell.write("No","COMMENT")

