from enum import Enum


class GetScriptByPathWithDraftResponse200DraftLanguage(str, Enum):
    ANSIBLE = "ansible"
    BASH = "bash"
    BIGQUERY = "bigquery"
    BUN = "bun"
    DENO = "deno"
    GO = "go"
    GRAPHQL = "graphql"
    MSSQL = "mssql"
    MYSQL = "mysql"
    NATIVETS = "nativets"
    PHP = "php"
    POSTGRESQL = "postgresql"
    POWERSHELL = "powershell"
    PYTHON3 = "python3"
    RUST = "rust"
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
