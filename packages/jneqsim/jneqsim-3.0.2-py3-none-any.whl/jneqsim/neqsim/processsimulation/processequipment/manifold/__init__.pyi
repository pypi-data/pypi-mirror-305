
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import jneqsim.neqsim.processsimulation.processequipment
import jneqsim.neqsim.processsimulation.processequipment.stream
import typing



class Manifold(jneqsim.neqsim.processsimulation.processequipment.ProcessEquipmentBaseClass):
    def __init__(self, string: typing.Union[java.lang.String, str]): ...
    def addStream(self, streamInterface: jneqsim.neqsim.processsimulation.processequipment.stream.StreamInterface) -> None: ...
    def getMixedStream(self) -> jneqsim.neqsim.processsimulation.processequipment.stream.StreamInterface: ...
    def getSplitStream(self, int: int) -> jneqsim.neqsim.processsimulation.processequipment.stream.StreamInterface: ...
    @typing.overload
    def run(self) -> None: ...
    @typing.overload
    def run(self, uUID: java.util.UUID) -> None: ...
    def setName(self, string: typing.Union[java.lang.String, str]) -> None: ...
    def setSplitFactors(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("jneqsim.neqsim.processsimulation.processequipment.manifold")``.

    Manifold: typing.Type[Manifold]
