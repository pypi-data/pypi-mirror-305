from dataclasses import dataclass, field
from uuid import uuid4
from serde import serialize

from cyst.api.configuration.configuration import ConfigItem


@serialize
@dataclass
class DataConfig(ConfigItem):
    """ Configuration of a data element.

    This component is currently in a very rudimentary state and the future updates will among other things include the
    option to encrypt the data and add specific flags.

    :param owner: An identity of the owner of the data.
    :type owner: str

    :param description: A textual description of the data. Currently the only mechanism to distinguish different data.
    :type description: str

    :param id: A unique identifier of the data configuration.
    :type id: str
    """
    owner: str
    description: str
    id: str = field(default_factory=lambda: str(uuid4()))
