# from sqlalchemy.orm import DeclarativeBase
# from typing import List, Optional
# from sqlalchemy import String, ForeignKey, create_engine, MetaData
# from sqlalchemy.orm import Mapped, Session, mapped_column, relationship


# class Base(DeclarativeBase):
#     pass


# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# metadata_obj = MetaData()


# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(back_populates="user")

#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped[User] = relationship(back_populates="addresses")

#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# metadata_obj.create_all(engine)

# squidward = User(name="squidward", fullname="Squidward Tentacles")
# krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")

# session = Session(engine)
# session.add(squidward)
# session.add(krabs)
# session.flush()


# from sqlalchemy import ForeignKey, MetaData
# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import Session

# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# metadata_obj = MetaData()

# user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String),
# )

# address_table = Table(
#     "address",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", Integer, ForeignKey("user_account.id"), nullable=False),
#     Column("email_adress", String, nullable=False),
# )

# metadata_obj.create_all(engine)


# with engine.begin() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [
#             {"x": 6, "y": 3},
#             {"x": 9, "y": 6},
#             {"x": 1, "y": 1},
#             {"x": 2, "y": 5},
#             {"x": 3, "y": 2},
#         ],
#     )
#     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
#     for row in result:
#         print(f"x: {row.x} y: {row.y}")

# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
# with Session(engine) as session:
#     result = session.execute(stmt, {"y": 0})
#     for row in result:
#         print(f"x: {row.x}, y: {row.y}")
