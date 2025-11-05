from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from ..models.paper import Paper, Citation, Bookmark, UserInteraction

class IPaperRepository(ABC):

    @abstractmethod
    def get_paper_by_id(self, paper_id: str) -> Optional[Paper]:
        pass

    @abstractmethod
    def get_papers_by_category(self, category: str, limit: int = 20) -> List[Paper]:
        pass

    @abstractmethod
    def search_papers(self, query: str, filters: Dict[str, Any] = None) -> List[Paper]:
        pass

    @abstractmethod
    def save_paper(self, paper: Paper) -> bool:
        pass

    @abstractmethod
    def update_paper(self, paper: Paper) -> bool:
        pass

    @abstractmethod
    def delete_paper(self, paper_id: str) -> bool:
        pass

    @abstractmethod
    def get_paper_citations(self, paper_id: str) -> List[Citation]:
        pass

    @abstractmethod
    def get_papers_by_author(self, author_name: str) -> List[Paper]:
        pass

    @abstractmethod
    def get_similar_papers(self, paper_id: str, limit: int = 10) -> List[Paper]:
        pass

class PaperRepository(IPaperRepository):

    def __init__(self, db_connection):
        pass

    def get_paper_by_id(self, paper_id: str) -> Optional[Paper]:
        pass

    def get_papers_by_category(self, category: str, limit: int = 20) -> List[Paper]:
        pass

    def search_papers(self, query: str, filters: Dict[str, Any] = None) -> List[Paper]:
        pass

    def save_paper(self, paper: Paper) -> bool:
        pass

    def update_paper(self, paper: Paper) -> bool:
        pass

    def delete_paper(self, paper_id: str) -> bool:
        pass

    def get_paper_citations(self, paper_id: str) -> List[Citation]:
        pass

    def get_papers_by_author(self, author_name: str) -> List[Paper]:
        pass

    def get_similar_papers(self, paper_id: str, limit: int = 10) -> List[Paper]:
        pass