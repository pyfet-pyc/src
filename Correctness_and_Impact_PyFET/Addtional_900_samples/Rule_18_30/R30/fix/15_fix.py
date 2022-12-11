# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import mmap
from pathlib import Path
import io
from typing import BinaryIO, List, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn.functional as F

SF_AUDIO_FILE_EXTENSIONS = {".wav", ".flac", ".ogg"}
FEATURE_OR_SF_AUDIO_FILE_EXTENSIONS = {".npy", ".wav", ".flac", ".ogg"}
