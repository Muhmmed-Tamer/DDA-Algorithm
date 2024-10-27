import matplotlib.pyplot as plt
def dda_line(x0, y0, x1, y1):
    # Calculate the differences
    dx = x1 - x0
    dy = y1 - y0
    
    # Determine the number of steps required
    steps = int(max(abs(dx), abs(dy)))
    
    # Calculate increment in x and y for each step
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Initialize the starting point
    x = x0
    y = y0
    
    # Create lists to store the points
    points = []
    
    for _ in range(steps + 1):
        points.append((round(x), round(y)))  # Round to nearest integer
        x += x_inc
        y += y_inc
    
    return points

# Example usage
if __name__ == "__main__":
    # Define start and end points
    x0, y0 = 2, 3
    x1, y1 = 10, 7
    
    # Get the points from DDA algorithm
    line_points = dda_line(x0, y0, x1, y1)
    
    # Extract x and y coordinates for plotting
    x_coords, y_coords = zip(*line_points)
    
    # Plotting the line
    plt.plot(x_coords, y_coords, marker='o')
    plt.title('DDA Line Drawing Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.xlim(0, 12)
    plt.ylim(0, 10)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.show()