# Rayoptix

`Rayoptix` is a Python library designed to run from the terminal. It facilitates the creation and evaluation of simulations for complex bifacial photovoltaic systems using ray tracing techniques. With this tool, users can define modules, set up experimental conditions, and run simulations to analyze the energy performance of these systems.

## Installation

To install `Rayoptix`, simply run:

```bash
pip install rayoptix
```
Note: It is necessary to have the Radiance, bifacial_radiance, pandas, matplotlib, sutil, GPUtil, seaborn, and psutil libraries installed beforehand.

## References

Ayala Pelaez, S. and Deline, C. (2020). *bifacial_radiance: a Python package for modeling bifacial solar photovoltaic systems*. Journal of Open Source Software, 5(50), 1865. [https://doi.org/10.21105/joss.01865](https://doi.org/10.21105/joss.01865)

## Function Documentation

For more details on each of the functions in `Rayoptix`, please refer to the specific documentation:

- [Folder Setup (`setup_folders`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/setup_folders.md): Allows creating and configuring folders to store simulation configurations.
- [Create Module (`make_module`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_module.md): Creates a bifacial radiance module based on CSV parameters.
- [Add Torque Tube (`add_torque_tube`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/add_torque_tube.md): Adds a torque tube to a bifacial radiance module.
- [Add Cell Module (`add_cell_module`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/add_cell_module.md): Adds a cell module to a bifacial radiance module.
- [Add Omega Profile (`add_omega`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/add_omega.md): Adds an omega profile to a bifacial radiance module.
- [Add Frame (`add_frame`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/add_frame.md): Adds a frame to a bifacial radiance module.
- [Show Module (`show_module`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/show_module.md): Displays the current module configuration.
- [Read Module (`read_module`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/read_module.md): Reads and loads a module configuration file.
- [Compile Text (`compile_text`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/compile_text.md): Compiles text data for a module configuration.
- [Return Material Files (`return_material_files`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/return_material_files.md): Returns material file paths for a bifacial radiance simulation.
- [Set Ground (`set_ground`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_ground.md): Sets the ground material for the simulation.
- [Set 1-Axis Tracker (`set_1axis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_1axis.md): Sets the 1-axis tracker configuration for the simulation.
- [Create Scene (`make_scene`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_scene.md): Creates a scene based on CSV parameters.
- [Create 1-Axis Tracker Scene (`make_scene1axis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_scene1axis.md): Creates a 1-axis tracker scene based on CSV parameters.
- [Generate OCT File (`make_oct`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_oct.md): Generates an .oct file for the simulation.
- [Generate 1-Axis OCT File (`make_oct1axis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_oct1axis.md): Generates an .oct file for a 1-axis tracker configuration.
- [Show Scene (`show_scene`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/show_scene.md): Displays the scene for the simulation.
- [Create Custom Object (`make_customobject`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_customobject.md): Creates a custom object based on CSV parameters.
- [Append to Scene (`append_to_scene`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/append_to_scene.md): Appends a custom object to the scene.
- [Generate Cumulative Sky (`gen_cum_sky`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/gen_cum_sky.md): Generates a cumulative sky for the simulation folder.
- [Generate Cumulative Sky for 1-Axis Tracker (`gen_cum_sky_1axis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/gen_cum_sky_1axis.md): Generates a cumulative sky for a 1-axis tracker configuration.
- [Generate Daylighting Data (`gen_daylit`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/gen_daylit.md): Generates daylighting data for a specific time index.
- [Manually Generate Daylighting Data (`gen_daylit_manual`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/gen_daylit_manual.md): Manually generates daylighting data using specified values.
- [Generate Daylighting Data for 1-Axis Tracker (`gen_daylit_1axis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/gen_daylit_1axis.md): Generates daylighting data for a 1-axis tracker configuration.
- [Set Weather (`set_weather`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_weather.md): Configures the weather files for the simulation folder using parameters from a specified CSV file.
- [Set Module Analysis (`set_module_analysis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_module_analysis.md): Configures and runs the module analysis for a bifacial radiance simulation using parameters from a specified CSV file.
- [Set Back Scan (`set_back_scan`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_back_scan.md): Updates the back scan parameters for a bifacial radiance simulation using values from a specified CSV file.
- [Set Front Scan (`set_front_scan`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/set_front_scan.md): Updates the front scan parameters for a bifacial radiance simulation using values from a specified CSV file.
- [Save Results (`save_results`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/save_results.md): Generates a heatmap from the results of a bifacial radiance simulation and saves it to a specified path or displays it.
- [Multi-Point Analysis (`multi_analysis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/multi_analysis.md): Runs a multi-point analysis for bifacial radiance, executing multiple analyses based on the specified sensor configuration.
- [Perform Analysis (`make_analysis`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_analysis.md): Performs the analysis for a bifacial radiance simulation using previously defined scan points.
- [Setup Analysis Object (`make_analysis_obj`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/make_analysis_obj.md): Sets up the analysis object for a bifacial radiance simulation.
- [Get Timestamp (`get_timestamp`)](https://github.com/Daval03/CE-114-rayoptix/blob/main/docs/get_timestamp.md): Retrieves a timestamp from the simulation data based on the provided time.

Each link leads to detailed documentation on how to use the corresponding commands, their options, and usage examples.