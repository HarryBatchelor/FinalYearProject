import matplotlib.pyplot as plt
import pandas
from os import listdir
from os.path import isfile, join
from matplotlib.backends.backend_pdf import PdfPages

# time = []
# x = []
# y = []
# z = []

# with open('test.csv', 'r') as File:
#     lines = csv.reader(File, delimiter=',')
#     for row in lines:
#         time.append(row[0])
#         x.append(row[1])
        # y.append(row[2])
        # z.append(row[3])
onlyfiles = [f for f in listdir("CSV/Outputs") if isfile(join("CSV/Outputs", f))]     

for files in onlyfiles:
        with PdfPages('multipage_pdf.pdf') as pdf:
                data = pandas.read_csv()
                plt.plot(data.TIME, data.X, label = "X Coords")
                plt.plot(data.TIME, data.Y, label = "Y Coords")
                plt.plot(data.TIME, data.Z, label = "Z Coords")
                plt.title("Hits on left pole ")
                plt.xlabel("Time")
                plt.ylabel("Acceleration")
                ax = plt.gca()
                ax.axes.xaxis.set_ticks([])
                plt.legend()
                pdf.savefig()
                plt.close()
