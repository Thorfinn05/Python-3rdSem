import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d_with_boundary(x_start, y_start):
    # Initialize arrays for the x and y coordinates
    x = [x_start]
    y = [y_start]

    # Define possible step directions: Up, Down, Left, Right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    steps = 0
    while abs(x[-1]) <= 4 and abs(y[-1]) <= 4:
        dx, dy = directions[np.random.choice(len(directions))]
        new_x = x[-1] + dx
        new_y = y[-1] + dy

        # Append the new coordinates
        x.append(new_x)
        y.append(new_y)
        steps += 1

        print(f"Step: {steps}, Position: ({new_x}, {new_y})")

    print(f"At the boundary after {steps} steps")
    return np.array(x), np.array(y)

def plot_random_walk(x, y):
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, marker='o', linestyle='dotted', markersize=3, linewidth=1, color='green')
    plt.title('2D Random Walk with Boundary Conditions')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Main execution
x_start = int(input("Enter x coordinate: "))
y_start = int(input("Enter y coordinate: "))

x, y = random_walk_2d_with_boundary(x_start, y_start)
plot_random_walk(x, y)