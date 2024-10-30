from __future__ import annotations
import time
import uuid
import datetime

from ..utils.helpers import _validate_api_key
from .utils.logging import _handle_special_types
from .utils.logging import *


# Logs #
# -----#


class Log:

    def __init__(
        self,
        id: int,
        timestamp: Optional[datetime] = None,
        api_key: Optional[str] = None,
        parameters: Dict[str, Any] = None,
        **kwargs,
    ):
        self._id = id
        self._timestamp = timestamp
        self._entries = kwargs
        self._parameters = parameters
        self._api_key = _validate_api_key(api_key)

    # Properties

    @property
    def id(self) -> int:
        return self._id

    @property
    def timestamp(self) -> Optional[datetime]:
        return self._timestamp

    @property
    def entries(self) -> Dict[str, Any]:
        return self._entries

    @property
    def parameters(self) -> Dict[str, Any]:
        return self._parameters

    # Dunders

    def __eq__(self, other: Union[dict, Log]) -> bool:
        if isinstance(other, dict):
            other = Log(other["id"], **other["entries"])
        return self._id == other._id

    def __len__(self):
        return len(self._entries)

    def __repr__(self) -> str:
        return f"Log(id={self._id})"

    # Public

    def download(self):
        self._entries = get_log_by_id(self._id, self._api_key)._entries

    def add_entries(self, **kwargs) -> None:
        add_log_entries(self._id, api_key=self._api_key, **kwargs)
        self._entries = {**self._entries, **kwargs}

    def replace_entries(self, **kwargs) -> None:
        replace_log_entries(self._id, self._api_key, **kwargs)
        self._entries = {**self._entries, **kwargs}

    def update_entries(self, fn, **kwargs) -> None:
        update_log_entries(fn, self._id, self._api_key, **kwargs)
        for k, v in kwargs.items():
            self._entries[k] = fn(self._entries[k], v)

    def rename_entries(self, **kwargs) -> None:
        rename_log_entries(self._id, self._api_key, **kwargs)
        for old_name, new_name in kwargs.items():
            self._entries[new_name] = self._entries[old_name]
            del self._entries[old_name]

    def delete_entries(
        self,
        keys_to_delete: List[str],
    ) -> None:
        for key in keys_to_delete:
            delete_log_entry(key, self._id, self._api_key)
            del self._entries[key]

    def delete(self) -> None:
        delete_log(self._id, self._api_key)

    def to_json(self):
        return {
            "id": self._id,
            "timestamp": self._timestamp,
            "entries": self._entries,
            "parameters": self._parameters,
            "api_key": self._api_key,
        }

    @staticmethod
    def from_json(state):
        entries = state["entries"]
        del state["entries"]
        state = {**state, **entries}
        return Log(**state)


class Context:
    def __init__(self, **kwargs):
        self.kwargs = _handle_special_types(kwargs)

    def __enter__(self):
        self.token = current_global_active_log_kwargs.set(
            {**current_global_active_log_kwargs.get(), **self.kwargs},
        )
        self.nest_level_token = current_context_nest_level.set(
            current_context_nest_level.get() + 1,
        )

    def __exit__(self, *args, **kwargs):
        # print("Before clearing", current_global_active_log_kwargs.get())
        current_global_active_log_kwargs.reset(self.token)
        current_context_nest_level.reset(self.nest_level_token)
        if current_context_nest_level.get() == 0:
            current_logged_logs.set({})


def span(io=True):
    def wrapper(fn):
        def wrapped(*args, **kwargs):
            t1 = time.perf_counter()
            if not current_span.get():
                running_time.set(t1)
            inputs = None
            if io:
                signature = inspect.signature(fn)
                bound_args = signature.bind(*args, **kwargs)
                bound_args.apply_defaults()
                inputs = bound_args.arguments
            new_span = {
                "id": str(uuid.uuid4()),
                "parent_span_id": (
                    None if not current_span.get() else current_span.get()["id"]
                ),
                "span_name": fn.__name__,
                "exec_time": None,
                "offset": round(
                    0.0 if not current_span.get() else t1 - running_time.get(),
                    2,
                ),
                "inputs": inputs,
                "outputs": None,
                "errors": None,
                "child_spans": [],
            }
            token = current_span.set(new_span)
            result = None
            try:
                result = fn(*args, **kwargs)
                return result
            except Exception as e:
                new_span["errors"] = str(e)
                raise e
            finally:
                t2 = time.perf_counter()
                exec_time = t2 - t1
                current_span.get()["exec_time"] = round(exec_time, 2)
                current_span.get()["outputs"] = (
                    None if result is None or not io else result
                )
                if token.old_value is token.MISSING:
                    unify.log(trace=current_span.get(), skip_duplicates=False)
                    current_span.reset(token)
                else:
                    current_span.reset(token)
                    current_span.get()["child_spans"].append(new_span)

        async def async_wrapped(*args, **kwargs):
            t1 = time.perf_counter()
            if not current_span.get():
                running_time.set(t1)
            inputs = None
            if io:
                signature = inspect.signature(fn)
                bound_args = signature.bind(*args, **kwargs)
                bound_args.apply_defaults()
                inputs = bound_args.arguments
            new_span = {
                "id": str(uuid.uuid4()),
                "parent_span_id": (
                    None if not current_span.get() else current_span.get()["id"]
                ),
                "span_name": fn.__name__,
                "exec_time": None,
                "offset": round(
                    0.0 if not current_span.get() else t1 - running_time.get(),
                    2,
                ),
                "inputs": inputs,
                "outputs": None,
                "errors": None,
                "child_spans": [],
            }
            token = current_span.set(new_span)
            # capture the arguments here
            result = None
            try:
                result = await fn(*args, **kwargs)
                return result
            except Exception as e:
                new_span["errors"] = str(e)
                raise e
            finally:
                t2 = time.perf_counter()
                exec_time = t2 - t1
                current_span.get()["exec_time"] = round(exec_time, 2)
                current_span.get()["outputs"] = (
                    None if result is None or not io else result
                )
                if token.old_value is token.MISSING:
                    unify.log(trace=current_span.get(), skip_duplicates=False)
                    current_span.reset(token)
                else:
                    current_span.reset(token)
                    current_span.get()["child_spans"].append(new_span)

        return wrapped if not inspect.iscoroutinefunction(fn) else async_wrapped

    return wrapper
