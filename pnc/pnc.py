#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argh
from pnc_help_formatter import PNCFormatter
import products
import productversions
import projects
import buildconfigurations
import buildconfigurationsets
import licenses
import environments

parser = argh.ArghParser()
parser.add_commands([products.create_product,
                     products.update_product,
                     products.get_product,
                     products.list_products,
                     products.list_versions_for_product,
                     productversions.create_product_version,
                     productversions.list_product_versions,
                     productversions.get_product_version,
                     productversions.update_product_version,
                     projects.create_project,
                     projects.delete_project,
                     projects.update_project,
                     projects.get_project,
                     projects.list_projects,
                     licenses.create_license,
                     licenses.update_license,
                     licenses.delete_license,
                     licenses.get_license,
                     licenses.list_licenses,
                     buildconfigurations.create_build_configuration,
                     buildconfigurations.build,
                   #  update_build_configuration,
                     buildconfigurations.list_build_configurations,
                     environments.create_environment,
                     environments.update_environment,
                     environments.delete_environment,
                     environments.get_environment,
                     environments.list_environments,
                     buildconfigurationsets.list_build_configuration_sets,
                     #buildconfigurationsets.add_build_configuration_to_set,
                     buildconfigurationsets.create_build_config_set,
                     buildconfigurationsets.get_build_config_set,
                     buildconfigurationsets.update_build_config_set,
                     buildconfigurationsets.delete_build_config_set,
                     buildconfigurationsets.list_build_configurations_for_set,
                     buildconfigurationsets.trigger_build_config_set],
                    func_kwargs={"formatter_class": PNCFormatter})
parser.autocomplete()

if __name__ == "__main__":
    parser.dispatch()