import os

from typing import Dict
from os.path import join
from ninja_bear import DistributorBase, DistributeInfo
from ninja_bear.base.distributor_credentials import DistributorCredentials


class Distributor(DistributorBase):
    """
    FileSystem specific distributor. For more information about the distributor methods,
    refer to DistributorBase.
    """
    def __init__(self, config: Dict, credentials: DistributorCredentials=None):
        super().__init__(config, credentials)

        paths, _ = self.from_config('paths')

        # Make sure _paths is a list.
        if not isinstance(paths, list):
            paths = [paths]

        # Make sure _paths are directories.
        self._paths = paths
        self._create_parents, _ = self.from_config('create_parents')

    def _distribute(self, info: DistributeInfo) -> DistributorBase:
        """
        Distributes the generated config. Here goes all the logic to distribute the generated
        config according to the plugin's functionality (e.g. commit to Git, copy to a different
        directory, ...).

        :param info: Contains the required information to distribute the generated config.
        :type info:  DistributeInfo
        """
        parent = info.input_path.parent
        parent = str(parent.absolute()) if parent else ''

        for path in self._paths:
            destination_path = join(parent, path)

            # Create parents if required.
            if destination_path and self._create_parents:
                os.makedirs(destination_path, exist_ok=True)

            # Write files to destination path.
            with open(join(destination_path, info.file_name), 'w') as f:
                f.write(info.data)
