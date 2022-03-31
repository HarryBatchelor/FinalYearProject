import csv
import re



inp_file = "HitsLeft.csv"
out_file_pattern_Left = "Left_{:{fill}2}.csv"
    # edit depending on SQL limit
max_rows = 141

with open(inp_file, "r") as inp_f:
    reader = csv.reader(inp_f)

    all_rows = []
    cur_file = 1

    

    for row in reader:
        all_rows.append(row)

        patn = re.sub(r"/[(,)']/g","", all_rows) 
        # DOESNT WORK ^

        if len(patn) == max_rows:
            with open(out_file_pattern_Left.format(cur_file, fill="0"), "w") as out_f:
                writer = csv.writer(out_f)
                writer.writerows(patn)
            all_rows = []
            cur_file +=1