import snap

def load(fname="turb.edgelist"):
    return snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1)

def plot_degrees(net, fname="turb", desc="degrees"):
    snap.PlotInDegDistr(net, fname, desc, False, True)
    snap.PlotOutDegDistr(net, fname, desc, False, True)

if __name__ == "__main__":
    net = load()
    plot_degrees(net)
