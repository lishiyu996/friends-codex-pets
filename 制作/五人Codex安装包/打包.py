#!/usr/bin/env python3
"""将已完成的五人 v3 GIF 打包为保留原时序的 Codex v1 动画图集。"""

import hashlib
import json
from pathlib import Path
import zipfile

import numpy as np
from PIL import Image


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ACTORS = (
    ("罗斯", "ross", "抱恐龙书与伸手，停留时眨眼"),
    ("乔伊", "joey", "持披萨、吃披萨与眨眼"),
    ("菲比", "phoebe", "抱吉他、音符上升与眨眼"),
    ("莫妮卡", "monica", "叉腰持毛巾、抱臂与眨眼"),
    ("钱德勒", "chandler", "西装版原地眨眼"),
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(name, slug, action):
    source = ROOT / "制作" / "五人单动作预览" / name
    gif = source / f"{name}-动作预览-v3.gif"
    timeline = json.loads((source / "时间线-v3.json").read_text())
    pet_id = f"friends-{slug}-mvp"
    destination = HERE / pet_id
    destination.mkdir(exist_ok=True)
    cells, durations, sheets = [], [], []
    with Image.open(gif) as image:
        for index in range(image.n_frames):
            image.seek(index)
            durations.append(image.info["duration"])
            artwork = image.convert("RGBA").resize((180, 195), Image.Resampling.LANCZOS)
            cell = Image.new("RGBA", (192, 208))
            cell.paste(artwork, (6, 6))
            pixels = np.array(cell)
            pixels[pixels[:, :, 3] == 0, :3] = 0
            cell = Image.fromarray(pixels)
            bounds = cell.getchannel("A").getbbox()
            assert bounds and bounds[0] >= 6 and bounds[1] >= 6
            assert bounds[2] <= 186 and bounds[3] <= 202
            cells.append(cell)
            # 各状态的每个格子在同一时刻都显示相同姿态。
            # 客户端切换图集格子时，动画 WebP 仍按自己的毫秒时序播放。
            sheet = Image.new("RGBA", (1536, 1872))
            for row in range(9):
                for column in range(8):
                    sheet.paste(cell, (column * 192, row * 208))
            sheets.append(sheet)
    assert durations == [event["duration_ms"] for event in timeline["events"]]
    assert sum(durations) == timeline["cycle_ms"]
    spritesheet = destination / "spritesheet.webp"
    sheets[0].save(
        spritesheet, format="WEBP", save_all=True, append_images=sheets[1:],
        duration=durations, loop=0, lossless=True, method=4,
        background=(0, 0, 0, 0),
    )
    assert spritesheet.stat().st_size < 20 * 1024 * 1024
    with Image.open(spritesheet) as image:
        assert image.size == (1536, 1872) and image.is_animated
        assert image.n_frames == len(cells) and image.info["loop"] == 0
        decoded_durations = []
        for index, cell in enumerate(cells):
            image.seek(index)
            image.load()
            decoded_durations.append(image.info["duration"])
            # 无损编码后，检查所有 72 个格子，避免任务状态切换时闪跳。
            pixels = np.array(image.convert("RGBA"))
            # 动画 WebP 编码器可改写 alpha=0 的隐藏 RGB；显示结果不受影响。
            pixels[pixels[:, :, 3] == 0, :3] = 0
            expected = np.tile(np.array(cell), (9, 8, 1))
            assert np.array_equal(pixels, expected), (name, index)
        assert decoded_durations == durations
    manifest = {
        "id": pet_id,
        "displayName": name,
        "description": f"朝左单动作：{action}；保留 v3 节奏，所有任务及交互状态共用此循环。",
        "spriteVersionNumber": 1,
        "spritesheetPath": "spritesheet.webp",
    }
    (destination / "pet.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    with zipfile.ZipFile(HERE / f"{pet_id}.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for filename in ("pet.json", "spritesheet.webp"):
            archive.write(destination / filename, f"{pet_id}/{filename}")
    result = {
        "name": name, "pet_id": pet_id,
        "source_gif": str(gif.relative_to(ROOT)), "source_sha256": sha256(gif),
        "spritesheet": str(spritesheet.relative_to(ROOT)),
        "spritesheet_sha256": sha256(spritesheet), "size_bytes": spritesheet.stat().st_size,
        "dimensions": [1536, 1872], "encoding": "lossless animated WebP",
        "cycle_ms": sum(durations), "frame_durations_ms": durations,
        "all_72_cells_match_source_at_each_time": True,
        "comparison_ignores_hidden_rgb_at_alpha_zero": True,
        "all_states_share_single_loop": True,
        "source_artwork_modified": False,
    }
    print(json.dumps(result, ensure_ascii=False), flush=True)
    return result


if __name__ == "__main__":
    results = [build(*actor) for actor in ACTORS]
    (HERE / "打包检查.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
