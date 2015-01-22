import snap

def load(fname="turb.edgelist"):
    return snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1)

if __name__ == "__main__":
    net = load()

