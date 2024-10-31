![嗨，我是 (2)](https://github.com/user-attachments/assets/505aa5a8-f301-4a03-8dd3-1f086dd769fe)

# MinePlayer

![PyPI - Downloads](https://img.shields.io/pypi/dd/mineplayer?style=for-the-badge)![GitHub forks](https://img.shields.io/github/forks/510208/minePlayer?style=for-the-badge)![GitHub License](https://img.shields.io/github/license/510208/minePlayer?style=for-the-badge)![GitHub Repo stars](https://img.shields.io/github/stars/510208/minePlayer?style=for-the-badge)

MinePlayer 是一款簡單的模組，提供使用者解析一個 Minecraft 玩家的資訊！

MinePlayer is a simple module that allows users to parse information about a Minecraft player!
```
INFO:root:=== Create a new player. ===
INFO:root:Player Sam510208 created.
INFO:root:=== Get the player's UUID. ===
INFO:root:Player Sam510208's UUID is 9ea020446a4c4e4686b8e5d0bde8ce56.
```


## 特色 (Feature)

- 簡單易用   (Easy to use)
- 基於 GNU v3.0 開源  (Open Source based GNU v3.0)
- 支持所有相容於 CraftAvatar 的玩家頭像服務，並可自行決定  (Supports all CraftAvatar-compatible player avatar services at your discretion)
- 可取得幾乎所有 CraftAvatar 服務提供的頭像資源，甚至是玩家 Skin！  (Get access to almost all avatar assets provided by the CraftAvatar service, even player Skins!)

## 範例 (Example)
```python
import mineplayer
import logging

logging.basicConfig(level=logging.INFO)

# Create a new player
logging.info("=== Create a new player. ===")
player = mineplayer.MinePlayer("Sam510208")
logging.info(f"Player {player.username} created.")

# Get the player's UUID
logging.info("=== Get the player's UUID. ===")
uuid = player.uuid
logging.info(f"Player {player.username}'s UUID is {uuid}.")

# Get the player's information
logging.info("=== Get the player's information. ===")
info = player.info
logging.info(f"Player {player.username}'s information is {info}.")
```

範例收錄於 `test.py` 中

## 謝誌 (Thanks)
- Thank you to <a href="https://crafatar.com">Crafatar</a> for providing avatars.
- Source of inspiration: [510208/yunyubot-dc-annou](https://github.com/510208/yunyubot-dc-annou)

## 貢獻 (Countributing)
如果您希望貢獻此專案，我們非常歡迎！請Fork此儲存庫，開啟一個以自己貢獻的內容為名的分支，在該分支上開發。
開發完畢後，在GitHub頁面上提供完整說明，然後我們會盡快幫助您審核

如果您在使用此程式時出了什麼問題，歡迎在GitHub的Issues告訴我們！我們會盡力幫助您的
