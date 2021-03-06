import connexion
import six

from var_controller import *
from swagger_server.models.var import VAR  # noqa: E501
from swagger_server import util


def get_var_by_id(id):  # noqa: E501
    """get_var_by_id

    Returns value of a named variable identified by id # noqa: E501

    :param id: name of variable
    :type id: str
    :rtype: VAR
    """
    item = get_var_by_id_mongo(id)
    return VAR(item[0], item[1], item[2])


def var_get():  # noqa: E501
    """var_get

    Returns list of variables # noqa: E501


    :rtype: List[VAR]
    """
    listofVar = []
    items = get_var()
    for each in items:
	listofVar.append(VAR(each[0], each[1], each[2]))
    return listofVar
