from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
from .. import initialize_nltk


def calculate_bleu(reference: str, candidate: str) -> float:
    """
    Calculate BLEU score for a candidate summary against a reference text.
    Args:
        reference: The ground truth text
        candidate: The text to evaluate
    Returns:
        float: BLEU score between 0 and 1
    """
    # Ensure NLTK is initialized before calculating scores
    initialize_nltk()

    # Tokenize both texts
    reference_tokens = [
        word_tokenize(reference.lower())
    ]  # Must be a list of references
    candidate_tokens = word_tokenize(candidate.lower())

    # Use custom weights to focus more on unigram and bigram matches
    # (1-gram, 2-gram, 3-gram, 4-gram)
    weights = (0.25, 0.25, 0.25, 0.25)

    return sentence_bleu(
        reference_tokens,
        candidate_tokens,
        weights=weights,
        smoothing_function=None,  # You can import SmoothingFunction for better handling of edge cases
    )
