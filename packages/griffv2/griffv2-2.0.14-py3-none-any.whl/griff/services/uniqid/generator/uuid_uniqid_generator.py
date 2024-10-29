from uuid import uuid4

from griff.services.uniqid.generator.uniqid_generator import (
    UniqIdGenerator,
)


class UuidUniqIdGenerator(UniqIdGenerator):
    def next_id(self) -> str:
        return str(uuid4())

    def reset(self, start_id: int = 1) -> None:  # pragma: no cover
        pass
