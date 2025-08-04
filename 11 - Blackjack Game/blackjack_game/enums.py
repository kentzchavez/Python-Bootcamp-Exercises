from enum import IntEnum

class BlackjackResult(IntEnum):
    """Determines blackjack checker results"""
    USER_WIN = 1
    DEALER_WIN = 2
    TIE = 3
    CONTINUE = 0
