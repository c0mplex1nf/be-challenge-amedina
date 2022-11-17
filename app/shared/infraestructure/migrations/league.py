from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey

def createTable(metadata):
    league = Table(
        "league",
        metadata,
        Column("id", String(255), primary_key=True, nullable=False),
        Column("name", String(255), nullable=True),
        Column("code", String(255), nullable=True),
        Column("area_name", String(255), nullable=True),
    )

    return league
