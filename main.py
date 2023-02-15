import numpy as np
from txt2geo import txt2geo
from msh2gri import msh2gri
from matricesGenerator import I2E


def main():
    # Open the input .txt file and read the node coordinates
    main = np.loadtxt('main.txt')
    flap = np.loadtxt('flap.txt')
    slat = np.loadtxt('slat.txt')

    # convert geometries .txt to .geo
    txt2geo(main, flap, slat)
    # after generating mesh file from Gmsh, convert the .msh to .gri
    msh2gri('all.msh', 'all.gri')
    # generate the matrices from .gri
    I2E('all.gri')

if __name__ == "__main__":
    main()
