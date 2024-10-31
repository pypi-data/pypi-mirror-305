from typing import Any, Dict, Optional, Union

from ..exceptions import ParserError, PatternError
from ..payloads.encryption import EncryptionRegistry
from ..payloads.inputs import (
    JsonLogPatternPayload,
    LogFormat,
    RawTextLogPatternPayload,
)
from ..payloads.transformations import (
    TransformationRegistry,
    TransformationType,
)
from ..payloads.types import ParsedLogEntry
from ..utils.factory import create_parser


class LogParser:
    def __init__(self, encryption_key: Optional[str] = None):
        """
        Initializes the log parser with an empty dictionary of patterns
        """
        self.patterns: Dict[int, Dict[str, Any]] = {}
        self.encryption = EncryptionRegistry(encryption_key)
        self.transformations = TransformationRegistry()

    def add_pattern(self, pattern_dict: Dict[str, Any]) -> None:  # noqa: C901, PLR0912
        """
        Accepts dictionary for both: RawTextLogPatternPayload, JsonLogPatternPayload
        """
        pattern: Union[RawTextLogPatternPayload, JsonLogPatternPayload]
        log_format_str = pattern_dict["log_format"].lower()

        try:
            if log_format_str == LogFormat.RAW_TEXT:
                pattern = RawTextLogPatternPayload(**pattern_dict)
            elif log_format_str == LogFormat.JSON:
                pattern = JsonLogPatternPayload(**pattern_dict)
            else:
                raise PatternError(
                    f"Invalid log format {log_format_str}, "
                    f"use 'raw_text' or 'json_dict'"
                )

            if pattern.version in self.patterns:
                raise PatternError(f"Pattern version {pattern.version} already exists")

            for field in pattern.fields:
                if field.transformation:
                    try:
                        if field.transformation_type == TransformationType.EXPRESSION:
                            self.transformations.validate_expression(
                                field.transformation
                            )
                        elif field.transformation_type == TransformationType.FUNCTION:
                            if (
                                field.transformation
                                not in self.transformations._processors
                            ):
                                raise ValueError(
                                    f"Unknown function transformation: {field.transformation}"
                                )
                    except ValueError as e:
                        raise PatternError(
                            f"Invalid transformation for field {field.key}: {e!s}"
                        )

            parser = create_parser(pattern, transformations=self.transformations)
            self.patterns[pattern.version] = {
                "parser": parser,
                "fields": {field.key: field for field in pattern.fields},
            }
        except Exception as e:
            raise PatternError(f"Error adding pattern: {e!s}")

    def parse_log(
        self, log: Union[str, Dict[str, Any]], version: int
    ) -> ParsedLogEntry:
        if version not in self.patterns:
            raise ParserError(f"Unknown pattern version: {version}")

        pattern = self.patterns[version]
        parser = pattern["parser"]
        fields = pattern["fields"]

        try:
            parsed_fields = parser.parse(log, fields)

            for field_key, field_def in fields.items():

                if field_key in parsed_fields and field_def.encryption:
                    parsed_fields[field_key] = self.encryption.encrypt(
                        str(parsed_fields[field_key])
                    )

            return ParsedLogEntry(version=version, parsed_fields=parsed_fields)
        except Exception as e:
            raise ParserError(f"Error parsing log: {e!s}") from e

    def decrypt_field(self, value: str) -> str:
        """
        Decrypt an encrypted field value
        """
        return self.encryption.decrypt(value)
