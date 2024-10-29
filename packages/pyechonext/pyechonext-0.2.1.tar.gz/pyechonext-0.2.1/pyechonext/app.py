import inspect
from enum import Enum
from typing import Iterable, Callable, List, Type, Tuple, Optional, Union
from socks import method
from parse import parse
from loguru import logger
from pyechonext.urls import URL
from pyechonext.views import View
from pyechonext.request import Request
from pyechonext.response import Response
from pyechonext.utils.exceptions import (
	RoutePathExistsError,
	MethodNotAllow,
	URLNotFound,
	WebError,
)
from pyechonext.utils import _prepare_url


class ApplicationType(Enum):
	"""
	This enum class describes an application type.
	"""

	JSON = "application/json"
	HTML = "text/html"


class EchoNext:
	"""
	This class describes an EchoNext WSGI Application.
	"""

	__slots__ = ("app_name", "application_type", "urls", "routes")

	def __init__(
		self,
		app_name: str,
		urls: Optional[List[URL]] = [],
		application_type: Optional[ApplicationType] = ApplicationType.JSON,
	):
		"""
		Constructs a new instance.

		:param		app_name:  The application name
		:type		app_name:  str
		"""
		self.app_name = app_name
		self.application_type = application_type
		self.routes = {}
		self.urls = urls
		logger.debug(f"Application {self.application_type.value}: {self.app_name}")

	def _find_view(self, raw_url: str) -> Union[Type[URL], None]:
		"""
		Finds a view by raw url.

		:param		raw_url:  The raw url
		:type		raw_url:  str

		:returns:	URL dataclass
		:rtype:		Type[URL]
		"""
		url = _prepare_url(raw_url)

		for path in self.urls:
			if url == _prepare_url(path.url):
				return path

		return None

	def _check_request_method(self, view: View, request: Request):
		"""
		Check request method for view

		:param		view:			 The view
		:type		view:			 View
		:param		request:		 The request
		:type		request:		 Request

		:raises		MethodNotAllow:	 Method not allow
		"""
		if not hasattr(view, request.method.lower()):
			raise MethodNotAllow(f"Method not allow: {request.method}")

	def _get_view(self, request: Request) -> View:
		"""
		Gets the view.

		:param		request:  The request
		:type		request:  Request

		:returns:	The view.
		:rtype:		View
		"""
		url = request.path

		return self._find_view(url)

	def _get_request(self, environ: dict) -> Request:
		"""
		Gets the request.

		:param		environ:  The environ
		:type		environ:  dict

		:returns:	The request.
		:rtype:		Request
		"""
		return Request(environ)

	def _get_response(self) -> Response:
		"""
		Gets the response.

		:returns:	The response.
		:rtype:		Response
		"""
		return Response(content_type=self.application_type.value)

	def route_page(self, page_path: str) -> Callable:
		"""
		Creating a New Page Route

		:param		page_path:	The page path
		:type		page_path:	str

		:returns:	wrapper handler
		:rtype:		Callable
		"""
		if page_path in self.routes:
			raise RoutePathExistsError("Such route already exists.")

		def wrapper(handler):
			"""
			Wrapper for handler

			:param		handler:  The handler
			:type		handler:  callable

			:returns:	handler
			:rtype:		callable
			"""
			self.routes[page_path] = handler
			return handler

		return wrapper

	def _default_response(self, response: Response, error: WebError) -> None:
		"""
		Get default response (404)

		:param		response:  The response
		:type		response:  Response
		"""
		response.status_code = str(error.code)
		response.body = str(error)

	def _find_handler(self, request: Request) -> Tuple[Callable, str]:
		"""
		Finds a handler.

		:param		request_path:  The request path
		:type		request_path:  str

		:returns:	handler function and parsed result
		:rtype:		Tuple[Callable, str]
		"""
		for path, handler in self.routes.items():
			parse_result = parse(path, request.path)
			if parse_result is not None:
				return handler, parse_result.named

		view = self._get_view(request)

		if view is not None:
			parse_result = parse(view.url, request.path)

			if parse_result is not None:
				return view.view, parse_result.named

		return None, None

	def _handle_request(self, request: Request) -> Response:
		"""
		Handle response from request

		:param		request:  The request
		:type		request:  Request

		:returns:	Response callable object
		:rtype:		Response
		"""
		response = self._get_response()

		handler, kwargs = self._find_handler(request)

		if handler is not None:
			if inspect.isclass(handler):
				handler = getattr(handler(), request.method.lower(), None)
				if handler is None:
					raise MethodNotAllow(f"Method not allowed: {request.method}")

			response.body = handler(request, response, **kwargs)
		else:
			raise URLNotFound(f'URL "{request.path}" not found.')

		return response

	def __call__(self, environ: dict, start_response: method) -> Iterable:
		"""
		Makes the application object callable

		:param		environ:		 The environ
		:type		environ:		 dict
		:param		start_response:	 The start response
		:type		start_response:	 method

		:returns:	response body
		:rtype:		Iterable
		"""
		request = self._get_request(environ)
		response = self._get_response()

		try:
			response = self._handle_request(request)
		except URLNotFound as err:
			self._default_response(response, error=err)
		except MethodNotAllow as err:
			self._default_response(response, error=err)

		return response(environ, start_response)
