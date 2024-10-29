from Application.Abstractions.base_composit import BaseComposit
from Application.Abstractions.base_message import BaseMessage
from Application.Abstractions.base_random_uuid import BaseRandomGUID
from examples.Domain.Enums.enum_type_message import EnumTypeMessage
from fwdi.Infrastructure.Configs.rest_client_config import RestClientConfig


class GenerateUuidAndPrint(BaseComposit):
    def __init__(self, rnd: BaseRandomGUID, config:RestClientConfig, msg: BaseMessage) -> None:
        super().__init__()
        self.__rnd:BaseRandomGUID = rnd
        self.__msg:BaseMessage = msg
        self.__config:RestClientConfig = config

    def run_once(self)->BaseMessage:
        rnd_uuid = self.__rnd.get_id()
        message_text = f"""Try generate random UUID:
{rnd_uuid.__str__()},
Rest client config:
    Server:{self.__config.server}
    Port:{self.__config.port}
    Security:{self.__config.security_layer}
    Username:{self.__config.username}
"""
        self.__msg.set_msg(msg=message_text, msg_type=EnumTypeMessage.Normal)
        self.__msg.show_message()

        return self.__msg