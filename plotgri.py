import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------
def readgri(fname):
    f = open(fname, 'r')
    Nn, Ne, dim = [int(s) for s in f.readline().split()]
    # read vertices
    V = np.array([[float(s) for s in f.readline().split()] for n in range(Nn)])
    # read boundaries
    NB = int(f.readline())
    B = [];
    Bname = []
    for i in range(NB):
        s = f.readline().split();
        Nb = int(s[0]);
        Bname.append(s[2])
        Bi = np.array([[int(s) - 1 for s in f.readline().split()] for n in range(Nb)])
        B.append(Bi)
    # read elements
    Ne0 = 0;
    E = []
    while (Ne0 < Ne):
        s = f.readline().split();
        ne = int(s[0])
        Ei = np.array([[int(s) - 1 for s in f.readline().split()] for n in range(ne)])
        E = Ei if (Ne0 == 0) else np.concatenate((E, Ei), axis=0)
        Ne0 += ne
    f.close()
    Mesh = {'V': V, 'E': E, 'B': B, 'Bname': Bname}
    return Mesh


# -----------------------------------------------------------
def plotmesh(Mesh, fname):
    V = Mesh['V'];
    E = Mesh['E'];
    f = plt.figure(figsize=(12, 12))
    # plt.tripcolor(V[:,0], V[:,1], triangles=E)
    plt.triplot(V[:, 0], V[:, 1], E, 'k-')
    plt.scatter(V[:, 0], V[:, 1], c='red', marker='o', s=2)
    dosave = not not fname
    plt.axis('equal')
    plt.tick_params(axis='both', labelsize=12)
    f.tight_layout();
    plt.show(block=(not dosave))
    if (dosave): plt.savefig(fname)
    plt.close(f)


# -----------------------------------------------------------
def main():
    #plotmesh(readgri('test.gri'), [])
    #plotmesh(readgri('all.gri'), []);
    #plotmesh(readgri('localRefinedAllTrail.gri'), []);
    plotmesh(readgri('localSmoothedAllTrail.gri'), []);
    plotmesh(readgri('localRefinedAll.gri'), []);
    plotmesh(readgri('localSmoothedAll.gri'), []);
    #plotmesh(readgri('shitSmoothed.gri'), []);
    plotmesh(readgri('uniformRefinedAll.gri'), []);


if __name__ == "__main__":
    main()
