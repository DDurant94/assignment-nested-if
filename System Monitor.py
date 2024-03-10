'''
5. The Silent Logger: System Monitor 🖥️
Objective:

To practice the use of the pass statement in a system monitoring context.

Task 1: Code Correction

You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.

Buggy Code:

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90
    pass
Task 2: System Check

Based on the corrected code from Task 1, enhance the program to also monitor memory usage and disk space, and provide alerts accordingly.

Task 3: Alert System

If any of the system parameters exceed a certain threshold, print an alert message. However, if the system parameter is within a "gray zone", use the pass statement to silently log this without alerting the user.
'''
# Task one

'''
import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
  pass
'''

# Task two
'''
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0,100)
disk_space = random.randint(0,100)
if cpu_usage > 90:
    print("High CPU usage!", cpu_usage,"%", "Is being used!")
elif cpu_usage > 80 and cpu_usage <= 90:
  print("High CPU usage!", cpu_usage,"%", "Is being used!")
elif cpu_usage > 30 and cpu_usage <=79:
   print("CPU usage is",cpu_usage,"%!")
else:
   print("CPU usage is",cpu_usage,"%!")
   pass

if memory_usage > 90:
   print("Memory low!",memory_usage,"%", "used!")
elif memory_usage > 70 and memory_usage <= 89:
   print("Memory low!",memory_usage,"%", "used!")
elif memory_usage > 30 and memory_usage <= 69:
   print(memory_usage,"%", "Memory used!")
else:
   print(memory_usage,"%", "Memory used!")

if disk_space > 90:
   print("Hard Disk space low!", (100 - disk_space),"%", "Hard Disk space left!")
elif disk_space > 70 and disk_space <=89:
   print("Hard Disk space low!", (100 - disk_space),"%", "Hard Disk space left!")
elif disk_space > 30 and disk_space <= 69:
   print(disk_space,"%", "Hard Disk space used!")
else:
  print(disk_space,"%", "Hard Disk space used!")

  '''

# Task three.
import random as r 


cpu_usage = r.randint(0, 100)
memory_usage = r.randint(0,100)
disk_space = r.randint(0,100)

if cpu_usage > 90:
    print("High CPU usage!", cpu_usage,"%", "Is being used!")
elif cpu_usage > 80 and cpu_usage <= 90:
  print("High CPU usage!", cpu_usage,"%", "Is being used!")
elif cpu_usage > 30 and cpu_usage <=79:
   pass
else:
   pass

if memory_usage > 90:
   print("Memory low!",memory_usage,"%", "used!")
elif memory_usage > 70 and memory_usage <= 89:
   print("Memory low!",memory_usage,"%", "used!")
elif memory_usage > 30 and memory_usage <= 69:
   pass
else:
   pass

if disk_space > 90:
   print("Hard Disk space low!", (100 - disk_space),"%", "Hard Disk space left!")
elif disk_space > 70 and disk_space <=89:
   print("Hard Disk space low!", (100 - disk_space),"%", "Hard Disk space left!")
elif disk_space > 30 and disk_space <= 69:
   pass
else:
   pass