from model.creature import Creature

#데이터베이스와 SQL로 바꿀 때 까지 사용할 가짜 데이터
_cretures = [
    Creature(name = "Yeti",
        aka = "Abominable Snowman",
        country = "CN",
        area = "Himalayas",
        description = "Hirsute Himalayan"
        ),

    Creature(name = "Bigfoot",
        description = "Yeti's Cousin Eddie",
        country = "US",
        area = "*",
        aka = "Sasquatch"),
]

def get_all() -> list[Creature]:
    """생명체의 목록을 반환한다."""
    return _cretures

def get_one(name : str) -> Creature | None:
    """검색한 생명체를 반환한다."""
    for _creture in _cretures:
        if _creture.name == name:
            return _creture
    return None


# 다음 함수는 작동하지 않는다.

def create(creature : Creature) -> Creature:
    """생명체를 추가한다."""
    return creature

def modify(name : str, creature : Creature) -> Creature:
    """생명체의 일부 정보를 수정한다."""
    return creature

def replace(name : str, creature : Creature) -> Creature:
    """생명체를 완전히 교체한다."""
    return creature

def delete(name : str) -> bool:
    """생명체를 삭제한다. 만약 대상이 없다면 False를 반환한다."""
    for _creture in _cretures:
        if _creture.name == name:
            return True
    return False


