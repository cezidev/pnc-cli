import logging
import os
import sys
import shutil
import tarfile
import urllib

from argh import arg
from pnc_cli import productmilestones
from pnc_cli import buildrecords

target="target/"
tempdir="target/tmp/"


@arg('-m', '--milestone_id', help='Product milestone id', type=int)
@arg('-o', '--output', help='Output archive name')
def generate_sources_zip(milestone_id=None, output=None):
    """
    Generate a sources archive for given milestone id. 
    """
    if not is_input_valid(milestone_id, output):
        print("invalid input")
        return 1
    create_work_dir(output)
    download_sources_artifacts(milestone_id, output)
    create_zip(output)

def create_zip(directory_name):
    archive_name = target + directory_name
    shutil.make_archive(archive_name, 'zip', target + directory_name)
    print("Successfully created sources archive: " + archive_name + ".zip")


def download_sources_artifacts(milestone_id, directory_name):
    milestone = productmilestones.get_milestone(milestone_id)
    build_record_ids = milestone.performed_builds
    for record_id in build_record_ids:
        print("downloading build record["+str(record_id)+"]")
        built_artifacts = buildrecords.list_built_artifacts(record_id, 100000)
        sources_artifacts = [artifact for artifact in built_artifacts if artifact.filename.endswith("project-sources.tar.gz")]

        if len(sources_artifacts) != 1:
            print("Invalid number of project sources artifacts for build_record_id=" + str(record_id)
                  + ". Expecting exactly 1, found: " + str(len(sources_artifacts)) + ", artifacts found: " + str(sources_artifacts))
            sys.exit(1)

        for artifact in sources_artifacts:
            download_and_unpack(artifact, directory_name)


def download_and_unpack(artifact, directory_name):
    sources_tgz = tempdir + artifact.filename
    urllib.urlretrieve(artifact.public_url, sources_tgz)
    output_directory = target+directory_name
    tar = tarfile.open(sources_tgz, "r:gz")
    print("extracting " + sources_tgz)
    tar.extractall(output_directory)
    tar.close()
    print("done")


def create_work_dir(directory_name):
    if os.path.exists(target):
        shutil.rmtree(target)
    os.makedirs(target + directory_name)
    os.makedirs(tempdir)

def is_input_valid(milestone_id, output_name):
    if milestone_id is None:
        logging.error('Product milestone id --milestone_id is not specified.')
        return False
    if output_name is None:
        logging.error('Output archive name --output is not specified.')
        return False

    return True