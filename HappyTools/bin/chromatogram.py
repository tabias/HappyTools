from HappyTools.bin.trace import Trace
from os import path


class Chromatogram(object):
    def __init__(self, filename):
        self.filename = filename
        self.trace = Trace(self)
        self.trace.open_chrom(self)
        #self.data = Trace(self).open_chrom(self)

    def plot_data(self, master):
        master.fig.clear()
        axes = master.fig.add_subplot(111)
        for i in master.data:
            x_array = []
            y_array = []
            for j in i.data:
                x_array.append(j[0])
                y_array.append(j[1])
            label = path.splitext(path.basename(i.filename))[0]
            axes.plot(x_array, y_array, label=str(label))
        axes.set_xlabel("Time [m]")
        axes.set_ylabel("Intensity [au]")
        handles, labels = axes.get_legend_handles_labels()
        master.fig.legend(handles, labels)
        axes.get_xaxis().get_major_formatter().set_useOffset(False)
        master.canvas.draw()

    def plot_data_new(self, master):
        master.fig.clear()
        axes = master.fig.add_subplot(111)
        for i in master.data:
            x_array = []
            y_array = []
            for j in i.trace.chrom_data:
                x_array.append(j[0])
                y_array.append(j[1])
            label = path.splitext(path.basename(i.filename))[0]
            axes.plot(x_array, y_array, label=str(label))
        axes.set_xlabel("Time [m]")
        axes.set_ylabel("Intensity [au]")
        handles, labels = axes.get_legend_handles_labels()
        master.fig.legend(handles, labels)
        axes.get_xaxis().get_major_formatter().set_useOffset(False)
        master.canvas.draw()
