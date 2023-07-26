import os
import random
import json
import numpy as np
from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataloader import default_collate


class PARTNET(Dataset):
    def __init__(self, split="train"):
        super(PARTNET, self).__init__()

        assert split in ["train", "val", "test"]
        self.split = split
        self.root_dir = your_path
        self.files = os.listdir(self.root_dir)
        self.img_transform = transforms.Compose([transforms.ToTensor()])

    def __getitem__(self, index):
        path = self.files[index]
        image = Image.open(os.path.join(self.root_dir, path, "0.png")).convert("RGB")
        image = image.resize((128, 128))
        image = self.img_transform(image)
        sample = {"image": image}

        return sample

    def __len__(self):
        return len(self.files)


class CLEVR(Dataset):
    def __init__(self, split="train", resolution=(128, 128)):
        super(CLEVR, self).__init__()

        assert split in ["train", "val", "test"]
        self.split = split
        self.resolution = resolution
        self.root_dir = os.path.join(
            "/home/oh/prog/slot-attention-pytorch/dataset/CLEVR_v1.0/images", split
        )
        self.files = os.listdir(self.root_dir)
        self.img_transform = transforms.Compose([transforms.ToTensor()])

    def __getitem__(self, index):
        path = self.files[index]
        # image = Image.open(os.path.join(self.root_dir, path, "0.png")).convert("RGB")
        image = Image.open(os.path.join(self.root_dir, path)).convert("RGB")
        image = image.resize(self.resolution)
        image = self.img_transform(image)
        sample = {"image": image}

        return sample

    def __len__(self):
        return len(self.files)
