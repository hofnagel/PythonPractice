with open("st.txt", "w") as f:
	f.write("Hi From Python!") # with open automatically closes the st.txt file after f.write command executes.

import csv

with open("st.csv", "w") as f:
          w=csv.writer(f,
                       delimiter=",")
          w.writerow(["one",
                      "two",
                      "three"])
          w.writerow(["four",
                      "five",
                      "six"])

import csv

with open("st.csv", "r") as f:
    r=csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
