from abc import ABC, abstractmethod
from typing import List, Optional
from ..models.paper import Bookmark, UserInteraction

class IUserRepository(ABC):

    @abstractmethod
    def get_user_bookmarks(self, user_id: str) -> List[Bookmark]:
        pass

    @abstractmethod
    def add_bookmark(self, bookmark: Bookmark) -> bool:
        pass

    @abstractmethod
    def remove_bookmark(self, user_id: str, paper_id: str) -> bool:
        pass

    @abstractmethod
    def get_user_interactions(self, user_id: str) -> List[UserInteraction]:
        pass

    @abstractmethod
    def save_user_interaction(self, interaction: UserInteraction) -> bool:
        pass

    @abstractmethod
    def get_user_preferences(self, user_id: str) -> dict:
        pass

    @abstractmethod
    def update_user_preferences(self, user_id: str, preferences: dict) -> bool:
        pass

class UserRepository(IUserRepository):

    def __init__(self, db_connection):
        pass

    def get_user_bookmarks(self, user_id: str) -> List[Bookmark]:
        pass

    def add_bookmark(self, bookmark: Bookmark) -> bool:
        pass

    def remove_bookmark(self, user_id: str, paper_id: str) -> bool:
        pass

    def get_user_interactions(self, user_id: str) -> List[UserInteraction]:
        pass

    def save_user_interaction(self, interaction: UserInteraction) -> bool:
        pass

    def get_user_preferences(self, user_id: str) -> dict:
        pass

    def update_user_preferences(self, user_id: str, preferences: dict) -> bool:
        pass