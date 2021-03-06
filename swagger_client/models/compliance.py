# coding: utf-8

"""
    AUDITORIA

    # Introducão  Seja bem-vindo a documentação da API do [SCANVIN](https://scanvin.com.br) para auditorias    Nossa API foi criada utilizando o padrão [REST](https://restfulapi.net/) e [HATEOAS](https://restfulapi.net/hateoas/), possibilitando a integração de seu sistema ao nosso, e está documentada abaixo.  # Como usar a API?  Logo a seguir você encontrará todos os recursos e métodos suportados pela API, sendo que essa página possibilita que você teste os recursos e métodos diretamente através dela.  # Autenticação  Você precisa de uma [API KEY](https://en.wikipedia.org/wiki/Application_programming_interface_key#HTTP_APIs) para identificar a conta que está realizando solicitações para a API. Você pode obter seu token de autenticação no seu [Painel do Cliente](https://auditoria.scanvin.com.br/client/).  Insira seu token no campo que se encontra topo desta página para testar os métodos da API.  # Webhook  Você também deve configurar seu [Webhook](https://en.wikipedia.org/wiki/Webhook) no [Painel do Cliente](https://auditoria.scanvin.com.br/client/webhook). Quando os resultados da auditoria estiverem disponíveis, uma notificação será enviada para a URL informada, via [HTTP POST](https://en.wikipedia.org/wiki/POST_(HTTP)). A notificação possui ```Content-type``` do tipo ```application/json```. O [JSON](https://en.wikipedia.org/wiki/JSON) postado contém um único campo, ```notification_id```, que contém o identificador único do evento que gerou a notificação. Deve-se então chamar o endpoint ```Inspection - Get Inspection```, informando esse mesmo identificador único, para recuperar os dados da vistoria, e da auditoria realizada.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Compliance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'engine': 'bool',
        'front_plate': 'bool',
        'rear_plate': 'bool',
        'vin': 'bool'
    }

    attribute_map = {
        'engine': 'engine',
        'front_plate': 'front_plate',
        'rear_plate': 'rear_plate',
        'vin': 'vin'
    }

    def __init__(self, engine=None, front_plate=None, rear_plate=None, vin=None):  # noqa: E501
        """Compliance - a model defined in Swagger"""  # noqa: E501
        self._engine = None
        self._front_plate = None
        self._rear_plate = None
        self._vin = None
        self.discriminator = None
        self.engine = engine
        self.front_plate = front_plate
        self.rear_plate = rear_plate
        self.vin = vin

    @property
    def engine(self):
        """Gets the engine of this Compliance.  # noqa: E501

        Informa se o número do motor está dentro dos padrões.  # noqa: E501

        :return: The engine of this Compliance.  # noqa: E501
        :rtype: bool
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this Compliance.

        Informa se o número do motor está dentro dos padrões.  # noqa: E501

        :param engine: The engine of this Compliance.  # noqa: E501
        :type: bool
        """
        if engine is None:
            raise ValueError("Invalid value for `engine`, must not be `None`")  # noqa: E501

        self._engine = engine

    @property
    def front_plate(self):
        """Gets the front_plate of this Compliance.  # noqa: E501

        Informa se a placa dianteira está dentro dos padrões.  # noqa: E501

        :return: The front_plate of this Compliance.  # noqa: E501
        :rtype: bool
        """
        return self._front_plate

    @front_plate.setter
    def front_plate(self, front_plate):
        """Sets the front_plate of this Compliance.

        Informa se a placa dianteira está dentro dos padrões.  # noqa: E501

        :param front_plate: The front_plate of this Compliance.  # noqa: E501
        :type: bool
        """
        if front_plate is None:
            raise ValueError("Invalid value for `front_plate`, must not be `None`")  # noqa: E501

        self._front_plate = front_plate

    @property
    def rear_plate(self):
        """Gets the rear_plate of this Compliance.  # noqa: E501

        Informa se a placa traseira está dentro dos padrões.  # noqa: E501

        :return: The rear_plate of this Compliance.  # noqa: E501
        :rtype: bool
        """
        return self._rear_plate

    @rear_plate.setter
    def rear_plate(self, rear_plate):
        """Sets the rear_plate of this Compliance.

        Informa se a placa traseira está dentro dos padrões.  # noqa: E501

        :param rear_plate: The rear_plate of this Compliance.  # noqa: E501
        :type: bool
        """
        if rear_plate is None:
            raise ValueError("Invalid value for `rear_plate`, must not be `None`")  # noqa: E501

        self._rear_plate = rear_plate

    @property
    def vin(self):
        """Gets the vin of this Compliance.  # noqa: E501

        Informa se o número do chassi está dentro dos padrões.  # noqa: E501

        :return: The vin of this Compliance.  # noqa: E501
        :rtype: bool
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this Compliance.

        Informa se o número do chassi está dentro dos padrões.  # noqa: E501

        :param vin: The vin of this Compliance.  # noqa: E501
        :type: bool
        """
        if vin is None:
            raise ValueError("Invalid value for `vin`, must not be `None`")  # noqa: E501

        self._vin = vin

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Compliance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Compliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
