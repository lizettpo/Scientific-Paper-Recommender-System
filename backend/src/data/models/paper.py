from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime

@dataclass
class Author:
    name: str
    affiliation: Optional[str] = None
    email: Optional[str] = None

@dataclass
class Paper:
    id: str
    title: str
    abstract: str
    authors: List[Author]
    published_date: datetime
    arxiv_id: Optional[str] = None
    doi: Optional[str] = None
    categories: List[str]
    keywords: List[str]
    pdf_url: Optional[str] = None
    citation_count: int = 0
    embedding: Optional[List[float]] = None

@dataclass
class Citation:
    paper_id: str
    cited_paper_id: str
    context: Optional[str] = None

@dataclass
class UserInteraction:
    user_id: str
    paper_id: str
    interaction_type: str
    timestamp: datetime
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class Bookmark:
    id: str
    user_id: str
    paper_id: str
    created_at: datetime
    notes: Optional[str] = None