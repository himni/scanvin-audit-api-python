# swagger_client.MiscApi

All URIs are relative to *https://auditoria.scanvin.com.br/api/inspection*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspection_get_inspection**](MiscApi.md#inspection_get_inspection) | **GET** /{notification_id} | Inspection - Get Inspection
[**inspection_picture_types**](MiscApi.md#inspection_picture_types) | **GET** /picture-types | Inspection - Picture Types
[**inspection_submit**](MiscApi.md#inspection_submit) | **POST** /submit | Inspection - Submit

# **inspection_get_inspection**
> InspectionGetInspection inspection_get_inspection(notification_id)

Inspection - Get Inspection

Recupera as informações da vistoria e o resultado da auditoria, se estiver disponível.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Api-Key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))
notification_id = 'notification_id_example' # str | O código da notificação, recebido pelo seu webhook via HTTP POST

try:
    # Inspection - Get Inspection
    api_response = api_instance.inspection_get_inspection(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->inspection_get_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| O código da notificação, recebido pelo seu webhook via HTTP POST | 

### Return type

[**InspectionGetInspection**](InspectionGetInspection.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_picture_types**
> str inspection_picture_types()

Inspection - Picture Types

Utilize este endpoint para obter a lista de códigos para os tipos de imagem que devem ser utilizados ao realizar chamadas ao endpoint ```Inspection - Submit```.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Api-Key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))

try:
    # Inspection - Picture Types
    api_response = api_instance.inspection_picture_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->inspection_picture_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspection_submit**
> InspectionSubmit inspection_submit(body)

Inspection - Submit

Utilize este endpoint para enviar uma vistoria para auditoria. As vistorias são colocadas em uma fila e distribuídas aleatoriamente entre os auditores, e são processadas na ordem de chegada. Para receber uma notificação assim que a auditoria for realizada, configure o webhook no [Painel do Cliente](https://auditoria.scanvin.com.br/client/webhook). Alternativamente, caso prefira especificar um webhook customizado para cada vistoria, informe o parâmetro ```postback_url```.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Api-Key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MiscApi(swagger_client.ApiClient(configuration))
body = swagger_client.InspectionSubmitRequest() # InspectionSubmitRequest | 

try:
    # Inspection - Submit
    api_response = api_instance.inspection_submit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->inspection_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InspectionSubmitRequest**](InspectionSubmitRequest.md)|  | 

### Return type

[**InspectionSubmit**](InspectionSubmit.md)

### Authorization

[Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

