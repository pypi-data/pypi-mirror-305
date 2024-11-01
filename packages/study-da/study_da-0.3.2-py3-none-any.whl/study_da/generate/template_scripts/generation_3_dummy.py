"""This is a template script for generation 1 of simulation study, in which ones generates a
particle distribution and a collider from a MAD-X model."""

# ==================================================================================================
# --- Imports
# ==================================================================================================

# Import standard library modules
import logging
import os

# Import third-party modules
import pandas as pd

# Import user-defined modules
from study_da.utils import (
    load_dic_from_path,
    set_item_in_dic,
    write_dic_to_path,
)

# Set up the logger here if needed


# ==================================================================================================
# --- Script functions
# ==================================================================================================
def reupdate_particles_distribution(full_configuration):
    # Get configuration
    file_particles = (
        "../" + full_configuration["config_simulation"]["path_distribution_file_output"]
    )

    # Load particle distribution
    particle_df = pd.read_parquet(file_particles)

    # Multiply all x values by 2
    particle_df["r_vect"] = particle_df["r_vect"] * 2

    # Save output (although the path is the same, location will be one level lower than the previous
    # generation, since the file is being called from a child directory)
    particle_df.to_parquet(full_configuration["config_simulation"]["path_distribution_file_output"])


# ==================================================================================================
# --- Parameters definition
# ==================================================================================================
dict_mutated_parameters = {{parameters}}
path_configuration = "{{main_configuration}}"

# ==================================================================================================
# --- Script for execution
# ==================================================================================================

if __name__ == "__main__":
    logging.info("Starting script to configure collider and track")

    # Load full configuration
    full_configuration, ryaml = load_dic_from_path(path_configuration)

    # Mutate parameters in configuration
    for key, value in dict_mutated_parameters.items():
        set_item_in_dic(full_configuration, key, value)

    # Update particle distribution
    reupdate_particles_distribution(full_configuration)

    # Drop updated configuration
    name_configuration = os.path.basename(path_configuration)
    write_dic_to_path(full_configuration, name_configuration, ryaml)

    logging.info("Script finished")
