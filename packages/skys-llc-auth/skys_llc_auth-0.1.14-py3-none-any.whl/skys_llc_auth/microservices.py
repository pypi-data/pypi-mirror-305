from typing import Any

import httpx
from httpx._types import RequestContent, RequestFiles

from skys_llc_auth.exceptions import RequestError


class RequestBetweenMicroservices:
    def __init__(
        self,
        refresh_url: str,
        login_url: str,
        name: str,
        access: str,
        refresh: str,
        login: str,
        password: str,
        retries: int,
    ):
        self.refresh_url = refresh_url
        self.login_url = login_url
        self.name = name
        self.access_token = access
        self.refresh_token = refresh
        self.login = login
        self.password = password
        self.transport = httpx.AsyncHTTPTransport(retries=retries)
        self.headers = {}

    async def _send_request(
        self,
        method: str,
        url: str,
        content: RequestContent | None = None,
        data: dict[str, Any] | None = None,
        files: RequestFiles | None = None,
        json: Any | None = None,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Function for send async request to another microservices"""
        async with httpx.AsyncClient(transport=self.transport) as client:
            response = await client.request(
                method,
                url,
                content=content,
                data=data,
                files=files,
                json=json,
                params=params,
                headers=headers,
                timeout=timeout,
            )

        return response  # noqa: RET504

    async def request_with_microservice_tokens(
        self,
        method: str,
        url: str,
        *args: Any,
        **kwargs: Any,
    ) -> httpx.Response:
        """Function for send async request to another microservices and validate credentials"""
        if not self.access_token:
            await self.logging_in()

        auth = {"Authorization": "Bearer " + self.access_token}
        self.headers = kwargs.get("headers", {})
        self.headers.update(auth)

        response = await self._send_request(method=method, url=url, headers=self.headers, *args, **kwargs)  # noqa: B026

        if response.status_code == 401:
            refreshed_token_pair = await self.refresh_tokens()

            if refreshed_token_pair.status_code == 401:
                await self.logging_in()

                self.headers.update({"Authorization": "Bearer " + self.access_token})

                return await self._send_request(method=method, url=url, headers=self.headers, *args, **kwargs)  # noqa: B026

            return await self._send_request(method=method, url=url, headers=self.headers, *args, **kwargs)  # noqa: B026

        return response

    async def logging_in(self) -> httpx.Response:
        """Function for send async request to users and get tokens"""
        response = await self._send_request(
            "POST", self.login_url, json={"login": self.login, "password": self.password}
        )

        if response.status_code == 401:
            raise RequestError(f"Login failed for {self.name}")

        if response.status_code == 201:
            self.access_token = response.json().get("access_token", "")
            self.refresh_token = response.json().get("refresh_token", "")

        return response

    async def refresh_tokens(self) -> httpx.Response:
        """Function for send async request to users and refresh new tokens"""
        response = await self._send_request("POST", self.refresh_url, headers={"Authorization": self.refresh_token})
        if response.status_code == 401:
            raise RequestError(f"Login failed for {self.name}")

        if response.status_code == 201:
            self.access_token = response.json().get("access_token", "")
            self.refresh_token = response.json().get("refresh_token", "")

        return response
