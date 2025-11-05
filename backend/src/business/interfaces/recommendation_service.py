from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from ...data.models.paper import Paper

class IRecommendationService(ABC):

    @abstractmethod
    def get_personalized_recommendations(self, user_id: str, limit: int = 10) -> List[Paper]:
        pass

    @abstractmethod
    def get_content_based_recommendations(self, paper_id: str, limit: int = 10) -> List[Paper]:
        pass

    @abstractmethod
    def get_trending_papers(self, category: Optional[str] = None, limit: int = 10) -> List[Paper]:
        pass

    @abstractmethod
    def get_paper_of_the_week(self, category: Optional[str] = None) -> Paper:
        pass

    @abstractmethod
    def calculate_similarity_score(self, paper1_id: str, paper2_id: str) -> float:
        pass

    @abstractmethod
    def update_user_preferences(self, user_id: str, paper_interactions: List[Dict[str, Any]]) -> bool:
        pass