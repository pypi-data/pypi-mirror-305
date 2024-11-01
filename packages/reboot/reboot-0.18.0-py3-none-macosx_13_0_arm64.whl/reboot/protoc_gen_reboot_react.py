#!/usr/bin/env python3
import os
from dataclasses import dataclass
from google.protobuf.descriptor_pb2 import FileDescriptorProto
from reboot.cli import terminal
from reboot.protoc_gen_reboot_generic import (
    BaseFile,
    BaseMethod,
    BaseMethodOptions,
    BaseService,
    BaseServiceOptions,
    PluginSpecificData,
    ProtoType,
    UserProtoError,
)
from reboot.protoc_gen_reboot_typescript import TypescriptRebootProtocPlugin
from reboot.settings import ENVVAR_REBOOT_REACT_EXTENSIONLESS
from typing import Sequence

ReactType = str


@dataclass
class ReactMethodOptions(BaseMethodOptions):
    errors: dict[ProtoType, ReactType]


@dataclass
class ReactMethod(BaseMethod):
    options: ReactMethodOptions
    input_type: ReactType
    output_type: ReactType


@dataclass
class ReactService(BaseService):
    methods: Sequence[ReactMethod]


@dataclass
class ReactFile(BaseFile):
    services: Sequence[ReactService]
    # Dictionary where the key is the relative path to the
    # file and the value is the unique name of the file.
    imports: dict[str, str]
    # The name of the ES module, which contains the generated protobuf
    # messages ("*_pb.js").
    pb_name: str
    # Set of messages that are used in the file and should be imported from
    # '@bufbuild/protobuf'.
    google_protobuf_used_messages: set[str]
    # Whether or not to emit .js extensions.
    react_extensionless: bool


class ReactRebootProtocPlugin(TypescriptRebootProtocPlugin):

    @staticmethod
    def plugin_specific_data() -> PluginSpecificData:
        return PluginSpecificData(
            template_filename="reboot_react.ts.j2",
            output_filename_suffix="_rbt_react.ts",
            supported_features=[
                "reader",
                "writer",
                "transaction",
                "error",
                "streaming",
                "workflow",
            ],
        )

    def plugin_template_data(
        self, proto_file: FileDescriptorProto
    ) -> BaseFile:
        file = self.pool.FindFileByName(proto_file.name)

        state_names = self._proto_state_names(file)

        reboot_services = self._proto_reboot_services(
            file,
            self._proto_state_names(file),
        )

        proto = self._analyze_proto_file(file)

        services: Sequence[ReactService] = [
            ReactService(
                proto=self._analyze_proto_service(
                    service,
                    file.services_by_name[service.name],
                ),
                methods=[
                    ReactMethod(
                        proto=self._analyze_proto_method(method),
                        options=ReactMethodOptions(
                            proto=self._analyze_proto_method_options(
                                file.services_by_name[
                                    service.name].methods_by_name[method.name],
                                method.client_streaming or
                                method.server_streaming
                            ),
                            errors=self._analyze_errors(
                                file.services_by_name[
                                    service.name].methods_by_name[method.name],
                                state_names=state_names,
                            ),
                        ),
                        input_type=self._get_typescript_type_from_proto_type(
                            file.services_by_name[service.name].
                            methods_by_name[method.name].input_type,
                            file,
                            state_names=state_names,
                            messages_and_enums=proto.messages_and_enums,
                        ),
                        output_type=self._get_typescript_type_from_proto_type(
                            file.services_by_name[service.name].
                            methods_by_name[method.name].output_type,
                            file,
                            state_names=state_names,
                            messages_and_enums=proto.messages_and_enums,
                        ),
                    ) for method in service.method
                ],
                options=BaseServiceOptions(
                    proto=self._analyze_proto_service_options(
                        file.services_by_name[service.name]
                    ),
                ),
            ) for service in reboot_services
        ]

        react_file: BaseFile = ReactFile(
            proto=proto,
            services=services,
            imports=self._analyze_imports(file),
            pb_name=self._get_pb_file_name(file),
            google_protobuf_used_messages=self.
            _get_google_protobuf_messages(file),
            react_extensionless=os.environ.get(
                ENVVAR_REBOOT_REACT_EXTENSIONLESS, "false"
            ).lower() == "true",
        )

        return react_file


# This is a separate function (rather than just being in `__main__`) so that we
# can refer to it as a `script` in our `pyproject.rbt.toml` file.
def main():
    try:
        ReactRebootProtocPlugin.execute()
    except UserProtoError as error:
        terminal.fail(str(error))


if __name__ == '__main__':
    main()
