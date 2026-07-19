# コントリビューションガイド

[日本語](./CONTRIBUTING.md) | [English](./CONTRIBUTING.en.md)

誤りの報告、分かりにくい説明の改善、初心者向けサンプルの追加を歓迎します。

## Issueを作る

次の内容を短く書いてください。

- どのページまたはサンプルについてか
- 何が分かりにくい、または正しくないか
- 期待する説明や動作

APIキー、パスワード、個人情報は書かないでください。

## Pull Requestを作る

1. 変更の目的を一つに絞ります。
2. 初心者にも分かる短い表現を使います。
3. 日本語の内容を変えた場合は、対応する英語版も確認します。
4. 次のコマンドをリポジトリのルートで実行します。

```bash
python3 -m unittest discover -s examples/five-minute-agent -v
python3 scripts/check_markdown_links.py
```

Pull Requestには、変更内容、変更理由、確認結果を書いてください。

## 小さな変更を歓迎します

誤字の修正や説明の改善だけでも構いません。大きな変更は、先にIssueで目的を共有してください。
