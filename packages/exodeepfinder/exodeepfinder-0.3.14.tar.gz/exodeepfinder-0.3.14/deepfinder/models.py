# ============================================================================================
# DeepFinder - a deep learning approach to localize macromolecules in cryo electron tomograms
# ============================================================================================
# Copyright (c) 2019 - now
# Inria - Centre de Rennes Bretagne Atlantique, France
# Author: Emmanuel Moebel (serpico team)
# License: GPL v3.0. See <https://www.gnu.org/licenses/>
# ============================================================================================

from keras.layers import Input, concatenate
from keras.models import Model
from keras.layers import Conv3D, MaxPooling3D, UpSampling3D


# This model has been modified so that pooling is only performed on (x,y) dimensions and not in (t)
# (eml, 28/11/23)
def my_model(dim_in, Ncl):
    input = Input(shape=(dim_in, dim_in, dim_in, 1))

    x = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(input)
    high = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(x)

    x = MaxPooling3D((1, 2, 2), strides=None)(high)

    x = Conv3D(48, (3, 3, 3), padding='same', activation='relu')(x)
    mid = Conv3D(48, (3, 3, 3), padding='same', activation='relu')(x)

    x = MaxPooling3D((1, 2, 2), strides=None)(mid)

    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(64, (3, 3, 3), padding='same', activation='relu')(x)

    x = UpSampling3D(size=(1, 2, 2), data_format='channels_last')(x)
    x = Conv3D(64, (2, 2, 2), padding='same', activation='relu')(x)

    x = concatenate([x, mid])
    x = Conv3D(48, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(48, (3, 3, 3), padding='same', activation='relu')(x)

    x = UpSampling3D(size=(1, 2, 2), data_format='channels_last')(x)
    x = Conv3D(48, (2, 2, 2), padding='same', activation='relu')(x)

    x = concatenate([x, high])
    x = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(x)
    x = Conv3D(32, (3, 3, 3), padding='same', activation='relu')(x)

    output = Conv3D(Ncl, (1, 1, 1), padding='same', activation='softmax')(x)

    model = Model(input, output)
    return model