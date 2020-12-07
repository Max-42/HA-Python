import random
import time
def main():
    liste = ["",
             "Sehr gut!",
             "gut",
             "befridigend",
             "ausreichend",
             "mangelhaft",
             "ungenügend",]
    note = random.randint(1,6)
    print (liste[note])
    time.sleep(0.5)
    main()
main()

