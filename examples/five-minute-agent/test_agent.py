import unittest

from agent import MAX_INPUT_LENGTH, run_agent


class AgentTests(unittest.TestCase):
    def test_classifies_japanese_bug(self):
        result = run_agent("保存ボタンを押しても反応しません")
        self.assertEqual(result["category"], "bug")

    def test_classifies_japanese_crash_as_bug(self):
        result = run_agent("アプリがクラッシュします")
        self.assertEqual(result["category"], "bug")

    def test_classifies_english_question(self):
        result = run_agent("How do I change my password?")
        self.assertEqual(result["category"], "question")

    def test_uses_other_for_unclear_input(self):
        result = run_agent("Hello from a new customer")
        self.assertEqual(result["category"], "other")

    def test_does_not_match_keyword_inside_another_word(self):
        result = run_agent("Showcase update")
        self.assertEqual(result["category"], "other")

    def test_does_not_treat_chinese_as_japanese(self):
        result = run_agent("系统错误")
        self.assertTrue(result["reply_draft"].startswith("Thank you"))

    def test_always_requires_human_review(self):
        result = run_agent("The app crashes")
        self.assertIs(result["needs_human_review"], True)

    def test_records_completed_steps(self):
        result = run_agent("The app crashes")
        self.assertEqual(
            result["trace"],
            [
                "input_validated",
                "request_classified",
                "reply_drafted",
                "output_validated",
            ],
        )

    def test_rejects_empty_input(self):
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            run_agent("   ")

    def test_rejects_oversized_input(self):
        with self.assertRaisesRegex(ValueError, "at most"):
            run_agent("x" * (MAX_INPUT_LENGTH + 1))


if __name__ == "__main__":
    unittest.main()
