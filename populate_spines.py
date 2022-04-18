# take in N number to populate that many points
# uses fibonacci lattice
#
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3d #future use

num_spines = int( input("Number of spines: "))

def populate_spines(num_points):

    #golden angle in radians
    goldenAngle = (3 - np.sqrt(5)) * np.pi

    # Create a list of golden angle increments along the range of number of points
    theta = goldenAngle * np.arange(0, num_points)

    # Z is split into a range of -1 to 1 in order to create a unit circle
    z = np.linspace(1/num_points-1, 1-1/num_points, num_points)

    # a list of the radii at each height step of the unit circle
    radius = np.sqrt(1 - z * z)

    # Determine where xy fall on the sphere
    y = radius * np.sin(theta)
    x = radius * np.cos(theta)

    print(x,y,z)

    fig = plt.figure(num="N Number of Spines on a Sphere")
    ax = fig.add_subplot(111, projection='3d')

    # outer sphere shape to verify the points lie on the surface
    r = 1
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    X = r * np.outer(np.cos(u), np.sin(v))
    Y = r * np.outer(np.sin(u), np.sin(v))
    Z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(X, Y, Z, color='linen', alpha=0.5)

    #ax.plot(x, y, z, color="red")
    ax.scatter(x, y, z, color="red")
    ax.plot(x, y, z, color='blue')
    plt.title("Number of Spines: %i" % num_points)

    plt.show()

#passes the user input to function
populate_spines(num_spines)




