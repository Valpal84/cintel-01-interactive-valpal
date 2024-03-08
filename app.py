import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="Valerie's App with Plot", fillable=True)

with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins (0).
    # 4. An integer representing the maximum number of bins (100).
    # 5. An integer representing the initial value of the slider
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def histogram():
    # Define the number of points to generate.Use optional type hinting to indicate this is an integer.
    count_of_points: int = 100
    # Set a random seed to ensure reproducability
    np.random.seed(3)
    # Generate random data:
    # = np.random.randn(count_of_points) generates 'count_of_points' samples from a standard normal distribution.
    # - Each sample is then scaled by 15 (to increase the spread) and shifted by 100 (to center the distribution around 100).
    random_data_array = 100 + 15 * np.random.randn(437)
    # Create a histogram of the random data using matplotlib's hist() function:
    # - The first argument is the data array.
    # - The second argument specifies the number of bins, dynamically set by the input slider's current value.
    # - The 'density' parameter, when True, normalizes the histogram so that the total area under the histogram equals 1.
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="green")

@render.plot(alt="Random scatterplot")
def scatterplot():
    count_of_point: int = 100
    np.random.seed(3)
    x = np.random.randn(count_of_point)
    y = np.random.randn(count_of_point)
    sns.scatterplot(x=x, y=y, color='orange')
