import sys
import datum

date = datum.datetime()

print("Python",sys.version,"on",sys.platform,)
print("\n" + date[0])
print("\nHeute ist {}, der {}. {} {}.".format(date[1], date[2], date[3], date[4]), end=" ")
print("Es ist {:02d}:{:02d}:{:02d}.".format(date[5], date[6], date[7]))

