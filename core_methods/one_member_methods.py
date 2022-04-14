from configuration.one_member_config import OneMemberConfig
from src.endpoint_base_class import EndpointBaseclass
from src.methods_base_сlass import MethodsBaseClass

OneMember = EndpointBaseclass(OneMemberConfig().BASE_URL, MethodsBaseClass.get)

get_one_member_info = OneMember
