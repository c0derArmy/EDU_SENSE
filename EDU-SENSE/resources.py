"""
Resource links management for learning gap recommendations.
Contains subject-specific educational resources.
"""

SUBJECT_RESOURCES = {
    'social science': [
        'https://ncert.nic.in/',
        'https://byjus.com/'
    ],
    'computer science': [
        'https://www.geeksforgeeks.org/'
    ],
    'english': [
        'https://learnenglish.britishcouncil.org/'
    ],
    'maths': [
        'https://www.khanacademy.org/math/'
    ],
    'hindi': [
        'http://tiwariacademy.com/ncert-solutions/',  # Hindi literature
        'https://www.tiwariacademy.com/ncert-solutions/%20hindigrammar/'  # Hindi grammar
    ],
    'science': [
        'https://www.khanacademy.org/science/board-preparation-class-10'
    ],
    'arithmetic': [
        'https://www.khanacademy.org/math/'
    ],
    'fractions': [
        'https://www.khanacademy.org/math/'
    ],
    'algebra': [
        'https://www.khanacademy.org/math/'
    ],
    'geometry': [
        'https://www.khanacademy.org/math/'
    ],
    'data analysis': [
        'https://www.khanacademy.org/math/'
    ]
}


def get_resources_for_topic(topic: str) -> list:
    """
    Get resource links for a specific topic/subject.
    
    Args:
        topic: The topic/subject name
        
    Returns:
        List of resource URLs for the topic
    """
    if not topic:
        return []
    
    topic_lower = topic.lower().strip()
    
    # Direct match
    if topic_lower in SUBJECT_RESOURCES:
        return SUBJECT_RESOURCES[topic_lower]
    
    # Partial match (check if topic contains any key)
    for subject, resources in SUBJECT_RESOURCES.items():
        if subject in topic_lower or topic_lower in subject:
            return resources
    
    # Default to general resources if no match
    return []


def get_all_resources() -> dict:
    """Get all available resources"""
    return SUBJECT_RESOURCES
