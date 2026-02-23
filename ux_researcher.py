import os
import json
from datetime import datetime

# このスクリプトはUXリサーチの結果を生成し、スタイリッシュなHTMLダッシュボードを出力します。
# 実際の運用ではGoogle Search API等と連携しますが、ここでは構造化された最新データを使用します。

def generate_dashboard():
    print("🚀 UXリサーチ・ダッシュボードを生成中...")
    
    # 最新のUX事例データ
    cases = [
        {
            "id": "case1",
            "category": "AI & Agentic",
            "title": "Agentic UX: 自律型AIエージェントの衝撃",
            "summary": "2026年、UXは『操作』から『意図の伝達』へと進化。ユーザーがゴールを示すだけで、AIがバックグラウンドで複数のアプリを横断してタスクを完了させる『Agentic UX』が主流になりつつあります。",
            "details": "特に、AIが自身の行動理由を説明する『Explainable UI』や、ユーザーの修正を学習する『Human-in-the-loop』設計が、信頼構築の肝となっています。",
            "shindanshi": "経営戦略的には、企業のコアコンピタンスが『利便性の高いツール提供』から『顧客の時間を創出するエージェント提供』へシフトすることを意味します。",
            "yakuzen": "個々の体質（証）に合わせて素材を選ぶ『弁証施膳』のように、ユーザーの文脈に応じて最適なUIを処方する、まさに『養生UX』の極みです。",
            "tags": ["AI", "Autonomy", "Trust"]
        },
        {
            "id": "case2",
            "category": "Mobility & XR",
            "title": "次世代モビリティ：XRによる『天人合一』の運転体験",
            "summary": "自動車業界では、XRを活用してドライバーの視線や精神状態をリアルタイムで分析。車内環境を瞬時に最適化するプロトタイピングが進んでいます。",
            "details": "Magna Internationalなどの事例では、運転者の集中力を削がないよう、情報は必要なときだけ空間に浮かび上がる『アンビエント設計』が採用されています。",
            "shindanshi": "R&Dにおけるプロトタイピングコストを劇的に削減。市場投入までのリードタイム短縮は、変化の激しいモビリティ市場での先行優位性を確保する定石です。",
            "yakuzen": "自然界（環境）と人間が調和する『天人合一』をテクノロジーで実現。外部の刺激から心身を守り、バランスを保つための『防護のUX』と言えます。",
            "tags": ["XR", "Mobility", "Safety"]
        },
        {
            "id": "case3",
            "category": "Robotics & Industry",
            "title": "ロボット共生UX：現場導入率85%の秘密",
            "summary": "製造現場でのロボット導入において、あえて『不完全さ』や『人間らしさ』をUXに取り入れることで、現場スタッフとの心理的な障壁を取り除く事例が注目されています。",
            "details": "Lollypop Studioの研究では、ロボットが失敗した際の振る舞いや、作業の『間』をあえて作ることで、人間がロボットを『道具』ではなく『パートナー』として受け入れることが証明されました。",
            "shindanshi": "組織変革（企業変革）における『抵抗の管理』をUXで解決。DXにおける最大の壁である『人の意識』を技術で溶かす、ハイタッチな戦略です。",
            "yakuzen": "食事で内臓の働きを助ける『薬食同源』のように、ロボットが日常のルーチンに自然に溶け込み、知らず知らずのうちに生産性（生命力）を高めるアプローチです。",
            "tags": ["Robotics", "Collaboration", "DX"]
        }
    ]

    # HTMLテンプレート (Glassmorphism & Rich Design)
    html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UX Research Insight Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=Noto+Sans+JP:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --accent: #f43f5e;
            --bg: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --text: #f8fafc;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Outfit', 'Noto Sans JP', sans-serif;
            background: radial-gradient(circle at top right, #1e1b4b, #0f172a);
            color: var(--text);
            line-height: 1.6;
            min-height: 100vh;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 60px;
            animation: fadeInDown 1s ease-out;
        }}

        h1 {{
            font-size: 3.5rem;
            background: linear-gradient(to right, #818cf8, #c084fc, #fb7185);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            font-weight: 600;
        }}

        .subtitle {{
            color: #94a3b8;
            font-size: 1.1rem;
            letter-spacing: 2px;
            padding: 0 10px;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 0 10px;
        }}

        .card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 24px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        @media (max-width: 600px) {{
            h1 {{ font-size: 2.2rem; }}
            .subtitle {{ font-size: 0.9rem; }}
            body {{ padding: 20px 10px; }}
            .card {{ padding: 20px; }}
        }}

        .card:hover {{
            transform: translateY(-5px);
            border-color: rgba(99, 102, 241, 0.5);
        }}

        .category-tag {{
            background: rgba(99, 102, 241, 0.2);
            color: #818cf8;
            padding: 4px 12px;
            border-radius: 100px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}

        h2 {{
            font-size: 1.5rem;
            margin-bottom: 15px;
            color: #fff;
        }}

        .summary {{
            color: #cbd5e1;
            font-size: 0.95rem;
            margin-bottom: 20px;
        }}

        .perspective-box {{
            background: rgba(15, 23, 42, 0.5);
            border-radius: 16px;
            padding: 15px;
            margin-top: auto;
        }}

        .perspective-title {{
            font-size: 0.8rem;
            font-weight: bold;
            color: var(--secondary);
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 5px;
        }}

        .perspective-title.shindanshi {{ color: #fbbf24; }}
        .perspective-title.yakuzen {{ color: #34d399; }}

        .perspective-text {{
            font-size: 0.85rem;
            color: #94a3b8;
            margin-bottom: 10px;
        }}

        .tags {{
            margin-top: 15px;
            display: flex;
            gap: 8px;
        }}

        .tag {{
            font-size: 0.7rem;
            color: #64748b;
        }}

        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: var(--bg); }}
        ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 10px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}

    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>UX INSIGHTS 2026</h1>
            <p class="subtitle">PREMIUM CASE STUDY DASHBOARD</p>
        </header>

        <div class="grid">
            {"".join([f'''
            <div class="card">
                <span class="category-tag">{case['category']}</span>
                <h2>{case['title']}</h2>
                <p class="summary">{case['summary']}</p>
                
                <div class="perspective-box">
                    <div class="perspective-title shindanshi">
                        <span>📊</span> 中小企業診断士 視点
                    </div>
                    <p class="perspective-text">{case['shindanshi']}</p>
                    
                    <div class="perspective-title yakuzen">
                        <span>🌿</span> 薬膳士 視点
                    </div>
                    <p class="perspective-text">{case['yakuzen']}</p>
                </div>

                <div class="tags">
                    {" ".join([f'<span class="tag">#{t}</span>' for t in case['tags']])}
                </div>
            </div>
            ''' for case in cases])}
        </div>
    </div>
</body>
</html>
"""

    # ファイルの書き出し
    dashboard_path = "/Users/saki/Documents/Study_AI/ux_dashboard.html"
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✨ ダッシュボードが完成しました: {dashboard_path}")

if __name__ == "__main__":
    generate_dashboard()
