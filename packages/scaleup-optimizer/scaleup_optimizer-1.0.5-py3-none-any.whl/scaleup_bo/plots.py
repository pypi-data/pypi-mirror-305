import numpy as np
from skopt.utils import create_result
from skopt.plots import plot_objective
from skopt.space import Space
import matplotlib.pyplot as plt


def plot_performance(optimizer):
    """Plots the minimum objective function value achieved over iterations.
    
    Parameters:
        optimizer: Optimizer object with Y_iters attribute containing objective func values.
        
    The plot shows the convergence of the optimization process by tracking the
    minimum value found up to each iteration.
    """
    min_f = np.minimum.accumulate(optimizer.Y_iters)

    plt.plot(min_f, marker='o', label='f(x)')
    plt.xlabel('Number of steps (n)')
    plt.ylabel('min f(x) after n steps')
    plt.title('Performance Improvement Over Iteration')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_opt_process(optimizer):
    """Plots the optimization process by showing objective function values over iterations.
    
    Parameters:
        optimizer: Optimizer object with Y_iters attribute containing objective func values.
        
    The plot visualizes how the objective function values change across optimization steps.
    """
    plt.plot(optimizer.Y_iters, marker='o', label='f(x)')
    plt.xlabel('Number of steps (n)')
    plt.ylabel('f(x) after n steps')
    plt.title('Optimization Process')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_objective_contour(optimizer):
    """Plots the objective function landscape using a contour plot based on the optimizer's results.

    This function visualizes the optimization process by creating a contour plot of the
    objective function, showing how the function values vary across the search space.

    Parameters:
        optimizer: Optimizer object with search_space and Y_iters attributes. 
                   - `search_space`: Defines the bounds for each parameter in the optimization problem.
                   - `Y_iters`: Contains objective function values obtained during optimization.

    The plot provides a visual representation of the objective function landscape and the locations of the sampled points.
    """
    space = Space(optimizer.search_space)

    # After optimization
    opt_result = create_result(
        Xi=optimizer.X_iters.tolist(),
        yi=optimizer.Y_iters.tolist(),
        space=space,
        models=[optimizer.gp_models[-1]]
    )

    # Plot the objective landscape
    plot_objective(opt_result)