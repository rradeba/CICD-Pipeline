from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer

class Base(DeclarativeBase):
    pass

class Sum(Base):
    __tablename__ = 'sums'

    id: Mapped[int] = mapped_column(primary_key=True)
    num1: Mapped[int] = mapped_column(Integer, nullable=False)
    num2: Mapped[int] = mapped_column(Integer, nullable=False)
    result: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f"<Sum {self.id}: {self.num1} + {self.num2} = {self.result}>"
