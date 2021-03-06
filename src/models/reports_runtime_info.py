from sqlalchemy import Column, Integer, ForeignKey, Boolean, Float, String

from database import Base


class ReportsRuntimeInfo(Base):
    __tablename__ = 'reports_runtime_infos'

    id = Column(Integer, primary_key=True)
    step_id = Column(Integer, ForeignKey('steps.id'))
    is_finished = Column(Boolean)
    progress = Column(Float)
    error = Column(String)

    def __json__(self):
        return ['progress', 'error']
y