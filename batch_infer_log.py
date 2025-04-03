import os
import subprocess

dataset_dir = "/Users/lanqingcui/Desktop/tcm_add-main/dataset"
ckpt_path = "/Users/lanqingcui/Desktop/tcm_add-main/best_4.pth"
threshold = -3.73
log_file = "/Users/lanqingcui/Desktop/tcm_add-main/infer_results.txt"

# 已处理的文件记录
processed = set()
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if parts:
                processed.add(parts[0])

# 全部 .flac 文件
all_flacs = []
for root, dirs, files in os.walk(dataset_dir):
    for filename in files:
        if filename.endswith(".flac"):
            full_path = os.path.join(root, filename)
            all_flacs.append((filename, full_path))

# 总数 & 未处理数
total_files = len(all_flacs)
remaining = [(f, p) for f, p in all_flacs if f not in processed]
done = total_files - len(remaining)

print(f"\n📊 Total .flac files: {total_files}")
print(f"✅ Already processed: {done}")
print(f"🕒 Remaining: {len(remaining)}")
print(f"📈 Progress: {done / total_files * 100:.2f}%\n")

# 处理剩下的
with open(log_file, "a") as log:
    for filename, full_path in remaining:
        print(f"Processing {filename}...")
        result = subprocess.run(
            [
                "python", "inference.py",
                "--ckpt_path", ckpt_path,
                "--threshold", str(threshold),
                "--wav_path", full_path
            ],
            capture_output=True,
            text=True
        )

        for line in result.stdout.splitlines():
            if "Is the wav file bonafide?" in line:
                verdict = line.strip().split("->")[-1].strip()
                log.write(f"{filename}\t{verdict}\n")
                log.flush()
                break
