"""
This module contains classes related to interaction with local docker engine.
"""
from pathlib import Path
import shutil
from prettytable import PrettyTable, ALL
import docker
from celestical.config import Config

class DockerMachine:
    """
    This class contains attributes and method to interact with local docker engine. 
    """

    def __init__(self, config:Config = None):
        self.config = config
        if config is None:
            self.config = Config()
        self.client = self.get_docker_client()

    def _build_unix_socket(self, socket_path: Path) -> str:
        return 'unix://' + str(socket_path.resolve())

    def _connect_docker_colima(self) -> docker.DockerClient:
        """ Try to establish client connection with colima
        """
        current_ctx = docker.context.Context.load_context(
            docker.context.api.get_current_context_name())
        if current_ctx is None:
            return None
        url = current_ctx.endpoints["docker"]["Host"]
        return docker.DockerClient(base_url=url)

    def get_docker_client(self):
        """ Returns a docker client taken from local environment """
        client = None
        try:
            self.config.logger.debug("Searching docker API client from_env()")
            client = docker.from_env()
        except Exception as oops:
            err_msg = "Could not connect to the docker service. Is it really running?"
            self.config.logger.debug(err_msg)
            self.config.logger.error(oops)
            client = None

        # alternative to finding docker
        if client is None:
            try:
                self.config.logger.debug("Searching docker API from system socket.")
                client = docker.DockerClient(base_url='unix:///var/run/docker.sock')
            except Exception as oops:
                self.config.logger.error(oops)
                client = None

        if client is None:
            try:
                self.config.logger.debug("Searching docker API from userspace socket.")
                user_tilde = Path("~")
                user_home = user_tilde.expanduser()
                socket_path = user_home / ".docker/run/docker.sock"
                client = docker.DockerClient(base_url=self._build_unix_socket(socket_path))
            except Exception as oops:
                self.config.logger.error(oops)
                client = None

        # alternative to finding docker on Mac or Linux running Colima
        if client is None:
            try:
                self.config.logger.debug("Searching docker API client via context (Colima)")
                client = self._connect_docker_colima()
            except Exception as oops:
                self.config.logger.error(oops)
                client = None

        #if client is None:
        # then use call to command line docker client
        return client

    def get_ports(self,
              image_id:str,
              proto:str="tcp") -> str:
        """ Get ports from containers created from the specified image.
            else get the ExposedPorts info from the image itself.

            Params:
                image_id(str): should the string hash of the image
                docker_clienti(any): a docker client
                proto(str): (unused for now) ports for a that specific protocol,
                by default 'tcp'
            Returns:
                a string for a joint list of ports
        """
        if self.client is None:
            # We retry again in case it is a timing issue
            self.client = self.get_docker_client()
            if self.client is None:
                # Do nothing or do it via command lines
                return ""
            # else continue

        ports = set()

        # Checking from containers
        for container in self.client.containers.list(all=True):
            if container.image.id == image_id:
                port_data = container.attrs['HostConfig']['PortBindings']
                if port_data:
                    for port, bindings in port_data.items():
                        # get only the port number, not the protocol
                        ports.add(str(port.split('/')[0]))

        # Checking from listed images
        if len(ports) == 0:
            try:
                img = self.client.images.get(image_id)
                for tcpport in [str(attr).split("/")[0]
                                for attr in
                                img.attrs["Config"]["ExposedPorts"]
                                if "tcp" in attr]:
                    ports.add(tcpport)
            except Exception as oops:
                # The image_id is not found
                # The ports set remains empty and that's all ok.
                self.config.logger.debug(oops)

        return ",".join(sorted(ports))

    def list_local_images(self) -> PrettyTable|None:
        """List all docker images locally available with port information.

        Returns:
            PrettyTable of formatted table of docker images
        """
        if self.client is None:
            # We retry again in case it is a timing issue
            self.client = self.get_docker_client()
            if self.client is None:
                # Do nothing or do it via command lines
                return None

        table = PrettyTable()
        table.field_names = ["Image ID", "Image Name", "Tags", "Ports"]
        table.hrules = ALL  # Add horizontal rules between rows

        images = []
        terminal_width = 100
        try:
            terminal_width, _ = shutil.get_terminal_size()
            images = self.client.images.list()
        except Exception as whathappened:
            self.config.logger.error(whathappened)
            return table

        # Adjust column widths based on the terminal width
        # divide by 2 for two lines
        id_width = max(len(image.id) for image in images) // 2 + 1
        name_width = max(len(image.tags[0].split(':')[0])
                        if image.tags
                        else 0 for image in images)
        # divide by 2 to leave space for the Ports column
        tags_width = (terminal_width - id_width - name_width - 7) // 2
        ports_width = tags_width
        table.align["Image ID"] = "l"
        table.align["Image Name"] = "l"
        table.align["Tags"] = "l"
        table.align["Ports"] = "l"
        table._max_width = {
            "Image ID": id_width,
            "Image Name": name_width,
            "Tags": tags_width,
            "Ports": ports_width}

        for image in images:
            # Split the Image ID into two lines
            half_length = len(image.id) # // 2
            formatted_id = f'{image.id[:half_length]}\n{image.id[half_length:]}'
            # Extract image name from the tags
            image_name = image.tags[0].split(':')[0] if image.tags else 'N/A'
            # Get ports
            ports = self.get_ports(image.id)
            table.add_row([formatted_id, image_name, ', '.join(image.tags), ports])

        return table
