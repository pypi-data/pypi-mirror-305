# emissary-client-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *emissary-client-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=emissary-client-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/emissary/emissary). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Emissary - OpenAPI 3.1: This is a Emissary Platform API specification.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](https://github.com/Emissary-Tech/emissary-python/blob/master/#sdk-installation)
* [IDE Support](https://github.com/Emissary-Tech/emissary-python/blob/master/#ide-support)
* [SDK Example Usage](https://github.com/Emissary-Tech/emissary-python/blob/master/#sdk-example-usage)
* [Available Resources and Operations](https://github.com/Emissary-Tech/emissary-python/blob/master/#available-resources-and-operations)
* [File uploads](https://github.com/Emissary-Tech/emissary-python/blob/master/#file-uploads)
* [Retries](https://github.com/Emissary-Tech/emissary-python/blob/master/#retries)
* [Error Handling](https://github.com/Emissary-Tech/emissary-python/blob/master/#error-handling)
* [Server Selection](https://github.com/Emissary-Tech/emissary-python/blob/master/#server-selection)
* [Custom HTTP Client](https://github.com/Emissary-Tech/emissary-python/blob/master/#custom-http-client)
* [Authentication](https://github.com/Emissary-Tech/emissary-python/blob/master/#authentication)
* [Debugging](https://github.com/Emissary-Tech/emissary-python/blob/master/#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install emissary-client-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add emissary-client-sdk
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from emissary_client_sdk import EmissaryClient
import os

async def main():
    s = EmissaryClient(
        api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
    )
    res = await s.base_models.list_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [base_models](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/basemodels/README.md)

* [list](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/basemodels/README.md#list) - List of Base Models

### [datasets](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/datasets/README.md)

* [create](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/datasets/README.md#create) - Create a new Dataset
* [list](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/datasets/README.md#list) - List of Datasets
* [get](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/datasets/README.md#get) - Retrieve a dataset by ID
* [delete](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/datasets/README.md#delete) - Delete a dataset by ID

### [deployments](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md)

* [create](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#create) - Create a new Deployment
* [list](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#list) - List of Deployments
* [get](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#get) - Retrieve a deployment by ID
* [delete](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#delete) - Delete a deployment by ID
* [cancel](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#cancel) - Cancel a deployment by ID
* [get_completions](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#get_completions) - Get Completions from a Deployment
* [get_embeddings](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/deployments/README.md#get_embeddings) - Get Embeddings from a Deployment

#### [deployments.chat](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/chat/README.md)

* [complete](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/chat/README.md#complete) - Get Chat Completions from a Deployment

#### [deployments.classification](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/classification/README.md)

* [get](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/classification/README.md#get) - Get Classification from a Deployment


### [projects](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/projects/README.md)

* [create](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/projects/README.md#create) - Create a new project
* [list](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/projects/README.md#list) - List of Projects
* [get](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/projects/README.md#get) - Retrieve a project by ID
* [delete](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/projects/README.md#delete) - Delete a project by ID

### [training_jobs](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md)

* [create](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#create) - Create a new Training Job
* [list](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#list) - List of Training Jobs
* [retrieve](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#retrieve) - Retrieve a training job by ID
* [delete](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#delete) - Delete a training job by ID
* [cancel](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#cancel) - Cancel a training job by ID
* [list_checkpoints](https://github.com/Emissary-Tech/emissary-python/blob/master/docs/sdks/trainingjobs/README.md#list_checkpoints) - List of Checkpoints

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.datasets.create(project_id="<id>", request_body={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
        "content_type": "<value>",
    },
    "name": "my_dataset",
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from emissary_client_sdk import EmissaryClient
from emissaryclient.utils import BackoffStrategy, RetryConfig
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from emissary_client_sdk import EmissaryClient
from emissaryclient.utils import BackoffStrategy, RetryConfig
import os

s = EmissaryClient(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list()

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_async` method may raise the following exceptions:

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.APIErrorInvalidInput | 400                         | application/json            |
| models.APIErrorUnauthorized | 401                         | application/json            |
| models.SDKError             | 4XX, 5XX                    | \*/\*                       |

### Example

```python
from emissary_client_sdk import EmissaryClient, models
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = None
try:
    res = s.base_models.list()

    if res is not None:
        # handle response
        pass

except models.APIErrorInvalidInput as e:
    # handle e.data: models.APIErrorInvalidInputData
    raise(e)
except models.APIErrorUnauthorized as e:
    # handle e.data: models.APIErrorUnauthorizedData
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://d1d3-4-4-33-74.ngrok-free.app` | None |

#### Example

```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    server_idx=0,
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list()

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    server_url="https://d1d3-4-4-33-74.ngrok-free.app",
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list()

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from emissary_client_sdk import EmissaryClient
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = EmissaryClient(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from emissary_client_sdk import EmissaryClient
from emissary_client_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = EmissaryClient(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                      | Type                      | Scheme                    | Environment Variable      |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `api_key`                 | apiKey                    | API key                   | `EMISSARY_CLIENT_API_KEY` |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from emissary_client_sdk import EmissaryClient
import os

s = EmissaryClient(
    api_key=os.getenv("EMISSARY_CLIENT_API_KEY", ""),
)

res = s.base_models.list()

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from emissary_client_sdk import EmissaryClient
import logging

logging.basicConfig(level=logging.DEBUG)
s = EmissaryClient(debug_logger=logging.getLogger("emissary_client_sdk"))
```

You can also enable a default debug logger by setting an environment variable `EMISSARY_CLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=emissary-client-sdk&utm_campaign=python)
