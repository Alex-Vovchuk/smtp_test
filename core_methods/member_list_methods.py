from configuration.members_list_config import MemberListConfig
from src.endpoint_base_class import EndpointBaseclass
from src.methods_base_сlass import MethodsBaseClass

MemberList = EndpointBaseclass(MemberListConfig().BASE_URL, MethodsBaseClass.get)

get_members_list = MemberList
