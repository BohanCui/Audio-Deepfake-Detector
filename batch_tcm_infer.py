import os
import subprocess

# 配置参数
input_dir = "/Users/lanqingcui/Desktop/tcm_add-main/dataset"  # 存放 .flac 文件的目录
ckpt_path = "/Users/lanqingcui/Desktop/tcm_add-main/best_4.pth"
threshold = "-3.73"

# 遍历 .flac 文件
for filename in os.listdir(input_dir):
    if filename.endswith(".flac"):
        wav_path = os.path.join(input_dir, filename)
        print(f"🔍 正在处理: {wav_path}")

        cmd = [
            "python", "inference.py",
            "--ckpt_path", ckpt_path,
            "--threshold", threshold,
            "--wav_path", wav_path
        ]

        subprocess.run(cmd)
