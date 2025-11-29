#visualization of a drone swarm responding to incursions on a 2D plane and intercepting

import numpy as np
import matplotlib.pyplot as plt

#generate position array

grid_size = 100
grid = np.zeros((grid_size, grid_size))

num_drones = 10

#function to distribute drones on the left and bottom edges

def distribute_drones(num_drones, grid_size):
    positions = []
    for i in range(num_drones):
        if i % 2 == 0:
            # Left edge
            x = 0.
            y = np.random.randint(0, grid_size)
        else:
            # Bottom edge
            x = np.random.randint(0, grid_size)
            y = 0.
        positions.append((x, y))
    return positions

drone_positions = np.array(distribute_drones(num_drones, grid_size))

#generate a random number of incursions all on the top right corner
num_incursions = 5

incursion_positions = []

for _ in range(num_incursions):
    x = int(grid_size)
    y = int(grid_size)
    incursion_positions.append([x, y])


incursion_positions_arr = np.array(incursion_positions, dtype=float)

#change in time to reflect drones coming to intercept incursions (the incursions also move in a general tendency to the bottom left)
time_steps = 200

for t in range(time_steps):
    plt.clf()
    plt.xlim(-10, grid_size + 10)
    plt.ylim(-10, grid_size + 10)
    
    # Plot drone positions
    plt.scatter(drone_positions[:, 0], drone_positions[:, 1], c='blue', label='Drones')
    
    # Plot incursion positions
    plt.scatter(incursion_positions_arr[:, 0], incursion_positions_arr[:, 1], c='red', label='Incursions')
    
    plt.title(f'Drone Swarm Interception - Time Step {t}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.pause(0.01)
    
    # Update drone positions to move towards nearest incursion
    for i in range(num_drones):
        if len(incursion_positions_arr) == 0:
            break
        distances = np.linalg.norm(incursion_positions_arr - drone_positions[i], axis=1)
        nearest_incursion_idx = np.argmin(distances)
        direction = incursion_positions_arr[nearest_incursion_idx] - drone_positions[i]
        direction = direction / np.linalg.norm(direction)  # Normalize
        drone_positions[i] += direction * 2  # Move drones faster
    
    # Update incursion positions to move towards bottom left
    for j in range(len(incursion_positions_arr)):
        direction = np.array([-1., -1.])
        direction = direction / np.linalg.norm(direction)  # Normalize
        incursion_positions_arr[j] += direction * 1.0  # Move incursions slower



#visualization using matplotlib

