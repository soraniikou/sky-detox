
# 空 (Sora) - Sky Minimalist App

https://sky-detox.streamlit.app

「ただ流し、ただ消し、ただ見つめるだけ。」
気が済むまで押してください。波紋が出るだけです。
ボタンを押すだけ。意味がいらないアプリです。


## 🎨 ギャラリー / Gallery

![空の写真](PXL_20260111_001520626.jpg)

*美しいグラデーションと、触れると広がる波紋が、心に静寂をもたらします。*

---

## ✨ 特徴

- 
- **波紋 (Ripple):** 画面に触れた場所に広がる静かなエフェクト。

---

## 💎 ストア（作品のこだわり）

### 1. 「間」のデザイン
ボタンを押してから色が完全に変わるまで余白の時間を設定しています。これは、デジタルの即時性から離れ、現実の空がゆっくりと移ろう情緒を再現するためです。

### 2. グラスモーフィズムUI
操作ボタンには背景をぼかす「グラスモーフィズム」を採用。背景の色を活かしつつ、空気のように自然に存在するデザインを目指しました。

## 🛠 実装の工夫（Technical Notes）

- **DOMの最適化:** 波紋エフェクトで生成された要素は、アニメーション終了後に自動で削除され、メモリ負荷を抑える設計になっています。
- **シームレスな遷移:** CSSの `transition` を活用し、JavaScriptでの色管理と組み合わせることで、途切れることのない滑らかな色彩の変化を実現しました。

---

Deploy
Streamlit Cloud
GitHubにプッシュ
Streamlit Cloud にログイン
"New app" をクリック
リポジトリを選択
デプロイ完了！
その他のオプション
Heroku
Railway
Render

Technology Stack
Frontend: Streamlit
Language: Python
Styling: Custom CSS with animations
📄 License
MIT License - 自由に使用・改変できます

Acknowledgments
このアプリは、デジタルデトックスと瞑想の概念にインスパイアされています。
Made with 💙 for mindful moments
