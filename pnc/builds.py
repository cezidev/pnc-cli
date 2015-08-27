from argh import arg
import client
from client.BuildconfigurationsApi import BuildconfigurationsApi
import utils

__author__ = 'thauser'
def _create_build_configuration(name, project_id, environment, description, scm_url, scm_revision, patches_url,
                                build_script):
    created_build_configuration = client.models.Configuration.Configuration()
    created_build_configuration.name = name
    created_build_configuration.projectId = project_id
    created_build_configuration.environmentId = environment
    return created_build_configuration

def _get_build_configuration_id_by_name(name):
    """
    Returns the id of the build configuration matching name
    :param name: name of build configuration
    :return: id of the matching build configuration, or None if no match found
    """
    response = BuildconfigurationsApi(utils.get_api_client()).getAll()
    for config in response.json():
        if config["name"] == name:
            return config["id"]
    return None

def _build_configuration_exists(search_id):
    """
    Test if a build configuration matching search_id exists
    :param search_id: id to test for
    :return: True if a build configuration with search_id exists
    """
    response = BuildconfigurationsApi(utils.get_api_client()).getSpecific(id=search_id)
    if response.ok:
        return True
    return False

@arg("-n", "--name", help="Name of the build configuration to trigger")
@arg("-i", "--id", help="ID of the build configuration to trigger")
def build(name=None,id=None):
    """Trigger a build configuration giving either the name or ID."""
    if id:
        if _build_configuration_exists(id):
            response = BuildconfigurationsApi(utils.get_api_client()).trigger(id=id)
        else:
            print("There is no build configuration with id {0}.".format(id))
            return
    elif name:
        id = _get_build_configuration_id_by_name(name)
        if id:
            response = BuildconfigurationsApi(utils.get_api_client()).trigger(id=id)
        else:
            print("There is no build configuration with name {0}.".format(name))
            return
    else:
        print("Build requires either a name or an ID of a build configuration to trigger.")
        return

    if not response.ok:
        utils.print_failure()
        utils.print_error(__name__,response)
        return

    triggered_build = response.json()
    utils.print_by_key(triggered_build)
    return triggered_build

def create_build_configuration(name, project_id, environment, description="", scm_url="", scm_revision="", patches_url="",
                               build_script=""):
    #check for existing project_ids, fail out if the project id doesn't exist
    build_configuration = _create_build_configuration(name, project_id, environment, description, scm_url, scm_revision, patches_url, build_script)
    response = BuildconfigurationsApi(utils.get_api_client()).createNew(body=build_configuration)
    new_bc = response.json()
    utils.print_by_key(new_bc)
    return new_bc


@arg("-a", "--attributes", help="List of attributes to retrieve. Will print given attributes separated by whitespace.")
def list_build_configurations(attributes=None):
    response = BuildconfigurationsApi(utils.get_api_client()).getAll()
    if not response.ok:
        utils.print_error(__name__, response)
        return

    build_configurations = response.json()
    if attributes is not None:
        utils.print_matching_attribute(build_configurations, attributes, client.models.Configuration.Configuration().attributeMap)
    else:
        utils.print_by_key(build_configurations)
    return build_configurations