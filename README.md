# Temporal-Channel Modeling in Multi-head Self-Attention for Synthetic Speech Detection

This Repository contains the code and pretrained models for the following INTERSPEECH 2024 paper:

* **Title** : Temporal-Channel Modeling in Multi-head Self-Attention for Synthetic Speech Detection
* **Autor** : Duc-Tuan Truong, Ruijie Tao, Tuan Nguyen, Hieu-Thi Luong, Kong Aik Lee, Eng Siong Chng

## Pretrained Model
The pretrained model XLSR can be found at [link](https://dl.fbaipublicfiles.com/fairseq/wav2vec/xlsr2_300m.pt).

You can download pretrained models from [OneDrive](https://entuedu-my.sharepoint.com/:f:/g/personal/truongdu001_e_ntu_edu_sg/El7AV62BKkdKhOYCyB3s2EkBLr-aVdj0doH0HNj9mTIsGA?e=aOlRCB). 

## Setting up environment
Python version: 3.7.16

Install PyTorch
```bash
pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```

Install other libraries:
```bash
pip install -r requirements.txt
```

Install fairseq:
```bash
git clone https://github.com/facebookresearch/fairseq.git fairseq_dir
cd fairseq_dir
git checkout a54021305d6b3c
pip install --editable ./
```


## PUT data in dataset directory.

## To test a single wav file with the pretrained model, run:
```bash
python inference.py --ckpt_path=path_to/model.pth --threshold=-3.73 --wav_path=path_to/audio.flac
```

Example: 

```bash
python inference.py --ckpt_path=/Users/lanqingcui/Desktop/tcm_add-main/best_4.pth --threshold=-3.73 --wav_path=/Users/lanqingcui/Desktop/tcm_add-main/03a02Nc.flac
```

## To see the status and log running results: 
```bash
python batch_infer_log.py
```
## Results are stored in : infer_results.txt

##  To calculate Accuracy:

```bash
Python calculate_accuracy.py
```


## Citation
```
@inproceedings{truong24b_interspeech,
  title     = {Temporal-Channel Modeling in Multi-head Self-Attention for Synthetic Speech Detection},
  author    = {Duc-Tuan Truong and Ruijie Tao and Tuan Nguyen and Hieu-Thi Luong and Kong Aik Lee and Eng Siong Chng},
  year      = {2024},
  booktitle = {Interspeech 2024},
  pages     = {537--541},
  doi       = {10.21437/Interspeech.2024-659},
  issn      = {2958-1796},
}
```

[conformer](https://github.com/lucidrains/conformer) (for Conformer model architechture).

[DHVT](https://github.com/ArieSeirack/DHVT) (for Head Token desgin).

Thanks for these authors for sharing their work!
