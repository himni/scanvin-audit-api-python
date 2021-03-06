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


class InspectionGetInspection(object):
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
        'status': 'bool',
        'protocol': 'Protocol',
        'audit': 'Audit'
    }

    attribute_map = {
        'status': 'status',
        'protocol': 'protocol',
        'audit': 'audit'
    }

    def __init__(self, status=None, protocol=None, audit=None):  # noqa: E501
        """InspectionGetInspection - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._protocol = None
        self._audit = None
        self.discriminator = None
        self.status = status
        self.protocol = protocol
        self.audit = audit

    @property
    def status(self):
        """Gets the status of this InspectionGetInspection.  # noqa: E501

        Informa se a requisição foi concluída com sucesso.  # noqa: E501

        :return: The status of this InspectionGetInspection.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InspectionGetInspection.

        Informa se a requisição foi concluída com sucesso.  # noqa: E501

        :param status: The status of this InspectionGetInspection.  # noqa: E501
        :type: bool
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def protocol(self):
        """Gets the protocol of this InspectionGetInspection.  # noqa: E501


        :return: The protocol of this InspectionGetInspection.  # noqa: E501
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this InspectionGetInspection.


        :param protocol: The protocol of this InspectionGetInspection.  # noqa: E501
        :type: Protocol
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def audit(self):
        """Gets the audit of this InspectionGetInspection.  # noqa: E501


        :return: The audit of this InspectionGetInspection.  # noqa: E501
        :rtype: Audit
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        """Sets the audit of this InspectionGetInspection.


        :param audit: The audit of this InspectionGetInspection.  # noqa: E501
        :type: Audit
        """
        if audit is None:
            raise ValueError("Invalid value for `audit`, must not be `None`")  # noqa: E501

        self._audit = audit

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
        if issubclass(InspectionGetInspection, dict):
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
        if not isinstance(other, InspectionGetInspection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
