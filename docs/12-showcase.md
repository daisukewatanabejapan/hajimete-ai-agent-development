# OSS Showcase：実際のAGENTS.md事例

実際のOSSが `AGENTS.md` に何を書いているかを学ぶための一覧です。2026年7月20日にGitHub上の存在と内容を確認しました。各プロジェクトの方針をそのままコピーせず、自分の構成に合わせてください。

| OSS | 主な言語 | `AGENTS.md` から学べること |
| --- | --- | --- |
| [OpenAI Codex](https://github.com/openai/codex/blob/main/AGENTS.md) | Rust | crateごとの設計、レビュー規則、API互換性、テスト、変更サイズ |
| [GitHub CLI](https://github.com/cli/cli/blob/trunk/AGENTS.md) | Go | セキュリティ報告、ビルド・テスト、コマンド構造、アーキテクチャ |
| [Datadog Stratus Red Team](https://github.com/DataDog/stratus-red-team/blob/main/AGENTS.md) | Go | 新機能の追加規則、ローカル検証、明確な禁止事項 |
| [LiveKit Swift Client SDK](https://github.com/livekit/client-sdk-swift/blob/main/AGENTS.md) | Swift | ビルド・テストコマンド、必要なローカルサービス、SDKアーキテクチャ |
| [Grafana Tempo Operator](https://github.com/grafana/tempo-operator/blob/main/AGENTS.md) | Go | Operator構成、コード生成、ローカル開発・デプロイ手順 |
| [GraphFrames](https://github.com/graphframes/graphframes/blob/main/AGENTS.md) | Scala | レガシーコードの変更方針、回帰防止、複数バージョンのテスト |

## 見るポイント

1. 一般論ではなく、実際のコマンドが書かれているか
2. アーキテクチャと変更してよい境界が説明されているか
3. プロジェクト固有の危険や禁止事項があるか
4. テスト環境や外部サービスの前提が明記されているか
5. 公開APIやレガシー領域の扱いが定義されているか

リンク先は各OSSが管理しており、内容やファイルの場所は変更される場合があります。この一覧への掲載は、各プロジェクトによる本ガイドの推薦を意味しません。
