"""A deterministic, dependency-free example of a safe agent control loop."""

import argparse
import json
from typing import Dict, List


MAX_INPUT_LENGTH = 2_000
CATEGORIES = {"question", "bug", "other"}

BUG_WORDS = (
    "error",
    "bug",
    "broken",
    "crash",
    "doesn't",
    "does not",
    "nothing happens",
    "エラー",
    "不具合",
    "クラッシュ",
    "動かない",
    "反応しません",
    "できません",
)

QUESTION_WORDS = (
    "how",
    "what",
    "where",
    "can i",
    "?",
    "？",
    "方法",
    "教えて",
    "どこ",
    "できますか",
)


def validate_input(text: str) -> str:
    """Return normalized input or raise a clear error."""
    if not isinstance(text, str):
        raise TypeError("input must be text")
    normalized = " ".join(text.split())
    if not normalized:
        raise ValueError("input must not be empty")
    if len(normalized) > MAX_INPUT_LENGTH:
        raise ValueError(f"input must be at most {MAX_INPUT_LENGTH} characters")
    return normalized


def classify(text: str) -> str:
    """Classify a request into one of three bounded categories."""
    lowered = text.lower()
    if any(word in lowered for word in BUG_WORDS):
        return "bug"
    if any(word in lowered for word in QUESTION_WORDS):
        return "question"
    return "other"


def summarize(text: str, limit: int = 80) -> str:
    """Create a bounded summary without inventing information."""
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def draft_reply(category: str, language: str) -> str:
    """Create a safe draft. This function never sends anything."""
    replies = {
        "ja": {
            "bug": "ご報告ありがとうございます。発生した環境と再現手順を教えてください。",
            "question": "お問い合わせありがとうございます。確認のうえ、担当者からご案内します。",
            "other": "ご連絡ありがとうございます。内容を担当者が確認します。",
        },
        "en": {
            "bug": "Thank you for the report. Please share your environment and reproduction steps.",
            "question": "Thank you for your question. A team member will review it and respond.",
            "other": "Thank you for your message. A team member will review it.",
        },
    }
    return replies[language][category]


def detect_language(text: str) -> str:
    """Select Japanese when the input contains Japanese characters."""
    return "ja" if any("\u3040" <= char <= "\u9fff" for char in text) else "en"


def validate_output(result: Dict[str, object]) -> None:
    """Fail closed when the agent produces an unexpected result."""
    required = {"category", "summary", "reply_draft", "needs_human_review", "trace"}
    if set(result) != required:
        raise ValueError("output fields do not match the required schema")
    if result["category"] not in CATEGORIES:
        raise ValueError("category is not allowed")
    if result["needs_human_review"] is not True:
        raise ValueError("human review must remain enabled")
    if not isinstance(result["trace"], list):
        raise ValueError("trace must be a list")


def run_agent(text: str) -> Dict[str, object]:
    """Run the complete local agent workflow."""
    trace: List[str] = []
    normalized = validate_input(text)
    trace.append("input_validated")

    category = classify(normalized)
    trace.append("request_classified")

    result: Dict[str, object] = {
        "category": category,
        "summary": summarize(normalized),
        "reply_draft": draft_reply(category, detect_language(normalized)),
        "needs_human_review": True,
        "trace": trace,
    }
    trace.append("reply_drafted")

    validate_output(result)
    trace.append("output_validated")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the five-minute local agent")
    parser.add_argument(
        "--text",
        default="保存ボタンを押しても反応しません",
        help="support request to classify",
    )
    args = parser.parse_args()

    try:
        result = run_agent(args.text)
    except (TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
