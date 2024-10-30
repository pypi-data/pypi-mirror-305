from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ModelStatus]
    DISK: _ClassVar[ModelStatus]
    RAM: _ClassVar[ModelStatus]
    GPU: _ClassVar[ModelStatus]
    REMOTE: _ClassVar[ModelStatus]
UNKNOWN: ModelStatus
DISK: ModelStatus
RAM: ModelStatus
GPU: ModelStatus
REMOTE: ModelStatus

class GetModelStatusesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetModelStatusesResponse(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ModelState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelState, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, ModelState]
    def __init__(self, map: _Optional[_Mapping[str, ModelState]] = ...) -> None: ...

class ModelState(_message.Message):
    __slots__ = ("model_size", "status", "last_used")
    MODEL_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_FIELD_NUMBER: _ClassVar[int]
    model_size: int
    status: ModelStatus
    last_used: int
    def __init__(self, model_size: _Optional[int] = ..., status: _Optional[_Union[ModelStatus, str]] = ..., last_used: _Optional[int] = ...) -> None: ...

class LoadToRamRequest(_message.Message):
    __slots__ = ("model_name", "model_files")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FILES_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model_name: _Optional[str] = ..., model_files: _Optional[_Iterable[str]] = ...) -> None: ...

class UnloadFromRamRequest(_message.Message):
    __slots__ = ("model_name",)
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    def __init__(self, model_name: _Optional[str] = ...) -> None: ...

class LoadToGpuRequest(_message.Message):
    __slots__ = ("model_name", "model_files", "device_tensor_memory_layout", "ipc_handles")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FILES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TENSOR_MEMORY_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    IPC_HANDLES_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_files: _containers.RepeatedScalarFieldContainer[str]
    device_tensor_memory_layout: DeviceTensorMemoryLayout
    ipc_handles: IpcHandles
    def __init__(self, model_name: _Optional[str] = ..., model_files: _Optional[_Iterable[str]] = ..., device_tensor_memory_layout: _Optional[_Union[DeviceTensorMemoryLayout, _Mapping]] = ..., ipc_handles: _Optional[_Union[IpcHandles, _Mapping]] = ...) -> None: ...

class OffloadToRamRequest(_message.Message):
    __slots__ = ("model_name", "cuda_tensors")
    class CudaTensorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CudaTensor
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CudaTensor, _Mapping]] = ...) -> None: ...
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CUDA_TENSORS_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    cuda_tensors: _containers.MessageMap[str, CudaTensor]
    def __init__(self, model_name: _Optional[str] = ..., cuda_tensors: _Optional[_Mapping[str, CudaTensor]] = ...) -> None: ...

class WriteToDiskRequest(_message.Message):
    __slots__ = ("model_name", "model_files", "device_tensor_memory_layout", "ipc_handles")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FILES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TENSOR_MEMORY_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    IPC_HANDLES_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_files: _containers.RepeatedScalarFieldContainer[str]
    device_tensor_memory_layout: DeviceTensorMemoryLayout
    ipc_handles: IpcHandles
    def __init__(self, model_name: _Optional[str] = ..., model_files: _Optional[_Iterable[str]] = ..., device_tensor_memory_layout: _Optional[_Union[DeviceTensorMemoryLayout, _Mapping]] = ..., ipc_handles: _Optional[_Union[IpcHandles, _Mapping]] = ...) -> None: ...

class TensorTransportRequestResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class IpcHandles(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IpcHandle
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IpcHandle, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, IpcHandle]
    def __init__(self, map: _Optional[_Mapping[str, IpcHandle]] = ...) -> None: ...

class IpcHandle(_message.Message):
    __slots__ = ("mem_handle", "size")
    MEM_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    mem_handle: str
    size: int
    def __init__(self, mem_handle: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class CudaTensor(_message.Message):
    __slots__ = ("uuid", "ipc_handle", "dtype", "shape")
    UUID_FIELD_NUMBER: _ClassVar[int]
    IPC_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    ipc_handle: IpcHandle
    dtype: str
    shape: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, uuid: _Optional[str] = ..., ipc_handle: _Optional[_Union[IpcHandle, _Mapping]] = ..., dtype: _Optional[str] = ..., shape: _Optional[_Iterable[int]] = ...) -> None: ...

class DeviceTensorMemoryLayout(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TensorMemoryLayout
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TensorMemoryLayout, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, TensorMemoryLayout]
    def __init__(self, map: _Optional[_Mapping[str, TensorMemoryLayout]] = ...) -> None: ...

class TensorMemoryLayout(_message.Message):
    __slots__ = ("map",)
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TensorMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TensorMetadata, _Mapping]] = ...) -> None: ...
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.MessageMap[str, TensorMetadata]
    def __init__(self, map: _Optional[_Mapping[str, TensorMetadata]] = ...) -> None: ...

class TensorMetadata(_message.Message):
    __slots__ = ("dtype", "shape", "offsets")
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    OFFSETS_FIELD_NUMBER: _ClassVar[int]
    dtype: str
    shape: _containers.RepeatedScalarFieldContainer[int]
    offsets: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dtype: _Optional[str] = ..., shape: _Optional[_Iterable[int]] = ..., offsets: _Optional[_Iterable[int]] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("id", "tag", "quantization", "status", "size", "last_used")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    QUANTIZATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_FIELD_NUMBER: _ClassVar[int]
    id: str
    tag: str
    quantization: str
    status: ModelStatus
    size: str
    last_used: str
    def __init__(self, id: _Optional[str] = ..., tag: _Optional[str] = ..., quantization: _Optional[str] = ..., status: _Optional[_Union[ModelStatus, str]] = ..., size: _Optional[str] = ..., last_used: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("show_all",)
    SHOW_ALL_FIELD_NUMBER: _ClassVar[int]
    show_all: bool
    def __init__(self, show_all: bool = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class PullModelRequest(_message.Message):
    __slots__ = ("model_id", "tag", "quantization")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    QUANTIZATION_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    tag: str
    quantization: str
    def __init__(self, model_id: _Optional[str] = ..., tag: _Optional[str] = ..., quantization: _Optional[str] = ...) -> None: ...

class PullModelResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class RemoveModelRequest(_message.Message):
    __slots__ = ("model_id", "tag")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    tag: str
    def __init__(self, model_id: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class RemoveModelResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetModelInfoRequest(_message.Message):
    __slots__ = ("model_id", "tag")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    tag: str
    def __init__(self, model_id: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class GetModelInfoResponse(_message.Message):
    __slots__ = ("model_id", "registry", "description", "created_at", "available_tags", "available_quantizations", "default_quantization", "size", "estimated_vram")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TAGS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QUANTIZATION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_VRAM_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    registry: str
    description: str
    created_at: str
    available_tags: _containers.RepeatedScalarFieldContainer[str]
    available_quantizations: _containers.RepeatedScalarFieldContainer[str]
    default_quantization: str
    size: str
    estimated_vram: str
    def __init__(self, model_id: _Optional[str] = ..., registry: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[str] = ..., available_tags: _Optional[_Iterable[str]] = ..., available_quantizations: _Optional[_Iterable[str]] = ..., default_quantization: _Optional[str] = ..., size: _Optional[str] = ..., estimated_vram: _Optional[str] = ...) -> None: ...

class UpdateModelStatusRequest(_message.Message):
    __slots__ = ("model_id", "tag", "new_status")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    tag: str
    new_status: ModelStatus
    def __init__(self, model_id: _Optional[str] = ..., tag: _Optional[str] = ..., new_status: _Optional[_Union[ModelStatus, str]] = ...) -> None: ...

class UpdateModelStatusResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
