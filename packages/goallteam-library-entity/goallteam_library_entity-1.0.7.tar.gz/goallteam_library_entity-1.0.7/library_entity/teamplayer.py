"""Module Entity TeamPlayer"""
from sqlalchemy import  Integer,  PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class TeamPlayer(Base):
    """Entity TEAM_PLAYER"""
    __tablename__ = 'TEAM_PLAYER'
    player_id: Mapped[int] = mapped_column(Integer, ForeignKey('PLAYER.UUID'), name='PLAYER_ID')
    team_id: Mapped[int] = mapped_column(Integer, ForeignKey('TEAM.UUID'), nullable=False, name='TEAM_ID')



    __table_args__ = (
        PrimaryKeyConstraint('PLAYER_ID', 'TEAM_ID', name='team_player_pk'),
    )