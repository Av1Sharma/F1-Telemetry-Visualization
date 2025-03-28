# F1 Telemetry Visualization

This project visualizes Formula 1 telemetry data using 3D plots in Python. The goal is to showcase F1 car movements based on real telemetry data, such as the car's position (X, Y, Z) and speed, extracted from FastF1. The project is a work in progress and will be continuously refined to improve the data and features.

## Current Features:
- **3D Plot**: Visualize F1 car telemetry data in 3D (X, Y, Z positions).
- **Speed Visualization**: Color the path based on the speed of the car.

## Work in Progress:
- **Data Refinement**: The data processing part is still being refined for more accurate telemetry tracking.
- **Animation**: Future plans include animating the car's movement over time for better visualization and analysis.

## Future Features:
- **Animation**: We will animate the telemetry data to show the car’s movement frame by frame, providing a dynamic view of the race.
- **Additional Telemetry Metrics**: Plans to include more data points like tire wear, lap times, and other telemetry information for a richer experience.

## Inspiration:
This project was inspired by [this post](https://www.reddit.com/r/F1Technical/comments/135eksr/i_made_a_tool_to_visualise_f1_telemetry_data_in/) on Reddit by a fellow F1 enthusiast, who helped me tackle some of the challenges faced during development. A huge shoutout for the inspiration!

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/f1-telemetry-visualization.git
   cd f1-telemetry-visualization
2. Install Requirements:
   ```bash
    pip install -r requirements.txt
3. Run the data loading and visualization script:
   ```bash
   python src/load_data.py
   python src/plot_3d.py
## License:
This project is licensed under the MIT License - see the LICENSE file for details.

