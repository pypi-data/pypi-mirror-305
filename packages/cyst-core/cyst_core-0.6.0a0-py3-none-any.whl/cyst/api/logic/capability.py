from enum import IntEnum, auto


class CapabilityType(IntEnum):
    ACCESS_FILESYS_GENERIC = auto()
    ACCESS_FILESYS_ELEVATED = auto()  # e.g access to /root/, %WINDIR%, ...
    ACCESS_FILESYS_SHARED = auto()  # shares (SMB, FTP ... )

    FILESYS_READ = auto()
    FILESYS_WRITE = auto()

    ACCESS_NETWORK_DOMAIN = (
        auto()
    )  # this privilege is not present for local services in Windows systems, so they are not able to auth in the domain
    # TODO: an authed exploit action usage without creds but this - but only for very specific services -> so maybe a separate action

    ACCOUNT_MANIPULATION_USER_ADD = auto()
    ACCOUNT_MANIPULATION_USER_EDIT = auto()
    ACCOUNT_MANIPULATION_USER_DELETE = auto()

    PERSIST_LOG_OUT = auto()  # guest users do not have this, their files / registries are cleaned upon logout

    EXECUTE_CODE = auto()  # includes commands, scheduled tasks, interacting with the registry

    SHUTDOWN = auto()
    DOMAIN_LOGIN = auto()

    PERSISTENCE = auto()

    IMPERSONATE = auto()  # e.g. send mails in the users name, etc.

    CONTROL_DOMAIN = auto()
    CONFIG_LOCAL_MACHINE = auto()  # e.g tamper with HKLM registry, global $ENV
    CONFIG_LOCAL_USER = auto()  # e.g. tamper with HKCU registry, user $ENV

    SE_DEBUG = auto()
    SE_LOAD_DRIVER = auto()
    SE_CREATE_SECURITY_TOKEN = auto()
    SE_TOKEN_IMPERSONATE = auto()
    UAC_ELEVATE = auto()
