import os
import glob


class GitRepoParser:

    def __init__(self, repo_dir: str):
        self.repo_dir = repo_dir

    def get_folder_path(self, service_name: str) -> str:
        dir_path = '{path}/configuration/settings/{name}'.format(
            path=self.repo_dir,
            name=service_name
        )
        return dir_path

    def create_new_service(self, service_name: str, service_version: str):
        dir_path = self.get_folder_path(service_name)

        if os.path.isdir(dir_path):
            return

        os.makedirs(dir_path)
        property_file = '{folder}/{name}-deployment.properties'.format(
            folder=dir_path,
            name=service_name
        )

        current_path = os.path.dirname(__file__)
        template_path = os.path.join(
            current_path, '..', 'file_templates/deployment.properties'
        )

        if not os.path.isfile(template_path):
            return

        template_file = open(template_path, 'r')
        with open(property_file, 'w') as properties:
            for line in template_file:
                # Create parser for this code part
                value = line.strip().replace(
                    '%service_name%', service_name
                )

                properties.write(value + '\n')

        template_file.close()
